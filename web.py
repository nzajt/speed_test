from flask import Flask
from flask import jsonify
import sqlite3
import datetime
import statistics

app = Flask(__name__)

@app.route("/")
def hello():
    # results
    results = []
    data = []
    uploads = []
    downloads = []
    pings = []
    # sqlite connections
    conn = sqlite3.connect('results.db')
    for row in conn.execute('select * from speeds;'):
        downloads.append(row[0])
        uploads.append(row[1])
        pings.append(row[2])

        parse_results = {
                'download': row[0],
                'upload': row[1],
                'ping': row[2],
                'date': datetime.datetime.fromtimestamp(row[3]).strftime('%F %H:%M:%S')
        }
        data.append(parse_results)

    stats = {
        'averages': {
            'downloads': statistics.mean(downloads),
            'uploads': statistics.mean(uploads),
            'pings': statistics.mean(pings)
        },
        'stdev': {
            'downloads': statistics.stdev(downloads),
            'uploads': statistics.stdev(uploads),
            'pings': statistics.stdev(pings)
        },
        'min': {
            'downloads': min(downloads),
            'uploads': min(uploads),
            'pings': min(pings)
        },
        'max': {
            'downloads': max(downloads),
            'uploads': max(uploads),
            'pings': max(pings)
        }
    }

    results = {
            'data': data,
            'stats': stats
    }

    return jsonify(results)
