#!/usr/bin/env python3
"""
Python SDK API 和模型生成器
自动从 api-definitions.json 生成 SDK 代码。
"""

import os
import json
from pathlib import Path

BASE_DIR = Path("/Users/admin/promptflow-open/sdk/python-sdk/jiuwufen_sdk")
API_DEFINITIONS_PATH = Path("/Users/admin/promptflow-open/sdk/tools/api-definitions.json")

def snake_case(s: str) -> str:
    """连字符转下划线"""
    return s.replace("-", "_")

def to_camel_case(s: str) -> str:
    if not s:
        return ""
    return s[0].upper() + s[1:]

def generate_api_class(module_name: str, apis: list) -> str:
    """生成 API 类代码"""
    class_name = to_camel_case(module_name) + "Api"
    
    code = f'''"""
{class_name.replace("Api", "")} API
"""

from typing import Any, Dict, Optional, List


class {class_name}:
    """{class_name.replace("Api", "")} API"""
    
    def __init__(self, client):
        """初始化 API"""
        self.client = client
'''
    
    for api in apis:
        # Convert endpoint IDs like `get-reference-price` to `get_reference_price`
        method_name = snake_case(api["id"])
        path = api["path"]
        doc = api["description"] or api["name"]
        
        # Build params
        params = []
        param_dict_items = []
        request_params = sorted(api.get("requestParams", []), key=lambda x: not x.get("required", False))
        for param in request_params:
            name = param["name"]
            # Skip nested fields
            if "." in name:
                continue
            
            ptype = param.get("type", "Any")
            if ptype == "string": py_type = "str"
            elif ptype == "int" or ptype == "long" or ptype == "number": py_type = "int"
            elif ptype == "bool" or ptype == "boolean": py_type = "bool"
            elif "[]" in ptype or ptype == "array": py_type = "list"
            elif ptype == "object": py_type = "dict"
            else: py_type = "Any"
            
            if not param.get("required", False):
                params.append(f"{name}: Optional[{py_type}] = None")
            else:
                params.append(f"{name}: {py_type}")
                
            param_dict_items.append(f"'{name}': {name}")
        
        param_list = ", ".join(["self"] + params)
        if len(params) == 0:
            param_dict = "{}"
        else:
            param_dict = "{" + ", ".join(param_dict_items) + "}"
            
        # Filter out None values from the param_dict at runtime if optional parameters are used
        req_kwargs = "{" + f"k: v for k, v in {param_dict}.items() if v is not None" + "}"

        code += f'''
    def {method_name}({param_list}) -> Dict[str, Any]:
        """
        {doc}
        
        Returns:
            响应数据
        """
        params_dict = {req_kwargs}
        return self.client.request("{path}", params_dict)
'''
    
    return code


def main():
    """主函数"""
    print("开始生成 Python SDK API 类...")
    
    if not API_DEFINITIONS_PATH.exists():
        print(f"❌ 找不到 API 定义文件: {API_DEFINITIONS_PATH}")
        return
        
    with open(API_DEFINITIONS_PATH, 'r', encoding='utf-8') as f:
        api_definitions = json.load(f)
        
    api_dir = BASE_DIR / "api"
    api_dir.mkdir(exist_ok=True)
    
    # 清理旧文件（保留 __init__.py 直到最后写入）
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
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(code)
        
        print(f"✅ 生成: api/{module_name}.py")
        
        init_imports.append(f"from .{module_name} import {class_name}")
        init_all.append(class_name)
    
    init_code = '"""API 模块"""\n\n'
    init_code += '\n'.join(init_imports)
    init_code += '\n\n__all__ = [\n'
    init_code += ',\n'.join(f'    "{name}"' for name in init_all)
    init_code += '\n]\n'
    
    with open(api_dir / "__init__.py", 'w', encoding='utf-8') as f:
        f.write(init_code)
    
    print(f"✅ 生成: api/__init__.py")
    print(f"\n✨ 所有 API 类生成完成！")


if __name__ == "__main__":
    main()
