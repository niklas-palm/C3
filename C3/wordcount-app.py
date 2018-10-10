from flask import Flask, jsonify
import subprocess
import sys

app = Flask(__name__)

@app.route('/wordcount/api/v1.0/go', methods=['GET'])

def wordcount-server():
   #data=subprocess.check_output(["python","wordCount.py"])
   data = 'heeey'
   return data
      
if __name__ == '__main__':
          app.run(host='0.0.0.0',debug=True)
