def divide_content(content: bytes) -> tuple[bytes, bytes, bytes]:
    header = content[:12]
    entries_extension = content[12:]
    
    return header, entries, extension
