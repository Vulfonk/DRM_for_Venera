import sqlite3

db = sqlite3.connect('DRM-etalon.db')
cur = db.cursor()

    # Создаем таблицу
cur.execute("""CREATE TABLE IF NOT EXISTS Etalons (
    Id INTEGER PRIMARY KEY,
    AbsolutePath TEXT,
    CONSTRAINT AK_AbsolutePath UNIQUE(AbsolutePath)
)""")
db.commit()

cur.execute("""CREATE TABLE IF NOT EXISTS FilesHash (
    Id INTEGER PRIMARY KEY,
    RelativePath TEXT,
    Hash TEXT,
    EtalonId,
    FOREIGN KEY (EtalonID) REFERENCES Etalons(Id)
)""")
db.commit()