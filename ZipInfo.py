import sys
from zipfile import ZipFile
import io

def findInf(zipF):
    n = 0
    c = 0
    for i in zipF.infolist():
        if i.is_dir() == False:
            c = c + 1
        n = n + i.file_size
    return c, n


z = ZipFile(io.BytesIO(bytes.fromhex(sys.stdin.read())), 'r')
print(*findInf(z))

