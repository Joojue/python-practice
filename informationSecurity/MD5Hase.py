import hashlib
import os, sys

def getHash(path, blocksize=65536):
    afile = open(path, 'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()

file = "C:/Users/sdwrd/Desktop/코딩/python/PythonWorkspace/python-3.11.0-embed-win32.zip"
 
if os.path.exists(file):
    fileHash = getHash(file)
    print(fileHash)
else:
    print('%s is not a valid path, please verify' % file)
    sys.exit()