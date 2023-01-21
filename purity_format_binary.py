from typing import List


def purity_show_binary_data(bytes: bytes):
    line: List[str] = []
    for byte in bytes:
        line.append('{0:02x}'.format(byte))

    output: str = ''
    for idx in range(len(line)):
        if idx % 16 != 15:
            output += f'{line[idx]} '
        else:
            output += f'{line[idx]}\n'
    output.rstrip()
    print(output)


def binary_to_hex_string(bytes: bytes) -> str:
    line: List[str] = []
    for byte in bytes:
        line.append('{0:02x}'.format(byte))
    return ''.join(line)