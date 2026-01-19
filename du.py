import math
import os
import sys

from os import PathLike
from pathlib import Path


class FileTreeNode:
    """Basic file tree walking functionality. You probably want os.walk instead."""
    def __init__(self, path: PathLike):
        self.path = Path(path)
        self.subdirs = [] #list[FileTreeNode]
        self.files = [] #list[tuple[str, int]]
        self.cached_size = 0

    def __str__(self):
        size_k = math.floor(self.size() / 1024)
        size_M = math.floor(self.size() / (1024 * 1024))
        if size_M > 0:
            return f"{size_M}M {self.path}"
        if size_k > 0:
            return f"{size_k}k {self.path}"
        return f"{self.size()}\t{self.path}"

    def add(self, filename: str, size: int):
        self.files.append((filename, size))

    def size(self):
        if self.cached_size > 0:
            return self.cached_size
        total = 0
        total += sum(i.size() for i in self.subdirs)
        total += sum(i[1] for i in self.files)
        self.cached_size = total
        return total

    def scan_file_tree(self):
        self.subdirs = []
        self.files = []
        for i in self.path.iterdir():
            if i.is_dir():
                self.subdirs.append(FileTreeNode(i))
            if i.is_file():
                file_size = os.path.getsize(i)
                self.add(i, file_size)
        for sub in self.subdirs:
            sub.scan_file_tree()

    def print_sizes_recursively(self):
        for i in self.subdirs:
            i.print_sizes_recursively()
        print(self)


if __name__ == "__main__":
    root_path = '.'
    if len(sys.argv) == 2:
        root_path = sys.argv[1]

    root_node = FileTreeNode(root_path)
    root_node.scan_file_tree()
    root_node.print_sizes_recursively()

    # for dir_path, dir_names, filenames in os.walk(root_path):
    #     node = FileTreeNode(dir_path)
    #     nodes[dir_path] = node
    #     for filename in filenames:
    #         abs_path = PurePath(os.path.join(dir_path, filename))
    #         file_size = os.path.getsize(abs_path)
    #         node.add(filename, file_size)
    #     print(node)
