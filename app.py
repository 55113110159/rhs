import time
from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome to the Flask App!'

@app.route('/redirect')
def redirect_to_main_website():
    # Replace 'https://example.com' with the actual URL of your main website
    time.sleep(60)  # Sleep for 60 seconds
    return redirect('https://trustedge.com')

if __name__ == '__main__':
    app.run(debug=True)
