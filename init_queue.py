import PostCreator_queue
import InstUpload
import acceptPost
import threading
from collections import deque
from tkinter import *
posting_queue = deque()
checked_queue = deque()


def worker(jojo):
    global posting_queue
    PostCreator_queue.InstaBot(jojo, posting_queue)


def posting(theme):
    print(theme)
    global checked_queue
    InstUpload.init(checked_queue, theme)


def post_checking():
    global posting_queue
    global checked_queue
    acceptPost.init(posting_queue, checked_queue)


def submit():
    if var.get() == 0:
        window.destroy()
        global checked_queue
        global posting_queue
        checked_queue = posting_queue

        t = threading.Thread(target=worker, args=(jojo_groups,))  # jojo - 1  art - 2
        t.start()

        t = threading.Thread(target=posting, args=(1,))  # jojo - 1  art - 2
        t.start()
    elif var.get() == 1:
        window.destroy()
        t = threading.Thread(target=worker, args=(jojo_groups,))  # jojo - 1  art - 2
        t.start()

        t = threading.Thread(target=post_checking, args=())  # jojo - 1  art - 2
        t.start()

        t = threading.Thread(target=posting, args=(1,))  # jojo - 1  art - 2
        t.start()


window = Tk()
window.title("Добро пожаловать в приложение POD-505")
var = IntVar()
var.set(0)
r1 = Radiobutton(text='Без проверки', width=10, height=1, indicatoron=0, variable=var, value=0)
r1.grid(column=0, row=0)
r2 = Radiobutton(text='С проверкой', width=10, height=1, indicatoron=0, variable=var, value=1)
r2.grid(column=2, row=0)

submitBut = Button(text='Принять', width=20, height=10, command=submit)
submitBut.grid(column=0, row=1, columnspan=3)
jojo_groups = ("https://vk.com/standmemesunset https://vk.com/donut_heaven https://vk.com/iwatchjojo https://vk.com/public192447952 https://vk.com/club189404923 https://vk.com/club191279552 https://vk.com/stroheim_club https://vk.com/dioizm https://vk.com/jojofandom https://vk.com/bruhno_survived https://vk.com/polnobruh https://vk.com/public191711585 https://vk.com/jojobrazzers https://vk.com/lyajojo https://vk.com/somejojoshit https://vk.com/ordenpizdeca https://vk.com/po4kajotaro https://vk.com/fugomemes https://vk.com/memingqueen https://vk.com/madeinmorioh https://vk.com/jojosfunnyadventure https://vk.com/diobasement https://vk.com/za0warudo").strip().split(" ")
window.mainloop()




print("\nAll Threads are queued, let's see when they finish!")

#https://vk.com/standmemesunset https://vk.com/donut_heaven https://vk.com/iwatchjojo https://vk.com/public192447952 https://vk.com/club189404923 https://vk.com/club191279552 https://vk.com/stroheim_club https://vk.com/dioizm https://vk.com/jojofandom https://vk.com/bruhno_survived https://vk.com/polnobruh https://vk.com/public191711585 https://vk.com/jojobrazzers https://vk.com/lyajojo https://vk.com/somejojoshit https://vk.com/ordenpizdeca https://vk.com/po4kajotaro https://vk.com/fugomemes https://vk.com/memingqueen https://vk.com/madeinmorioh https://vk.com/jojosfunnyadventure https://vk.com/diobasement https://vk.com/za0warudo
#https://vk.com/panda.cafe  https://vk.com/acidillustrate
