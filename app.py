from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/index')
def index():
    age = "i am 99 "
    return render_template('index.html', x= age)

@app.route('/about')
def about():
    name= "Shwetank"
    return render_template('about.html', name=name)

@app.route('/boot')
def style():
    return render_template('boot.html')


if __name__ == "__main__":
    
    app.run(debug=True)