# api_fetcher.py
import requests
import sqlite3

def create_table():
    conn = sqlite3.connect('api_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS api_data (
            id INTEGER PRIMARY KEY,
            title TEXT,
            body TEXT
        )
    ''')
    conn.commit()
    conn.close()

def insert_data(data):
    conn = sqlite3.connect('api_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO api_data (title, body) VALUES (?, ?)
    ''', (data['title'], data['body']))
    conn.commit()
    conn.close()

def fetch_data():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

def view_records():
    conn = sqlite3.connect('api_data.db')
    cursor = conn.cursor()

    # Execute a query to fetch all records from the api_data table
    cursor.execute('SELECT * FROM api_data')
    
    # Fetch all records
    records = cursor.fetchall()

    # Display the records
    for record in records:
        print(record)

    conn.close()

if __name__ == "__main__":
    create_table()

    result = fetch_data()
    if result:
        print("Fetched data:")
        print(result)
        insert_data(result)
        print("Data inserted into SQLite database.")
        view_records()
    else:
        print("Failed to fetch data.")
