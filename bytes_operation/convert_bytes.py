from icecream import ic


def bytes_to_integer(input_bytes: bytes) -> int:
    return int.from_bytes(input_bytes, byteorder='big')


def bytes_to_binary_string(
    input_bytes: bytes,
    with_prefix: bool = False,
    digit: int = -1,
) -> str:
    converted_string = bin(bytes_to_integer(input_bytes))
    if digit > 0 & len(converted_string) - 2 < digit:
        to_be_inserted_zero_number = digit - len(converted_string) + 2
        converted_string = converted_string[:2] + \
                            ('0' * to_be_inserted_zero_number) + \
                            converted_string[2:]
    if with_prefix is False:
        converted_string = converted_string[2:]
    return converted_string


def bytes_to_decimal_string(input_bytes: bytes) -> str:
    converted_string = str(bytes_to_integer(input_bytes))
    return converted_string


def bytes_to_hex_string(
    input_bytes: bytes,
    with_prefix: bool = False,
) -> str:
    converted_string = hex(bytes_to_integer(input_bytes))
    if with_prefix is False:
        converted_string = converted_string[2:]
    return converted_string


if __name__ == '__main__':
    input = b'\x01\x34'
    ic(bytes_to_binary_string(input))
