import sqlite3
from time import sleep


def init(posting_queue, theme, to_check):
    conn = sqlite3.connect('table.db', check_same_thread=False)
    cur = conn.cursor()
    conn.commit()
    print(posting_queue)
    while True:
        if len(posting_queue[theme]) != 0:
            if to_check is True:
                ap = '''insert into images_await values(?,?)'''
            else:
                ap = '''insert into images_queue values(?,?)'''
            print(posting_queue[theme])
            final_queue = ""
            for i in range(len(posting_queue[theme][0])):
                final_queue += posting_queue[theme][0][i] + " "
            print(final_queue)
            cur.execute(ap, (final_queue, theme+1,))
            conn.commit()
            del posting_queue[theme][0]
        else:
            sleep(2)
