from bytes_operation.convert_bytes import bytes_to_integer
from git_index.index_entry import IndexEntry
import colorama
from colorama import Fore

#Initialize colorama
colorama.init(autoreset=True)


def show_header(header: bytes) -> None:
    _4_bytes_signature = header[0:4]
    _4_byte_version_number = header[4:8]
    _32_bit_number_of_index_entries = header[8:12]
    print(_4_bytes_signature.decode())
    print(bytes_to_integer(_4_byte_version_number))
    print(bytes_to_integer(_32_bit_number_of_index_entries))
    print(Fore.GREEN + '==================================')


def get_entry_number(header: bytes) -> int:
    _32_bit_number_of_index_entries = header[8:12]
    return bytes_to_integer(_32_bit_number_of_index_entries)


def show_entries(entries: bytes, entry_number: int) -> bytes:
    entries_bytearraay = bytearray(entries)
    for _ in range(entry_number):
        entry = IndexEntry(entries_bytearraay)
        entry.show()
        print(Fore.GREEN + '==================================')
    return bytes(entries_bytearraay)


def divide_content(content: bytes) -> tuple[bytes, bytes]:
    header = content[:12]
    entries = content[12:]
    return header, entries


def read_index(index_path: str) -> bytes:
    with open(index_path, mode='rb') as f:
        return f.read()


if __name__ == '__main__':
    index_path = r'.git/index'
    content = read_index(index_path)
    header, entries_extension = divide_content(content)
    show_header(header)
    entry_number = get_entry_number(header)
    extension = show_entries(entries_extension, entry_number)
    print(extension)
