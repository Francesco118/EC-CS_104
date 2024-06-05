import sqlite3
from users import users

conn = sqlite3.connect('people.db')
cursor = conn.cursor()

# with open('users.py', 'r') as file:
#     data = json.load(file)

for user in users:
    cursor.execute('''INSERT INTO users (username, password, level) 
                      VALUES (?, ?, ?)''', (user['username'], user['password'], user['auth_level']))

conn.commit()
conn.close()
