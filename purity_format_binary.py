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


def binary_to_hex_string(
    input_bytes: bytes,
    with_prefix: bool = False,
) -> str:
    converted_string = input_bytes.hex()
    if with_prefix:
        converted_string = '0x' + converted_string
    return converted_string


def binary_to_decimal_string(input_bytes: bytes) -> str:
    converted_string = int(input_bytes.hex(), 16)
    return str(converted_string)


def binary_to_decimal_number(input_bytes: bytes) -> int:
    return int(input_bytes.hex(), 16)
