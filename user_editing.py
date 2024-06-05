import sqlite3
from flask import Flask, request, jsonify
from users import users

app = Flask(__name__)

DATABASE = "people.db"

def query_db(query, args=(), one=False):
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute(query, args)
    rv = cur.fetchall()

    # Commit the changes if they are an UPDATE
    if query.startswith("UPDATE"):
        conn.commit()

    conn.close()
    return (rv[0] if rv else None) if one else rv

@app.route('/')
def index():
    return "<h1>User Database Management</h1><p>Authorized Users Only</p><p>By Johannes Castellano & Cia. Ltda.</p>"

@app.route('/revise')
def revise_user():
    username = request.args.get('username').lower()
    new_auth = request.args.get('auth')

    if not username:
        return jsonify({"error": "Please provide a username."})

    user = query_db("SELECT * FROM users WHERE LOWER(username) = ?", [username], one=True)

    if not user:
        return jsonify({"error": "User not found."})
    
    if new_auth is not None:
        try:
            new_auth = int(new_auth)  # Ensure it's a valid integer
            query_db("UPDATE users SET auth_level = ? WHERE LOWER(username) = ?", [new_auth, username])
            user = query_db("SELECT * FROM users WHERE LOWER(username) = ?", [username], one=True)  # Fetch updated user
        except ValueError:
            return jsonify({"error": "Invalid authorization level."})

    return jsonify(dict(user))  # Convert sqlite3.Row to dictionary

if __name__ == '__main__':
    app.run(debug=True)