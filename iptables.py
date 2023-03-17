# save this as app.py
from flask import Flask, render_template, redirect, url_for, request, flash, session

app = Flask(__name__)
app.secret_key='toto:tata'


@app.route("/")
def index2():

    if 'username' in session:
        return f'logged in as {session["username"]}'
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST' :
        username = request.form['username']
        password = request.form['password']
        secretToTest = username + ":" + password

        with open('passwd.txt', 'r') as f:
                lines = f.readlines()
                for line in lines:
                    line = line.strip()
                    if line == f'{username}:{password}':
                        session['username'] = username
                        return render_template ("index.html")
                    else:
                        return redirect(url_for('login'))

    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=password name=password>
            <p><input type=submit value=Login>
        </form>
        '''
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))


@app.route("/index")

def index():
    if 'username' in session:
        
        return render_template ("index.html")
    else:
        return redirect(url_for('login'))

@app.route("/alias")
def alias():
    if 'username' in session:
        
        return render_template ("Alias.html")
    else:
        return redirect(url_for('login'))

    

@app.route("/nat_filter")
def nat_filter():
    if 'username' in session:
        
        return render_template ("nat.html")
    
    else:
        return redirect(url_for('login'))
        