#!/usr/bin/env python3
"""
Python SDK API 生成器：从 api-definitions.json 生成 API 类。
每个接口使用完整请求体 Dict；文档字符串按树状层级列出请求/响应全部字段（与 MerchantApiDocs 点分路径一致）。
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BASE_DIR = ROOT / "jiuwufen_sdk"
API_DEFINITIONS_PATH = ROOT.parent / "tools" / "api-definitions.json"


def snake_case(s: str) -> str:
    return s.replace("-", "_")


def to_camel_case(s: str) -> str:
    if not s:
        return ""
    return s[0].upper() + s[1:]


def _split_path(name: str) -> list:
    return [p for p in name.split(".") if p]


def _build_level_tree(params: list) -> dict:
    """点分路径 -> 树：segment -> { 'param': 原始字段或 None, 'children': 子树 }"""

    def ensure(parent: dict, seg: str) -> dict:
        if seg not in parent:
            parent[seg] = {"param": None, "children": {}}
        return parent[seg]

    tree: dict = {}
    for p in params:
        parts = _split_path(p.get("name", ""))
        if not parts:
            continue
        cur_level = tree
        for i, part in enumerate(parts):
            node = ensure(cur_level, part)
            if i == len(parts) - 1:
                node["param"] = p
            cur_level = node["children"]
    return tree


def _format_level_tree(tree: dict, base_path: str, indent_unit: str, depth: int) -> list[str]:
    lines: list[str] = []
    for seg in sorted(tree.keys()):
        node = tree[seg]
        path = f"{base_path}.{seg}" if base_path else seg
        prefix = indent_unit * (2 + depth)
        if node["param"] is not None:
            p = node["param"]
            typ = p.get("type", "Any")
            req = "必填" if p.get("required") else "选填"
            desc = (p.get("description") or "").strip()
            tail = f": {desc}" if desc else ""
            lines.append(f"{prefix}- {path} ({typ}, {req}){tail}")
        if node["children"]:
            lines.extend(_format_level_tree(node["children"], path, indent_unit, depth + 1))
    return lines


def format_params_hierarchy(params: list, indent_unit: str = "  ") -> str:
    """按层级缩进输出全部字段（完整点分路径）。"""
    if not params:
        return f"{indent_unit * 2}（无）"
    tree = _build_level_tree(params)
    lines = _format_level_tree(tree, "", indent_unit, 0)
    return "\n".join(lines) if lines else f"{indent_unit * 2}（无）"


def generate_api_class(module_name: str, apis: list) -> str:
    class_name = to_camel_case(module_name) + "Api"

    code = f'''"""
{class_name.replace("Api", "")} API
"""

from typing import Any, Dict


class {class_name}:
    """{class_name.replace("Api", "")} API"""

    def __init__(self, client):
        self.client = client
'''

    for api in apis:
        method_name = snake_case(api["id"])
        path = api["path"]
        doc = api.get("description") or api.get("name") or ""
        req_params = api.get("requestParams") or []
        resp_params = api.get("responseParams") or []
        req_tree = format_params_hierarchy(req_params)
        resp_tree = format_params_hierarchy(resp_params)

        code += f'''
    def {method_name}(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """
        {doc}

        请求体字段（树状层级，与文档点分路径一致）:
{req_tree}

        响应 data 内常见字段（树状层级，供对照文档）:
{resp_tree}

        Args:
            body: 完整 JSON 请求体，须包含各层级嵌套对象/数组结构。

        Returns:
            响应 JSON（通常为业务 data 对象）
        """
        return self.client.request("{path}", body)
'''

    return code


def main():
    print("开始生成 Python SDK API 类...")

    if not API_DEFINITIONS_PATH.exists():
        print(f"❌ 找不到 API 定义文件: {API_DEFINITIONS_PATH}")
        return

    with open(API_DEFINITIONS_PATH, "r", encoding="utf-8") as f:
        api_definitions = json.load(f)

    api_dir = BASE_DIR / "api"
    api_dir.mkdir(exist_ok=True)

    for old_file in api_dir.glob("*.py"):
        if old_file.name != "__init__.py":
            old_file.unlink()

    init_imports = []
    init_all = []

    for module_name, apis in api_definitions["modules"].items():
        original_module_name = module_name
        if module_name == "return":
            module_name = "returns"

        class_name = to_camel_case(module_name) + "Api"
        code = generate_api_class(original_module_name, apis)
        file_path = api_dir / f"{module_name}.py"

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(code)

        print(f"✅ 生成: api/{module_name}.py")
        init_imports.append(f"from .{module_name} import {class_name}")
        init_all.append(class_name)

    init_code = '"""API 模块"""\n\n'
    init_code += "\n".join(init_imports)
    init_code += "\n\n__all__ = [\n"
    init_code += ",\n".join(f'    "{name}"' for name in init_all)
    init_code += "\n]\n"

    with open(api_dir / "__init__.py", "w", encoding="utf-8") as f:
        f.write(init_code)

    print("✅ 生成: api/__init__.py")
    print("✨ 所有 API 类生成完成！")


if __name__ == "__main__":
    main()
