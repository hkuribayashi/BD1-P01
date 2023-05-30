import io
import pandas as pd

df = pd.read_csv('data.csv', sep=",")
sql = "\n"
for index, row in df.iterrows():
    sql += "CREATE DATABASE a{};".format(row['matricula'])
    sql += "\n"
    sql += "CREATE USER 'a{}'@'%' IDENTIFIED BY 'a{}';".format(row['matricula'], row['matricula'])
    sql += "\n"
    sql += "GRANT ALL PRIVILEGES ON a{}.* to 'a{}'@'%';".format(row['matricula'], row['matricula'])
    sql += "\n"
    sql += "FLUSH PRIVILEGES;"
    sql += "\n"
    sql += "\n"

with open("create_tables.sql", "w", encoding="utf-8") as f:
    f.write(sql)

