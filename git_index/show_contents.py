from bytes_operation.convert_bytes import bytes_to_integer
import colorama
from colorama import Fore

from git_index.index_entry import IndexEntry

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


def show_entries(entries: bytes, entry_number: int) -> bytes:
    entries_bytearraay = bytearray(entries)
    for _ in range(entry_number):
        entry = IndexEntry(entries_bytearraay)
        entry.show()
        print(Fore.GREEN + '==================================')
    return bytes(entries_bytearraay)
