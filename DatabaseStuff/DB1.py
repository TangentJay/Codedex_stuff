import psycopg2

conn = psycopg2.connect(host='localhost', dbname='postgres', user='postgres', password='1234', port=5432)


curs = conn.cursor()

curs.execute("""CREATE TABLE IF NOT EXISTS stuff (
             id INT PRIMARY KEY,
             name VARCHAR(255),
             age INT,
             thing VARCHAR(25)
             );
             """)



curs.execute("""insert into stuff(id, name, age, thing) values 
             (1, 'bob', 10873, 'Dino'),
             (2, 'key', 1337, 'Gfios'),  
             (3, 'yellow', 21, 'lemon'),
             (4, 'moo', 420, 'Goat'),  
             (5, 'nana', 69, 'Affe'),
             (6, 'supa', 1, 'cape')
             on conflict (id) do nothing;    

""")


curs.execute("select * from stuff where age > 100;")
for row in curs.fetchall():
    print(row)
curs.execute("select * from stuff order by age desc;")
for desc in curs.fetchall():
    print(desc)

print(curs.fetchall())
conn.commit()



curs.close()


conn.close()