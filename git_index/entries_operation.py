from bytes_operation.convert_bytes import bytes_to_integer


def get_entry_number(header: bytes) -> int:
    _32_bit_number_of_index_entries = header[8:12]
    return bytes_to_integer(_32_bit_number_of_index_entries)


def get_entries_length(
    entries_extension: bytes,
    entries_number: int,
) -> int:
    entries_extension_bytearray = bytearray(entries_extension)
    while len(entries_extension_bytearray) > 0:
        size = __get_next_entry_size(entries_extension_bytearray)
        __skip_entry(entries_extension_bytearray, size)
    pass
