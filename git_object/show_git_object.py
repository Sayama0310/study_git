from typing import List
from bytes_operation.purity_format_binary import binary_to_hex_string


def purity_show_git_object(bytes: bytes):
    [header, *contents] = bytes.split(b'\x00')
    print(f'===== Header =====\n{header.decode()}')

    print('==== Contents ====')
    for content in contents:
        try:
            print(content.decode())
        except:
            print(binary_to_hex_string(content[0:20]))
            print('-----------------')
            print(content[20:].decode())


def show_git_object(bytes: bytes):
    """
    Gitオブジェクトの中身をできるだけそのままの形で、人間にも読みやすいように整えて表示します。
    * \x00 はそのまま表示
    * \n はそのまま表示

    Args:
        bytes (bytes): _description_
    """
    [header, *contents] = bytes.split(b'\x00')
    decoded_string: str = ''
    decoded_string += header.decode() + r'\x00'

    decoded_contents: List[str] = []
    for content in contents:
        try:
            decoded_contents.append(content.decode().replace('\n', r'\n'))
        except:
            decoded_contents.append(
                binary_to_hex_string(content[0:20]) + content[20:].decode())

    print(decoded_string + r'\x00'.join(decoded_contents))