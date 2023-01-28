from datetime import datetime
from bytes_operation.convert_bytes import bytes_to_binary_string, bytes_to_hex_string, bytes_to_integer


def convert_unix_time(unix_time_bytes: bytes) -> datetime:
    dt = datetime.fromtimestamp(bytes_to_integer(unix_time_bytes))
    return dt


def convert_unix_permission(permission_binary: str) -> str:
    user_permission = str(int(permission_binary[0:3], 2))
    group_permission = str(int(permission_binary[3:6], 2))
    other_permission = str(int(permission_binary[6:9], 2))
    return user_permission + group_permission + other_permission


def show_mode(mode_bytes: bytes) -> str:
    mode_binary = bytes_to_binary_string(mode_bytes, digit=32)

    for i in range(2):
        start = 16 * i
        end = 16 * (i + 1)
        splitted_mode_binary = mode_binary[start:end]

        # 最初の 4 bit は object type を表す
        object_type = splitted_mode_binary[0:4]
        if object_type == '1000':
            print('object type : regular file(1000)')
        elif object_type == '1010':
            print('object type : symbolic link(1010)')
        elif object_type == '1110':
            print('object type : gitlink(1010)')
        else:
            print('Doesn\'t match mode...')

        # 次の 3 bit は使われていない
        unused = splitted_mode_binary[4:7]
        print(f'unused : {unused}')

        # 次の 9 bit は unix permission を表す
        # regular file >> 0755 or 0644
        # symbolic link, gitlink >> 0
        unix_permission = splitted_mode_binary[7:16]
        print(f'unix_permission : {convert_unix_permission(unix_permission)}')


def show_header(header: bytes) -> None:
    _4_bytes_signature = header[0:4]
    _4_byte_version_number = header[4:8]
    _32_bit_number_of_index_entries = header[8:12]
    print(_4_bytes_signature.decode())
    print(bytes_to_integer(_4_byte_version_number))
    print(bytes_to_integer(_32_bit_number_of_index_entries))


def show_entries(entries: bytes) -> None:
    _32_bit_ctime_seconds = entries[0:4]
    # TODO nanosecond_fractionsの意味を調査
    _32_bit_ctime_nanosecond_fractions = entries[4:8]
    print(
        f'ctime : {convert_unix_time(_32_bit_ctime_seconds)}.{bytes_to_integer(_32_bit_ctime_nanosecond_fractions)}'
    )
    _32_bit_mtime_seconds = entries[8:12]
    _32_bit_mtime_nanosecond_fractions = entries[12:16]
    print(
        f'mtime : {convert_unix_time(_32_bit_mtime_seconds)}.{bytes_to_integer(_32_bit_mtime_nanosecond_fractions)}'
    )
    # TODO devとは？
    _32_bit_dev = entries[16:20]
    # TODO inoとは？
    _32_bit_ino = entries[20:24]
    _32_bit_mode = entries[24:28]
    _32_bit_uid = entries[28:32]
    _32_bit_gid = entries[32:36]
    _32_bit_file_size = entries[36:40]
    print(f'dev : {bytes_to_integer(_32_bit_dev)}')
    print(f'ino : {bytes_to_integer(_32_bit_ino)}')
    show_mode(_32_bit_mode)
    print(f'uid : {bytes_to_integer(_32_bit_uid)}')
    print(f'gid : {bytes_to_integer(_32_bit_gid)}')
    print(f'size : {bytes_to_integer(_32_bit_file_size)}')
    _160_bit_object_hash = entries[40:60]
    print(f'hash : {bytes_to_hex_string(_160_bit_object_hash)}')
    _16_bit_flags = entries[60:62]
    print(f'flag : {bytes_to_integer(_16_bit_flags)}')


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
