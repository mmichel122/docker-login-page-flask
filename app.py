from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
import mysql.connector

cnx = mysql.connector.connect(user='login', password='123456', host='172.17.0.2',database='login')
app = Flask(__name__)

@app.route('/')
def home():
        if not session.get('logged_in'):
                return render_template('login.html')
        else:
                return 'Hello Boss!  <a href="/logout">Logout</a>'

@app.route('/login', methods=['GET', 'POST'])
def do_admin_login():
        if request.method == 'POST':
                cursor = cnx.cursor()
                user_name = request.form['username']
                cursor.execute("SELECT password from Users WHERE username = '"+user_name+"'")
                db_user_pass = cursor.fetchone()
                cursor.close()
                if request.form['password'] == db_user_pass[0]:
                        session['logged_in'] = True
                        return home()
                else:
                        flash('wrong password!')
                        return home()
        else:
                return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
        if request.method == 'POST':
                cursor = cnx.cursor()
                user_name = request.form['username']
                pass_word = request.form['password'] 
                add_account = ("INSERT INTO Users(username, password) VALUES('"+user_name+"', "+pass_word+")")
                cursor.execute(add_account)
                cnx.commit()
                flash('Account Registred')
                cursor.close()
                return home()
        else:
                return render_template('register.html')

@app.route("/logout")
def logout():
        session['logged_in'] = False
        return home()

if __name__ == "__main__":
        app.secret_key = os.urandom(12)
        app.run(debug=True,host='0.0.0.0', port=8080)

