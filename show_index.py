from git_index.entry import Entries
from git_index.extension import Extension
from git_index.header import Header


def read_index(index_path: str) -> bytes:
    with open(index_path, mode='rb') as f:
        return f.read()


def semantical_read(content: bytes) -> tuple[Header, Entries, Extension]:
    header = Header(content[0:12])
    entries, remaining = Entries.feeder_constructor(
        content[12:],
        header.number_of_index_entries,
    )
    extension = Extension(remaining)
    return header, entries, extension


if __name__ == '__main__':
    index_path = r'.git/index'
    content = read_index(index_path)
    header, entries, extension = semantical_read(content)
    header.show()
    entries.show()
    extension.show()
