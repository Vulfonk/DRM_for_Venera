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
        # создание таблицы эталонов

        cur.execute("""CREATE TABLE IF NOT EXISTS FilesHash (
            Id INTEGER PRIMARY KEY,
            RelativePath TEXT,
            Hash TEXT,
            EtalonId,
            FOREIGN KEY (EtalonID) REFERENCES Etalons(Id)
        )""")
        # создание таблицы для хэшей файлов

        self.db.commit()

    def del_etalon(self, folder_path):

        cur = self.db.cursor()

        select_query = f"""
            SELECT Id
            FROM Etalons
            WHERE AbsolutePath = '{folder_path}'
            LIMIT  1
        """

        cur.execute(select_query)
        result = cur.fetchone()[0]

        delete_query = f"""
            DELETE 
            FROM Etalons
            WHERE Id = '{result}'
        """

        cur.execute(delete_query)

        delete_query = f"""
            DELETE 
            FROM FilesHash
            WHERE EtalonId = '{result}'
        """
        cur.execute(delete_query)
        self.db.commit()

    def update_etalon(self, dict_hashes_obj: DictHashesClass):
        self.del_etalon(dict_hashes_obj.dirr_path)
        self.add_etalon(dict_hashes_obj)

    def add_etalon(self, dict_hashes_obj: DictHashesClass):
        dict_hashes = dict_hashes_obj.dict_hashes
        folder_path = dict_hashes_obj.dirr_path
        self.db = sqlite3.connect(self.db_name)
        cur = self.db.cursor()

        cur.execute(f"""
            INSERT INTO Etalons (AbsolutePath) 
            VALUES ('{folder_path}');
        """)

        select_query = f"""
            SELECT Id
            FROM Etalons
            WHERE AbsolutePath = '{folder_path}'
            LIMIT  1
        """

        cur.execute(select_query)
        result = cur.fetchone()[0]

        for pair in dict_hashes:
            relative_path = '.' + pair.replace(folder_path, '', 1)
            hash_sha = dict_hashes[pair]['sha256']

            insert_query = f"""
                INSERT INTO FilesHash (RelativePath, Hash, EtalonId) 
                VALUES ('{relative_path}', '{hash_sha}','{result}')
                """

            cur.executescript(insert_query)

        self.db.commit()

    def view_hash_table(self, is_absolute_path):
        cur = self.db.cursor()
        select_query = f"""
            SELECT * 
            FROM FilesHash
        """
        cur.execute(select_query)
        files_query_result = cur.fetchall()

        if not is_absolute_path:
            return files_query_result

        select_query = f"""
            SELECT AbsolutePath, Id
            FROM Etalons
        """

        cur.execute(select_query)
        etalons_query_result = cur.fetchall()

        return files_query_result

    def view_etalons_list(self, is_absolute_path):
        cur = self.db.cursor()
        select_query = f"""
                   SELECT * 
                   FROM Etalons
               """
        cur.execute(select_query)
        etalons_query_result = cur.fetchall()
        return etalons_query_result

    def view_etalon_hashes(self, etalon_path):
        cur = self.db.cursor()

        select_query = f"""
                          SELECT Id 
                          FROM Etalons
                          WHERE AbsolutePath = '{etalon_path}'
                      """
        cur.execute(select_query)
        etalons_query_result = cur.fetchall()
        select_query = f"""
                          SELECT * 
                          FROM FilesHash
                          WHERE EtalonId = '{etalons_query_result[0][0]}'
                      """
        cur.execute(select_query)

        files_query_result = cur.fetchall()

        return files_query_result

    def __del__(self):
        self.db.close()
