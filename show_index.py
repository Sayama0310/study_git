from datetime import datetime
from purity_format_binary import binary_to_decimal_number, binary_to_decimal_string, binary_to_hex_string, bytes_to_binary_string, purity_show_binary_data


def show_unix_time(unix_time_bytes: bytes) -> datetime:
    dt = datetime.fromtimestamp(binary_to_decimal_number(unix_time_bytes))
    return dt

def perse_mode(mode_bytes: bytes) -> str:
    bytes_to_binary_string()


def show_header(header: bytes) -> None:
    _4_bytes_signature = header[0:4]
    _4_byte_version_number = header[4:8]
    _32_bit_number_of_index_entries = header[8:12]
    print(_4_bytes_signature.decode())
    print(binary_to_decimal_string(_4_byte_version_number))
    print(binary_to_decimal_string(_32_bit_number_of_index_entries))


def show_entries(entries: bytes) -> None:
    _32_bit_ctime_seconds = entries[0:4]
    # TODO nanosecond_fractionsの意味を調査
    _32_bit_ctime_nanosecond_fractions = entries[4:8]
    print(
        f'ctime : {show_unix_time(_32_bit_ctime_seconds)}.{binary_to_decimal_string(_32_bit_ctime_nanosecond_fractions)}'
    )
    _32_bit_mtime_seconds = entries[8:12]
    _32_bit_mtime_nanosecond_fractions = entries[12:16]
    print(
        f'mtime : {show_unix_time(_32_bit_mtime_seconds)}.{binary_to_decimal_string(_32_bit_mtime_nanosecond_fractions)}'
    )
    # TODO devとは？
    _32_bit_dev = entries[16:20]
    # TODO inoとは？
    _32_bit_ino = entries[20:24]
    _32_bit_mode = entries[24:28]
    print(_32_bit_mode)
    _32_bit_uid = entries[28:32]
    _32_bit_gid = entries[32:36]
    _32_bit_file_size = entries[36:40]
    print(f'dev : {binary_to_decimal_string(_32_bit_dev)}')
    print(f'ino : {binary_to_decimal_string(_32_bit_ino)}')
    print(f'mode : {binary_to_decimal_string(_32_bit_mode)}')
    print(f'uid : {binary_to_decimal_string(_32_bit_uid)}')
    print(f'gid : {binary_to_decimal_string(_32_bit_gid)}')
    print(f'size : {binary_to_decimal_string(_32_bit_file_size)}')
    _160_bit_object_hash = entries[40:60]
    print(f'hash : {binary_to_hex_string(_160_bit_object_hash)}')
    _16_bit_flags = entries[60:62]
    print(f'flag : {binary_to_decimal_string(_16_bit_flags)}')


def divide_content(content: bytes) -> tuple[bytes, bytes]:
    header = content[:12]
    entries = content[12:]
    return header, entries


def read_index(index_path: str) -> bytes:
    with open(index_path, mode='rb') as f:
        return f.read()


if __name__ == '__main__':
    index_path = r'.git/index'
    content = read_index(index_path)
    header, entries = divide_content(content)
    show_header(header)
    show_entries(entries)
