import psycopg2

conn = psycopg2.connect(host='localhost', dbname='postgres', user='postgres', password='1234', port=5432)


curs = conn.cursor()

curs.execute("""CREATE TABLE IF NOT EXISTS stuff (
             id INT PRIMARY KEY,
             name VARCHAR(255),
             age INT,
             thing CHAR
             );
             """)



curs.execute("""insert into stuff(id, name, age, thing) values 
             (1, 'bob', 80, 'Dino'),
             (2, 'key', 37, 'Gfio'),  
             (3, 'yellow', 21, 'lemon'),
             (4, 'moo', 42, 'Goat'),  
             (5, 'nana', 69, 'Affe')    

""")




conn.commit()



curs.close()


conn.close()