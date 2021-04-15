import hash_example
import CreateDB

database = CreateDB.HashesDataBase("TestingDataBase2")
try:
    hash_obj = hash_example.DictHashesClass("C:\\Users\\1\\Desktop\\Покер-бот", {'py', 'txt'})
    database.add_etalon(hash_obj)
except CreateDB.sqlite3.IntegrityError:
    print("хэши для данной папки уже созданы")
for i in database.view_hash_table():
    print(i)
