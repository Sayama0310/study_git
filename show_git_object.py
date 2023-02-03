from typing import List
import zlib
from bytes_operation.convert_bytes import bytes_to_hex_string
import colorama
from colorama import Fore

#Initialize colorama
colorama.init(autoreset=True)


def purity_show_git_object(input_bytes: bytes):
    [header, *contents] = input_bytes.split(b'\x00')
    print(Fore.GREEN + '===== Header =====')
    print(header.decode())

    print(Fore.GREEN + '==== Contents ====')
    for content in contents:
        try:
            print(content.decode())
        except:
            print(bytes_to_hex_string(content[0:20]))
            print(Fore.GREEN + '-----------------')
            print(content[20:].decode())


def show_git_object(input_bytes: bytes):
    """
    Gitオブジェクトの中身をできるだけそのままの形で、人間にも読みやすいように整えて表示します。
    * \x00 はそのまま表示
    * \n はそのまま表示

    Args:
        bytes (bytes): _description_
    """
    [header, *contents] = input_bytes.split(b'\x00')
    decoded_string: str = ''
    decoded_string += header.decode() + r'\x00'

    decoded_contents: List[str] = []
    for content in contents:
        try:
            decoded_contents.append(content.decode().replace('\n', r'\n'))
        except:
            decoded_contents.append(
                bytes_to_hex_string(content[0:20]) + content[20:].decode())

    print(decoded_string + r'\x00'.join(decoded_contents))


if __name__ == '__main__':
    git_object_path = r'.git/objects/00/98f38b085549b5a4a725b71cba6e646b091522'
    with open(git_object_path, mode='rb') as f:
        git_object_bytes = f.read()
        decompressed_git_object_bytes = zlib.decompress(git_object_bytes)
        purity_show_git_object(decompressed_git_object_bytes)
