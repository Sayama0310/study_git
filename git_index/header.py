import colorama
from colorama import Fore
from bytes_operation.convert_bytes import bytes_to_integer

#Initialize colorama
colorama.init(autoreset=True)


class Header:

    def __init__(self, header_bytes: bytes) -> None:
        # bytes_contents
        self._4_bytes_signature = header_bytes[0:4]
        self._4_byte_version_number = header_bytes[4:8]
        self._32_bit_number_of_index_entries = header_bytes[8:12]
        # semantic_contents
        self.signature: str = self._4_bytes_signature.decode()
        self.version_number: int = bytes_to_integer(
            self._4_byte_version_number)
        self.number_of_index_entries: int = bytes_to_integer(
            self._32_bit_number_of_index_entries)

    def show(self):
        print(Fore.GREEN + '============= HEADER =============')
        self._show_signature()
        self._show_version_number()
        self._show_number_of_index_entries()
        print(Fore.GREEN + '==================================')

    def _show_signature(self):
        print(f'signature : {self.signature}')

    def _show_version_number(self):
        print(f'version_number : {self.version_number}')

    def _show_number_of_index_entries(self):
        print(f'number_of_index_entries : {self.number_of_index_entries}')
