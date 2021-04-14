import os
import hashlib
import sqlite3
from glob import glob
from functools import partial

class DictHashesClass(object):

    def __init__(self, dirr, ext, res = {}):
        files = []
        for current_folder in list(os.walk(dirr)):
            for current_file in current_folder[2]:
                path_to_file = current_folder[0] + "\\" + current_file
                if os.path.splitext(path_to_file)[1][1:] in ext:
                    self.get_hash(path_to_file, res)
        self.dict_hashes = res
        self.dirr_path = dirr
        
    def get_hash(self, file, res):
        res[str(file)] = {}
        with open(str(file), "rb") as f:      
            sha256 = hashlib.sha256()
            for buf in iter(partial(f.read, 2048), b''):
                sha256.update(buf)
            res[str(file)]["sha256"] = sha256.hexdigest()
        return res
