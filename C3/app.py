#!flask/bin/python
from flask import Flask, jsonify
from CODE.tasks import wordCount

app = Flask(__name__)

@app.route('/', methods=['GET'])
def wordcountServer():
   #data=subprocess.check_output(["python","wordCount.py"])
   print('A new request!') #Prints on server.
    
   res = wordCount.delay()
    
   return jsonify(res.get())

if __name__ == '__main__':
          app.run(host='0.0.0.0', debug=True)
