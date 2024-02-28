import sqlite3

conn = sqlite3.connect('assets/test.db')
info = conn.execute('''
SELECT * FROM users;
''')
for a in info:
  print(a)
conn.commit()
conn.close()