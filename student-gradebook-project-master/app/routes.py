from flask import render_template,url_for,redirect
from flask import request
from app import app

database = ['bob']
passDatabase = ['sob']
teacherList = ['bob']
teacher = 'tree'
@app.route('/', methods=['GET', 'POST'])
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     error = None
#     if request.method == 'POST':
#         # if valid_login(request.form['username'],
#         #                request.form['password']):
#         if request.form['username'] != 'admin' or request.form['password'] != 'admin':
#             print('YAY')
#             return log_the_user_in(request.form['username'])
#         else:
#             error = 'Invalid username/password'
#     return render_template('login.html',error=error)


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            a= request.form['username']
            print(a)
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('teacher'))
    return render_template('login.html', error=error)


@app.route('/student')
def student():
    
    return render_template('student.html')

@app.route('/teacher')
def teacher():
    return render_template('teacher.html')


def valid_login(username,password):
    if username in database and password in passDatabase:
        return True
    else:
        return False


def log_the_user_in(username):
    if username in teacherList:
        return redirect(url_for('teacher'))
    else:
        return redirect(url_for('student'))