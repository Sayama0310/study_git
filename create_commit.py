import hashlib
import zlib
from purity_format_binary import purity_show_binary_data

# commitオブジェクトの中身
content = """tree 0cdbafebf15332c0788686f2457a87d8ea3ddbf5
parent 8add7f0af64c4166aa39f3b2430c07c2f3bd3d4f
author Sayama <sayama@example.co.jp> 1673766412 +0900
committer Sayama <sayama@example.co.jp> 1673766412 +0900

README.mdと同じ内容のファイルを作成
""".encode()

# headerのフォーマットは「commit <content_size>\0」
content_size = len(content)
header = f'commit {content_size}\0'.encode()

# zlibによる圧縮
commit = zlib.compress(header + content, level=1)
purity_show_binary_data(commit)

# SHA-1にハッシュ値の計算
hash = hashlib.sha1(header + content).hexdigest()
print(hash)
