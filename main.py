import zlib
from purity_format_binary import purity_show_binary_data
from show_git_object import purity_show_git_object, show_git_object

with open(
        './compressed_files/87/f3f8afa28796b2eeda4094bee471acbde78dcc',
        'rb',
) as f:
    content = f.read()
    decompressed = zlib.decompress(content)
    purity_show_git_object(decompressed)
    show_git_object(decompressed)
    purity_show_binary_data(decompressed)
