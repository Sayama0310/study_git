import hashlib
import zlib
from bytes_operation.purity_format_binary import purity_show_binary_data

# blobオブジェクトの中身
content = """# カレーのレシピ
美味しいカレーを作ろう！
""".encode()

# headerのフォーマットは「blob <content_size>\0」
content_size = len(content)
header = f'blob {content_size}\0'.encode()

# zlibによる圧縮
blob = zlib.compress(header + content, level=1)
purity_show_binary_data(blob)

# SHA-1にハッシュ値の計算
hash = hashlib.sha1(header + content).hexdigest()
print(hash)
