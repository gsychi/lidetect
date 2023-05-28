# Python script
from datetime import datetime, timedelta
from flask import Flask, render_template
from flask import jsonify
import json
from flask_ngrok import run_with_ngrok

app = Flask(__name__,static_url_path='', 
            static_folder='web/static',
            template_folder='web/templates')


@app.route('/')
def home():
   return render_template('index.html')

@app.route('/call_python_function/<string:input_string>')
def call_python_function(input_string):
    if len(input_string) == 0:
        return

    # Invoke the Python function and get the result
    return jsonify(("hello"))

if __name__ == '__main__':
    app.run(debug=True,port=8080)