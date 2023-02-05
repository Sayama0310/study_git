from datetime import datetime
from typing import List, Type, TypeVar
from bytes_operation.convert_bytes import bytes_to_binary_string, bytes_to_hex_string, bytes_to_integer
import colorama
from colorama import Fore

#Initialize colorama
colorama.init(autoreset=True)

# ファクトリメソッドで自身の型を返却することが現状できないみたい？
# See. https://github.com/python/typing/issues/58
T = TypeVar('T', bound='Entries')


class Entry:

    def __init__(self, entry_bytearray: bytearray) -> None:
        # index version >= 3 は未対応
        self.entry_bytes = bytes(entry_bytearray)
        file_name_size = self.get_file_name_size()
        self.entry_bytes = bytes(entry_bytearray[0:62 + file_name_size])
        next_entry_bytes_start = self._next_8_multiple(62 + file_name_size)
        entry_bytearray[:] = entry_bytearray[next_entry_bytes_start:]

    def _next_8_multiple(self, number: int):
        # number が 8 の倍数だったときは +8 をして返却
        remain = 8 - (number % 8)
        return number + remain

    def show(self):
        self.show_ctime()
        self.show_mtime()
        self.show_dev()
        self.show_ino()
        self.show_mode()
        self.show_uid()
        self.show_gid()
        self.show_size()
        self.show_hash()
        self.show_flag()
        self.show_file_name()

    def show_ctime(self):
        _32_bit_ctime_seconds = self.entry_bytes[0:4]
        # TODO nanosecond_fractionsの意味を調査
        _32_bit_ctime_nanosecond_fractions = self.entry_bytes[4:8]
        print(
            f'ctime : {self._convert_unix_time(_32_bit_ctime_seconds)}.{bytes_to_integer(_32_bit_ctime_nanosecond_fractions)}'
        )

    def show_mtime(self):
        _32_bit_mtime_seconds = self.entry_bytes[8:12]
        _32_bit_mtime_nanosecond_fractions = self.entry_bytes[12:16]
        print(
            f'mtime : {self._convert_unix_time(_32_bit_mtime_seconds)}.{bytes_to_integer(_32_bit_mtime_nanosecond_fractions)}'
        )

    def _convert_unix_time(self, unix_time_bytes: bytes) -> datetime:
        dt = datetime.fromtimestamp(bytes_to_integer(unix_time_bytes))
        return dt

    def show_dev(self):
        _32_bit_dev = self.entry_bytes[16:20]
        print(f'dev : {bytes_to_integer(_32_bit_dev)}')

    def show_ino(self):
        _32_bit_ino = self.entry_bytes[20:24]
        print(f'ino : {bytes_to_integer(_32_bit_ino)}')

    def show_mode(self):
        mode_binary = bytes_to_binary_string(self.entry_bytes[24:28], digit=32)

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
            print(
                f'unix_permission : {self._convert_unix_permission(unix_permission)}'
            )

    def _convert_unix_permission(self, permission_binary: str) -> str:
        user_permission = str(int(permission_binary[0:3], 2))
        group_permission = str(int(permission_binary[3:6], 2))
        other_permission = str(int(permission_binary[6:9], 2))
        return user_permission + group_permission + other_permission

    def show_uid(self):
        _32_bit_uid = self.entry_bytes[28:32]
        print(f'uid : {bytes_to_integer(_32_bit_uid)}')

    def show_gid(self):
        _32_bit_gid = self.entry_bytes[32:36]
        print(f'gid : {bytes_to_integer(_32_bit_gid)}')

    def show_size(self):
        _32_bit_file_size = self.entry_bytes[36:40]
        print(f'size : {bytes_to_integer(_32_bit_file_size)}')

    def show_hash(self):
        _160_bit_object_hash = self.entry_bytes[40:60]
        print(f'hash : {bytes_to_hex_string(_160_bit_object_hash)}')

    def show_flag(self):
        _16_bit_flags = self.entry_bytes[60:62]
        binary_flag = bytes_to_binary_string(_16_bit_flags, digit=16)
        print(f'assume-valid flag : {binary_flag[0:1]}')
        print(f'extended flag : {binary_flag[1:2]}')
        print(f'stage : {binary_flag[2:4]}')
        print(f'name length : {int(binary_flag[4:16], 2)}')

    def show_file_name(self):
        file_name_size = self.get_file_name_size()
        _file_name_bytes = self.entry_bytes[62:62 + file_name_size]
        file_name = ''
        try:
            file_name = _file_name_bytes.decode()
        except Exception as e:
            file_name = 'Error!!'
        print(f'file name : {file_name}')

    def get_file_name_size(self):
        _16_bit_flags = self.entry_bytes[60:62]
        binary_flag = bytes_to_binary_string(_16_bit_flags, digit=16)
        return int(binary_flag[4:16], 2)


class Entries:

    def __init__(self) -> None:
        self.entries: List[Entry] = []

    @classmethod
    def feeder_constructor(
        cls: Type[T],
        entries_bytes_and_remaining: bytes,
        number_of_index_entries: int,
    ) -> tuple[T, bytes]:
        entries = Entries()
        entries_extension_bytearray = bytearray(entries_bytes_and_remaining)
        for _ in range(number_of_index_entries):
            entries.append(Entry(entries_extension_bytearray))
        return entries, bytes(entries_extension_bytearray)

    def append(self, entry: Entry):
        self.entries.append(entry)

    def show(self):
        print(Fore.BLUE + '============= ENTRIES ============')
        for entry in self.entries:
            entry.show()
            print(Fore.BLUE + '==================================')
