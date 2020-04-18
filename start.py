from flask import Flask, render_template, redirect, url_for, request
import sqlite3
import os
import threading
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
image_ind = 0
web_image_ind = 0

if os.path.isfile('table.db'):
    conn = sqlite3.connect('table.db', check_same_thread=False)
    cur = conn.cursor()
else:
    conn = sqlite3.connect('table.db')
    cur = conn.cursor()
    cur.execute('''create table images_await(links TEXT, theme TEXT)''')
    cur.execute('''create table images_queue(links TEXT, theme TEXT)''')
    cur.execute('''create table users(login TEXT, password TEXT)''')
conn.commit()


def get_image():
    global image_ind
    post = None
    while post is None:
        cur.execute('''SELECT * FROM images_await WHERE ROWID = ?''', (image_ind,))
        post = cur.fetchone()
        if post is None:
            image_ind += 1
    return post


#                                       LOGIN HERE
# ********************************************************************************************************
@app.route('/')
def start():
    return redirect(url_for('log_page'))


@app.route('/login')
def log_page():
    return render_template('login_page.html', bad_login=False)


@app.route('/login_user', methods=['POST', 'GET'])
def login_user():
    login = request.form['login']
    password = request.form['password']
    cur.execute("select * from users")
    all_items = cur.fetchall()
    for item in all_items:
        db_login = item[0]
        db_pass = item[1]
        if db_pass == password and db_login == login:
            conn.commit()
            return redirect(url_for('main_page'))
    conn.commit()
    return render_template('login_page.html', bad_login=True)


@app.route('/register_user', methods=['POST'])
def register_user():
    login = request.form['login']
    password = request.form['password']

    ap = '''insert into users values(?,?)'''
    cur.execute(ap, (login, password))
    conn.commit()

    return redirect(url_for('main_page'))

#                                       MAIN_PAGE HERE
# ********************************************************************************************************


@app.route('/main_page', methods=['POST', 'GET'])
def main_page():
    global web_image_ind
    cur.execute('''SELECT COUNT(links) FROM images_await''')
    links_await = cur.fetchone()
    if links_await is None:
        links_await = 0
    else:
        links_await = links_await[0]
    conn.commit()

    cur.execute('''SELECT COUNT(links) FROM images_queue''')
    links_queue = cur.fetchone()
    if links_queue is None:
        links_queue = 0
    else:
        links_queue = links_queue[0]
    conn.commit()

    cur.execute('''SELECT links FROM images_await''')
    images_to_show = cur.fetchall()
    if images_to_show == []:
        image_to_show = ["https://www.salonlfc.com/wp-content/uploads/2018/01/image-not-found-scaled-1150x647.png"]
    else:
        image_to_show = images_to_show[0][0]
        print(image_to_show)
        image_to_show = image_to_show.strip().split(' ')

    conn.commit()

    return render_template('main_page.html', image_to_show=image_to_show[web_image_ind], links_await=links_await, links_queue=links_queue)


@app.route('/accept_image', methods=['POST'])
def accept_image():
    global web_image_ind
    global image_ind
    web_image_ind = 0
    post = None
    while post is None:
        cur.execute('''SELECT * FROM images_await WHERE ROWID = ?''', (image_ind, ))
        post = cur.fetchone()
        if post is None:
            image_ind += 1

    ap = '''insert into images_queue values(?,?)'''
    cur.execute(ap, (post[0], post[1]))
    cur.execute('''DELETE FROM images_await WHERE ROWID = ?''', (image_ind, ))
    conn.commit()
    return redirect(url_for('main_page'))


@app.route('/decline_image', methods=['POST'])
def decline_image():
    global web_image_ind
    web_image_ind = 0
    post = None
    global image_ind
    while post is None:
        cur.execute('''SELECT * FROM images_await WHERE ROWID = ?''', (image_ind, ))
        post = cur.fetchone()
        if post is None:
            image_ind += 1
    cur.execute('''DELETE FROM images_await WHERE ROWID = ?''', (image_ind, ))
    conn.commit()
    return redirect(url_for('main_page'))


@app.route('/next_image', methods=['POST'])
def next_image():
    global web_image_ind

    image_to_show = get_image()
    image_to_show = image_to_show[0].strip().split(' ')
    if web_image_ind != len(image_to_show)-1:
        web_image_ind += 1
    return redirect(url_for('main_page'))


@app.route('/previous_image', methods=['POST'])
def previous_image():
    global web_image_ind
    if web_image_ind != 0:
        web_image_ind -= 1

    return redirect(url_for('main_page'))


