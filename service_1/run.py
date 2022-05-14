from flask import Flask
from datetime import datetime
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..')))

from client.restClient import ServiceTwoClient


app = Flask(__name__)

@app.route("/service-1")
def home():
    rs = ServiceTwoClient.get_user()
    print("service- 1: ", rs)
    return rs


if __name__ == '__main__':
    app.run(debug=True,host=os.environ.get('HOST', '0.0.0.0'), port=int(os.environ.get('PORT', 5000)))