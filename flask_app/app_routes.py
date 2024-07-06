from flask import request, render_template, redirect, url_for, make_response
from flask import Flask
import pandas as pd
import subprocess
import json
import os

app = Flask(__name__)

def is_json_file_empty(file_path):
    return os.path.getsize(file_path) == 0

def run_scraper(start, end):
    process = subprocess.Popen(
        ['scrapy', 'crawl', 'scraper', '-a', f'start={start}', '-a', f'end={end}', '-O', 'output.json'],
        cwd=os.path.join(os.path.dirname(__file__), '../safer'),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    stdout, stderr = process.communicate()
    if process.returncode != 0:
        raise Exception(f"Scrapy returned a non-zero exit code: {stderr.decode('utf-8')}")
    if is_json_file_empty(os.path.join(os.path.dirname(__file__), '../safer/output.json')):
        raise Exception("No data found in the given range")
    else:
        with open(os.path.join(os.path.dirname(__file__), '../safer/output.json'), 'r') as f:
            return json.load(f)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        start = int(request.form['start'])
        end = int(request.form['end'])
        if start > end:
            return render_template('error.html', data={'error': "Start value must be less than or equal to end value."})
        elif start < 0 or end < 0:
            return render_template('error.html', data={'error': "Start and end values must be non-negative."})
        try:
            scraped_data = run_scraper(start, end)
            return render_template('success.html',data=scraped_data)        
        except Exception as e:
            return render_template('error.html',data={'error':f"An error occurred: {e}"})  
    
    return render_template('index.html')

@app.route('/download')
def download_csv():
    with open(os.path.join(os.path.dirname(__file__), '../safer/output.json'), 'r') as f:
        jo =  json.load(f)
    df = pd.DataFrame(jo)
    csv_data = df.to_csv(index=False)
    output = make_response(csv_data)
    output.headers["Content-Disposition"] = "attachment; filename=scraped_data.csv"
    output.headers["Content-type"] = "text/csv"
    return output
    
if __name__ == '__main__':
    app.run(debug=True)
