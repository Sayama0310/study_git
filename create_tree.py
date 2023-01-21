import hashlib
import zlib
from purity_format_binary import purity_show_binary_data

# treeオブジェクトの中身
content = '100644 README.md'.encode()            + b'\0' + bytes.fromhex('944b8ef2e83aea596fd2a662d629042f3e92edc3') \
        + '100644 curry-ingredients.md'.encode() + b'\0' + bytes.fromhex('87f3f8afa28796b2eeda4094bee471acbde78dcc') \
        + '40000 dir'.encode()                   + b'\0' + bytes.fromhex('6fc8f11b5d479640d1c79f9f8697c35f66d08f67')

# headerのフォーマットは「tree <content_size>\0」
content_size = len(content)
header = f'tree {content_size}\0'.encode()

# zlibによる圧縮
tree = zlib.compress(header + content, level=1)
purity_show_binary_data(tree)

# SHA-1でハッシュ値の計算
hash = hashlib.sha1(header + content).hexdigest()
print(hash)
