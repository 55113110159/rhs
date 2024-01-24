from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome to the Flask App!'

@app.route('/redirect')
def redirect_to_main_website():
    # Replace 'https://example.com' with the actual URL of your main website
    return redirect('https://trustedge.com/', code = 302)

if __name__ == '__main__':
    app.run(debug=True)
