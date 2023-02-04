from typing import List
from git_index.divide_content import divide_content
from git_index.header import Header
from git_index.show_contents import show_header, show_entries, show_extension
from git_index.entries_operation import get_entry_number


def read_index(index_path: str) -> bytes:
    with open(index_path, mode='rb') as f:
        return f.read()


def semantical_read(content: bytes) -> tuple[Header, Entries, Extension]:
    header = Header(content[0:12])
    entries = []
    for _ in range(header.number_of_index_entries):
        pass


if __name__ == '__main__':
    index_path = r'.git/index'
    content = read_index(index_path)
    header, entries, extension = semantical_read(content)
    header.show()
    for entry in entries:
        entry.show()
    extension.show()
