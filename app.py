from speed import Speed
import sqlite3
import time

# Connect to database
c = sqlite3.connect('results.db')

# Create db if it doesn't exists
c.execute('''CREATE TABLE IF NOT EXISTS speeds
             (download FLOAT, upload FLOAT, ping FLOAT, created_at DATETIME)''')

# Get speeds
s = Speed()
r = s.results
upload = r['upload']
download = r['download']
ping = r['ping']
now = time.time()
print(upload, download, ping)

# Add to dabates
c.execute('INSERT INTO speeds VALUES (?,?,?,?)', [download, upload, ping, now])
c.commit()
c.close
