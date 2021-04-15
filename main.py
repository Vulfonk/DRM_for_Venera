import hash_example
import CreateDB

database = CreateDB.HashesDataBase("TestingDataBase")
hash_obj = hash_example.DictHashesClass("C:\\Users\\1\\Desktop\\Теория вероятностей и статистика", {'py', 'txt'})
database.add_etalon(hash_obj)
database.add_etalon(hash_obj)
