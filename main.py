import zlib
from purity_format_binary import purity_show_binary_data
from show_git_object import purity_show_git_object, show_git_object

with open(
        './compressed_files/0c/dbafebf15332c0788686f2457a87d8ea3ddbf5',
        'rb',
) as f:
    content = f.read()
    decompressed = zlib.decompress(content)
    purity_show_git_object(decompressed)
    show_git_object(decompressed)
    print()
    print('Compressed Git Object')
    purity_show_binary_data(content)
    print('Decompressed Git Object')
    purity_show_binary_data(decompressed)
