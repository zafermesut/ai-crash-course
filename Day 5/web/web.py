from flask import Flask, render_template, request, redirect, url_for

import mysql.connector


app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user='root',
    password='',
    database='yapay_zeka'
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/kayitol', methods=['POST'])
def kayitol():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        cursor = db.cursor()
        cursor.execute('INSERT INTO users (username, email, password) VALUES (%s, %s, %s)', (username, email, password))
        db.commit()
        return render_template('index.html')
    


#update user
cursor = db.cursor()
name = "mesut"
email = "mesut@bilen.dev"
password = "12345678"
user_id = 1

cursor.execute('UPDATE users SET username = %s, email = %s, password = %s WHERE id = %s', (name, email, password, user_id))
db.commit()

#delete user
cursor = db.cursor()
cursor.execute('DELETE FROM users WHERE id = %s', (user_id,))
db.commit()
db.close()

    

if __name__ == '__main__':
    app.run(debug=True)