import colorama
from colorama import Fore
from bytes_operation.convert_bytes import bytes_to_integer

#Initialize colorama
colorama.init(autoreset=True)


class Header:

    def __init__(self, header_bytes: bytes) -> None:
        # bytes_contents
        self.__4_bytes_signature = header_bytes[0:4]
        self.__4_byte_version_number = header_bytes[4:8]
        self.__32_bit_number_of_index_entries = header_bytes[8:12]
        # semantic_contents
        self.signature: str = self.__4_bytes_signature.decode()
        self.version_number: int = bytes_to_integer(
            self.__4_byte_version_number)
        self.number_of_index_entries: int = bytes_to_integer(
            self.__32_bit_number_of_index_entries)

    def show(self):
        print(Fore.GREEN + '============= HEADER =============')
        self.__show_signature()
        self.__show_version_number()
        self.__show_number_of_index_entries()
        print(Fore.GREEN + '==================================')

    def __show_signature(self):
        print(f'signature : {self.signature}')

    def __show_version_number(self):
        print(f'version_number : {self.version_number}')

    def __show_number_of_index_entries(self):
        print(f'number_of_index_entries : {self.number_of_index_entries}')
