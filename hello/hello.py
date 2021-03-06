from flask import Flask, url_for, request, render_template, Markup

app = Flask(__name__)

with app.test_request_context('/hello', method='POST'):
    # now you can do something with the request until the
    # end of the with block, such as basic assertions:
    assert request.path == '/hello'
    assert request.method == 'POST'

@app.route('/')
def index():
    return 'index' \
           + Markup('<strong>Hello %s!</strong>') % '<blink>hacker</blink>' \
           + Markup.escape('<blink>hacker</blink>') \
           + Markup('<em>Marked up</em> &raquo; HTML').striptags()

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/map')
def map():
    return render_template('map.html')

@app.route('/login', methods=['POST', 'GET'])
#searchword = request.args.get('key', '')
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)

@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(username)

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))
    print(url_for('static', filename='style.css'))