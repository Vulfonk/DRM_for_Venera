import hash_example
import CreateDB

database = CreateDB.HashesDataBase("TestingDataBase2")
try:
    hash_obj = hash_example.DictHashesClass("C:\\Windows\\System32", {'exe', 'dll'})
    database.add_etalon(hash_obj)
except CreateDB.sqlite3.IntegrityError:
    print("хэши для данной папки уже созданы")
for i in database.view_hash_table(is_absolute_path=True):
    print(i)
