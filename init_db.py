import sqlite3

con = sqlite3.connect('items.db')

with open('records.sql') as f:
    con.executescript(f.read())

cur = con.cursor()

cur.execute("INSERT INTO records (Name, code, category, size, 'Unit price', inventory, color) VALUES (?, ?, ?, ?, ?, ?, ?)",
            ('Star', 'A-001', 'cloth', 'S、M', '200', '20', 'Red、Blue')
            )

cur.execute("INSERT INTO records (Name, code, category, size, 'Unit price', inventory, color) VALUES (?, ?, ?, ?, ?, ?, ?)",
            ('Moon', 'A-002', 'cloth', 'M、L', '300', '10', 'Red、White')
            )

cur.execute("INSERT INTO records (Name, code, category, size, 'Unit price', inventory, color) VALUES (?, ?, ?, ?, ?, ?, ?)",
            ('Eagle', 'B-001', 'pants', 'M、L', '100', '23', 'Green')
            )

cur.execute("INSERT INTO records (Name, code, category, size, 'Unit price', inventory, color) VALUES (?, ?, ?, ?, ?, ?, ?)",
            ('Bird', 'B-002', 'pants', 'S、M、L', '50', '12', 'Black')
            )


con.commit()
con.close()