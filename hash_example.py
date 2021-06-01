import os
import hashlib
from functools import partial
from datetime import datetime

class DictHashesClass(object):

    def __init__(self, dirr, ext, res=None):
        if res is None:
            res = {}
        for current_folder in list(os.walk(dirr)):
            for current_file in current_folder[2]:
                path_to_file = current_folder[0] + "\\" + current_file
                if os.path.splitext(path_to_file)[1][1:] in ext:
                    self.__get_hash__(path_to_file, res)
        self.dict_hashes = res
        self.dirr_path = dirr
        
    def __get_hash__(self, file, res):
        res[str(file)] = {}
        with open(str(file), "rb") as f:      
            sha256 = hashlib.sha256()
            for buf in iter(partial(f.read, 2048), b''):
                sha256.update(buf)
            res[str(file)]["sha256"] = sha256.hexdigest()
        return res

def Equal(turple_etalons, dict):
    lis = []
    dir_path = dict.dirr_path

    for turp in turple_etalons:
        path = turp[1].replace('.', dir_path, 1)
        try:
            hash = dict.dict_hashes[path]["sha256"]
            lis.append((turp[1],
                        turp[2],
                        datetime.now(),
                        "Хэш совпадает" if turp[2] == hash else "Хэш не совпадает"))
        except Exception:
            lis.append((turp[1],
                       turp[2],
                       datetime.now(),
                       "Файл отсутствует"))


    return  lis


def search_item(searched_elem, list_turp: dict,  dir_path):
    hash = list_turp[searched_elem]["sha256"]
    for elem in list_turp.values():
        rel_path = elem.replace(dir_path, '.')
        if rel_path == searched_elem:
            return elem
