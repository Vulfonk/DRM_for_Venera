import os
import hashlib
import sqlite3
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


def add_etalon(folder_path, name_program, ext):
    db = sqlite3.connect('DRM-etalon.db')
    dict_hashes  = get_hashes(folder_path, ext)
    cur = db.cursor()

    cur.execute(
        f"""INSERT INTO Etalons (AbsolutePath, NameProgram) 
        VALUES ('{folder_path}','{name_program}');""")

    select_query = f"""SELECT Id
            FROM Etalons
            WHERE AbsolutePath = '{folder_path}'
            LIMIT  1"""
            
    cur.execute(select_query)
    result = cur.fetchone()[0]

    for pair in dict_hashes:
        relative_path = '.' + pair.replace(folder_path, '', 1)
        hash_sha = dict_hashes[pair]['sha256']

        insert_query =f"""INSERT INTO FilesHash (RelativePath, Hash, EtalonId) 
                VALUES ('{relative_path}', '{hash_sha}','{result}')
                """ 
        
        cur.executescript(insert_query)
    db.commit()

add_etalon(r"C:\Users\1\Desktop\Python scripts", "test", ["py", "doc", "xlsx", "rtf", "txt"])
