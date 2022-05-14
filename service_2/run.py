from flask import Flask
import os

app = Flask(__name__)

@app.route("/service-2")
def home():
    print("service 2 called.......")
    return "service-2 called"


if __name__ == '__main__':
    app.run(debug=True, host=os.environ.get('HOST', '0.0.0.0'),port=int(os.environ.get('PORT', 6000)))