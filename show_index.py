from git_index.divide_content import divide_content
from git_index.show_contents import show_header, show_entries, show_extension
from git_index.entries_operation import get_entry_number


def read_index(index_path: str) -> bytes:
    with open(index_path, mode='rb') as f:
        return f.read()


if __name__ == '__main__':
    index_path = r'.git/index'
    content = read_index(index_path)
    header, entries, extension = divide_content(content)
    show_header(header)
    show_entries(entries, get_entry_number(header))
    show_extension(extension)
