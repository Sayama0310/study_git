import colorama
from colorama import Fore

#Initialize colorama
colorama.init(autoreset=True)


class Extension:

    def __init__(self, extension_bytes: bytes) -> None:
        self.__extension_bytes = extension_bytes

    def show(self):
        print(Fore.YELLOW + '============ EXTENSION ===========')
        print(self.__extension_bytes)
        print(Fore.YELLOW + '==================================')
