import time
from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
def hello():
    time.sleep(60)  # Sleep for 60 seconds
    return redirect("https://trustedge.com/", code = 302)

if __name__ == '__main__':
    app.run(debug=True)
