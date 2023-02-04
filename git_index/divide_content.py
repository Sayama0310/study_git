from git_index.entries_operation import get_entries_length, get_entry_number


def __divide_entries_extension(
    entries_extension: bytes,
    entries_number: int,
) -> tuple[bytes, bytes]:
    entries_length = get_entries_length(entries_extension, entries_number)
    entries = entries_extension[:entries_length]
    extension = entries_extension[entries_length:]
    return entries, extension


def divide_content(content: bytes) -> tuple[bytes, bytes, bytes]:
    header = content[:12]
    entries_extension = content[12:]
    entries_number = get_entry_number(header)
    entries, extension = __divide_entries_extension(
        entries_extension,
        entries_number,
    )
    return header, entries, extension
