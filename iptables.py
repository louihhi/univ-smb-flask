# save this as app.py
from flask import Flask, render_template, redirect, url_for, request, flash, session
from flask import jsonify
import json

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
        

@app.route('/get_content')
def get_content():
    with open('alias.json', 'r') as f:
        content = json.load(f)
    return jsonify(content)

@app.route('/json')
def json1():
    return '''
            <h1>Contenu de alias.json</h1>
            <table>
                <thead>
                    <tr>
                        <th>alias</th>
                        <th>ip address</th>
                        <th>port</th>
                    </tr>
                </thead>
                <tbody id="tableBody">
                </tbody>
            </table>

            <script>
            function getContent() {
                fetch('/get_content')
                    .then(response => response.json())
                    .then(data => {
                        const tableBody = document.getElementById('tableBody');
                        let tableHtml = '';
                        for (let i = 0; i < data.length; i++) {
                            const item = data[i];
                            tableHtml += `<tr><td>${item.alias}</td><td>${item.ip_address}</td><td>${item.port}</td></tr>`;
                        }
                        tableBody.innerHTML = tableHtml;
                    });
            }

            document.addEventListener('DOMContentLoaded', getContent);
            window.onload = getContent
            setInterval(getContent, 60000);
            </script>



    '''