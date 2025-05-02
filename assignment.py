import os
import importlib
from pathlib import Path


def read_file(file_path: str) -> str:
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()


def write_file(file_path: str, content: str) -> None:
    direct = os.path.dirname(file_path)
    if direct and not os.path.exists(direct):
        os.makedirs(direct)
    with open(file_path, 'w', encoding='utf-8') as f:
        return f.write(content)


def list_files_in_directory(directory_path: str) -> list:
    path = Path(directory_path)
    if not path.is_dir():
        return []
    
    files = []
    for p in path.iterdir():
        if p.is_file():
            files.append(p.name)
    return files



def generate_numbers(n: int) -> iter:
    for i in range(n):
        yield i


def use_function_from_module(module_name: str, function_name: str, *args) -> any:
    mod = importlib.import_module(module_name)
    f = getattr(mod, function_name)
    return f(*args)