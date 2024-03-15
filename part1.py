import requests
import sqlite3

# Create or connect to the SQLite database
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Create the users table using spl
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        firstName TEXT,
        lastName TEXT,
        email TEXT,
        ...
    )
''')

# Create the posts table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS posts (
        id INTEGER PRIMARY KEY,
        userId INTEGER,
        title TEXT,
        body TEXT,
        FOREIGN KEY (userId) REFERENCES users(id)
    )
''')

# Fetch user data from the API from given link
url = 'https://dummyapi.io/data/v1/user'
headers = {'app-id': 'YOUR_APP_ID'}  # Replace with your actual app ID
response = requests.get(url, headers=headers)
users_data = response.json()['data']

# Insert user data into the database using command
for user in users_data:
    cursor.execute('''
        INSERT INTO users (id, firstName, lastName, email, ...)
        VALUES (?, ?, ?, ?, ...)
    ''', (user['id'], user['firstName'], user['lastName'], user['email'], ...))

    # Fetch posts data for each user they insert
    posts_url = f'https://dummyapi.io/data/v1/user/{user["id"]}/post'
    posts_response = requests.get(posts_url, headers=headers)
    posts_data = posts_response.json()['data']

    # Insert posts data into the database
    for post in posts_data:
        cursor.execute('''
            INSERT INTO posts (id, userId, title, body)
            VALUES (?, ?, ?, ?)
        ''', (post['id'], user['id'], post['title'], post['body']))

conn.commit()

# Close the database connection
conn.close()
