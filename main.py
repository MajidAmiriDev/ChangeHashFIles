import os
import hashlib
entries = os.listdir('list')
for entry in entries:
    md5_hash = hashlib.md5()
    with open("list/"+entry,"rb") as f:
        for byte_block in iter(lambda: f.read(4096),b""):
            md5_hash.update(byte_block)
        print(md5_hash.hexdigest())
