# You can add to this file in the editor 
import pyotp
import sqlite3 
import hashlib
import uuid   
from flask import Flask, request
app = Flask(__name__)

db_name = "test.db"

@app.route("/")
def index():
    return "Welcome to the hands-on lab for an evolution of password systems"

########################## PLAIN TEXT #########################
@app.route('/signup/v1', methods={'POST'})
#criar a tabela e usuario de acesso ao Banco
def signup_v1():
    #criando o console e o cursor que vai realizar as tarefas no bd
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    #criando a tabela 
    c.execute('''CREATE TABLE IF NOT EXISTS USER_PLAIN
            (USERNAME TEXT PRIMARY KEY NOT NULL,
             PASSWORD TEXT NOT NULL); ''')
    conn.commit()
    try:
    #inserindo o usuario na tabela
        c.execute("INSERT INTO USER_PLAIN (USERNAME, PASSWORD)"
                    "VALUES ('{0}', '{1}')".format(request.form['username'],
request.form['password']))
        conn.commit()
    #retornando se o foi bem sucedido o login e o registro do usuario
    except sqlite3.IntegrityError:
        return "username has been registered."
    print('username: ', request.form['username'], 'password: ',
request.form['password'])
    return "signup sucess"


#verificar as novas credenciais da conta
def verify_plain(username, password):
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    #query que seleciona a senha da tabela conforme o username explicitado
    query = "SELECT PASSWORD FROM USER_PLAIN WHERE USERNAME = '{0}' ".format(username)
    c.execute(query)
    records= c.fetchone()
    conn.close()
    if not records:
        return False
    return records[0] == password

#verificar a conta e se o login for bem sucedido retornara uma mensagem
#caso ao contrario o usuario vera uma mensagem de nome de user/senha invalida

@app.route('/login/v1', methods=['GET', 'POST'])
def login_v1():
    error = None
    if request.method == 'POST':
        if verify_plain(request.form['username'], request.form['password']):
            error = 'login sucess'
        else:
            error = 'Invalid username/password'
    else:
        error = 'Invalid method'
    return error
#########################!!!!!!!!!!PASSWORD HASHING #######################
@app.route('/signup/v2', methods={'POST'})
#criar a tabela e usuario de acesso ao Banco
def signup_v2():
    #criando o console e o cursor que vai realizar as tarefas no bd
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    #criando a tabela 
    c.execute('''CREATE TABLE IF NOT EXISTS USER_HASH
            (USERNAME TEXT PRIMARY KEY NOT NULL,
             HASH TEXT NOT NULL); ''')
    conn.commit()
    try:
    #inserindo o usuario na tabela
        hash_value = hashlib.sha256(request.form['password'].encode()).hexdigest()
        c.execute("INSERT INTO USER_HASH (USERNAME, HASH)"
                    "VALUES ('{0}', '{1}')".format(request.form['username'],
hash_value))
        conn.commit()
    #retornando se o foi bem sucedido o login e o registro do usuario
    except sqlite3.IntegrityError:
        return "username has been registered."
    print('username: ', request.form['username'], 'password: ',
request.form['password'], 'hash: ', hash_value)
    return "signup sucess"


#verificar as novas credenciais da conta
def verify_hash(username, password):
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    #query que seleciona a senha da tabela conforme o username explicitado
    query = "SELECT HASH FROM USER_HASH WHERE USERNAME = '{0}' ".format(username)
    c.execute(query)
    records= c.fetchone()
    conn.close()
    if not records:
        return False
    return records[0] == hashlib.sha256(password.encode()).hexdigest()


#verificar a conta e se o login for bem sucedido retornara uma mensagem
#caso ao contrario o usuario vera uma mensagem de nome de user/senha invalida

@app.route('/login/v2', methods=['GET', 'POST'])
def login_v2():
    error = None
    if request.method == 'POST':
        if verify_hash(request.form['username'], request.form['password']):
            error = 'login sucess'
        else:
            error = 'Invalid username/password'
    else:
        error = 'Invalid method'
    return error

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, ssl_context='adhoc')
