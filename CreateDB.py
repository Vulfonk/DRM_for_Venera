import sqlite3
from hash_example import DictHashesClass


class HashesDataBase(object):
    def __init__(self, name):
        self.db_name = name
        self.db = sqlite3.connect(name)
        cur = self.db.cursor()

        cur.execute("""CREATE TABLE IF NOT EXISTS Etalons (
            Id INTEGER PRIMARY KEY,
            AbsolutePath TEXT,
            CONSTRAINT AK_AbsolutePath UNIQUE(AbsolutePath)
        )""")
        self.db.commit()

        cur.execute("""CREATE TABLE IF NOT EXISTS FilesHash (
            Id INTEGER PRIMARY KEY,
            RelativePath TEXT,
            Hash TEXT,
            EtalonId,
            FOREIGN KEY (EtalonID) REFERENCES Etalons(Id)
        )""")
        self.db.commit()

    def add_etalon(self, dict_hashes_obj: DictHashesClass):
        dict_hashes = dict_hashes_obj.dict_hashes
        folder_path = dict_hashes_obj.dirr_path
        self.db = sqlite3.connect(self.db_name)
        cur = self.db.cursor()

        cur.execute(
            f"""INSERT INTO Etalons (AbsolutePath) 
            VALUES ('{folder_path}');""")

        select_query = f"""SELECT Id
                FROM Etalons
                WHERE AbsolutePath = '{folder_path}'
                LIMIT  1"""

        cur.execute(select_query)
        result = cur.fetchone()[0]

        for pair in dict_hashes:
            relative_path = '.' + pair.replace(folder_path, '', 1)
            hash_sha = dict_hashes[pair]['sha256']

            insert_query = f"""INSERT INTO FilesHash (RelativePath, Hash, EtalonId) 
                    VALUES ('{relative_path}', '{hash_sha}','{result}')
                    """

            cur.executescript(insert_query)
        self.db.commit()

    def __del__(self):
        self.db.close()
