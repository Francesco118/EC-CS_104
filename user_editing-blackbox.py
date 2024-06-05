from flask import Flask, request, jsonify
#from users import users
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
    return "User Database Management Authorized Users Only <br> Johannes Castellano"

@app.route("/revise", methods=["GET"])
def revise_user():
    # Create a new SQLite connection and cursor for each request
    conn = sqlite3.connect('people.db')
    cursor = conn.cursor()

    # Get the username parameter
    username = request.args.get("username")

    # If no username is provided, return an error message
    if not username:
        return jsonify({"error": "Please provide a username."}), 400

    # Query the database for the user with the given username
    cursor.execute("SELECT * FROM users WHERE username=?", (username,))
    user = cursor.fetchone()

    # If the user is not found, return a 404 error
    if not user:
        return jsonify({"error": "User not found"}), 404

    # If a new authorization level is provided, update the user's auth level
    new_auth = request.args.get("auth")
    if new_auth:
        cursor.execute("UPDATE users SET auth=? WHERE username=?", (new_auth, username))
        conn.commit()
        cursor.execute("SELECT * FROM users WHERE username=?", (username,))
        user = cursor.fetchone()

    # Close the SQLite connection
    conn.close()

    # Return the user information as a JSON object
    return jsonify({
        "userid": user[0],
        "username": user[1],
        "password": user[2],
        "auth": user[3]
    })

if __name__ == "__main__":
    app.run(debug=True, threaded=False)