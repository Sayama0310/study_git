from bytes_operation.convert_bytes import bytes_to_integer


def get_entry_number(header: bytes) -> int:
    _32_bit_number_of_index_entries = header[8:12]
    return bytes_to_integer(_32_bit_number_of_index_entries)
