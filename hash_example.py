import os
import hashlib
from glob import glob
from functools import partial

def get_hashes(dirr, ext, res = {}):
    files = []
    for current_folder in list(os.walk(dirr)):
        for current_file in current_folder[2]:
            path_to_file = current_folder[0] + "\\" + current_file
            if os.path.splitext(path_to_file)[1][1:] in ext:
                get_hash(path_to_file, res)
    return res

def get_hash(file, res):
    res[str(file)] = {}
    with open(str(file), "rb") as f:      
        sha256 = hashlib.sha256()
        for buf in iter(partial(f.read, 2048), b''):
            sha256.update(buf)
        res[str(file)]["sha256"] = sha256.hexdigest()
    return res

dict_hashes  = get_hashes(r"C:\Users\1\Desktop\Диплом Венеры", ["pdf", "doc", "xlsx", "rtf", "txt"])
for pair in dict_hashes:
    print(pair + "=" + dict_hashes[pair]['sha256'])
