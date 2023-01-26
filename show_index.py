from datetime import datetime
from purity_format_binary import binary_to_decimal_number, binary_to_decimal_string, purity_show_binary_data


def show_unix_time(unix_time_bytes: bytes) -> datetime:
    dt = datetime.fromtimestamp(binary_to_decimal_number(unix_time_bytes))
    return dt


def show_header(header: bytes) -> None:
    _4_bytes_signature = header[0:4]
    _4_byte_version_number = header[4:8]
    _32_bit_number_of_index_entries = header[8:12]
    print(_4_bytes_signature.decode())
    print(binary_to_decimal_string(_4_byte_version_number))
    print(binary_to_decimal_string(_32_bit_number_of_index_entries))


def show_entries(entries: bytes) -> None:
    _32_bit_ctime_seconds = entries[:4]
    _32_bit_ctime_nanosecond_fractions = entries[4:8]
    print(show_unix_time(_32_bit_ctime_seconds))
    # TODO nanosecond_fractionsの意味を調査
    print(show_unix_time(_32_bit_ctime_nanosecond_fractions))


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
