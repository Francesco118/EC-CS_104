import sqlite3

conn = sqlite3.connect('people.db')  # Create or connect to the database
cursor = conn.cursor()  # Create a cursor object

# Create the table (if it doesn't exist)
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT,
                    password TEXT,
                    level INTEGER
                )''')

conn.commit()  # Save the changes
conn.close()   # Close the connection
