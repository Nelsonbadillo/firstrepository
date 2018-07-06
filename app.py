from flask import Flask, render_template

app = Flask(__name__)
app.config["TEMPLATE_AUTO_RELOAD"] = True

@app.route('/')
def layout():
    return render_template('index.html')

@app.route('/Contact')
def contact():
    return render_template('Contact.html')

@app.route('/About_me')
def about_me():
    return render_template('About_me.html')







