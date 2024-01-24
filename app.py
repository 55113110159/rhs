import time
from flask import Flask, redirect

app = Flask(__name__)

@app.route('/redirect')
def redirect_to_main_website():
    # Replace 'https://example.com' with the actual URL of your main website
    time.sleep(5)  # Sleep for 60 seconds
    return redirect("https://trustedge.com/", code = 302)

if __name__ == '__main__':
    app.run(debug=True)
