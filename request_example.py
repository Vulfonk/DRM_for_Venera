import os
import hashlib
from glob import glob
from functools import partial

def get_hashes(dirr, ext):
    files = os.listdir(dirr)
    directoryPath  = dirr + "\*."
    fileExtensions = ext
    listOfFiles    = []
    for extension in fileExtensions:
        listOfFiles.extend( glob( directoryPath + extension ))
    return _get_hashes(listOfFiles)

def _get_hashes(files):
    res = {}
    for file in files:
        res[str(file)] = {}
        with open(str(file), "rb") as f:      
            sha256 = hashlib.sha256()
            for buf in iter(partial(f.read, 2048), b''):
                sha256.update(buf)
            res[str(file)]["sha256"] = sha256.hexdigest()
    return res
    

get_hashes("C:\diplom", ["pdf", "doc", "xlsx", "rtf"])