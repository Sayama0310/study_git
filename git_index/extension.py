class Extension:

    def __init__(self, extension_bytes: bytes) -> None:
        self.__extension = extension_bytes

    def show(self):
        print(Fore.BLUE + '============= ENTRIES ============')
        print(Fore.BLUE + '==================================')
        print()
