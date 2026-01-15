import sys
from os import PathLike
from pathlib import Path


def all_dirs(path: PathLike) -> list[PathLike]:
    return [x for x in path.iterdir() if x.is_dir()]


def count_of_dir_contents(path: PathLike) -> int:
    return len([x for x in path.iterdir()])


def contains_nested_duplicate(path: PathLike) -> bool:
    duplicate_path = path / path
    return duplicate_path.is_dir()


def contains_only_nested_duplicate(path: PathLike) -> bool:
    return contains_nested_duplicate(path) and count_of_dir_contents(path) == 1


if __name__ == '__main__':
    root_path = '.'
    if len(sys.argv) == 2:
        root_path = sys.argv[1]

    root = Path(root_path)
    dirs_with_nested_duplicate = [
        x for x in all_dirs(root) if contains_only_nested_duplicate(root / x)
    ]

    for d in dirs_with_nested_duplicate:
        parent = d.resolve()
        sub = (d / d.name).resolve()
        print(f'mv \'{sub}\\*\' \'{parent}\'')
        print(f'rmdir \'{sub}\'')
