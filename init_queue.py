import PostCreator_queue
import InstUpload
import acceptPost
import threading
from time import sleep
from collections import deque
from tkinter import *
from functools import partial
posting_queue = deque()
checked_queue = deque()
activated_groups = []


def worker(jojo, ind):
    global posting_queue
    PostCreator_queue.InstaBot(jojo, posting_queue[ind])


def posting(theme, ind):
    print(theme)
    global checked_queue
    InstUpload.init(checked_queue[ind], theme)


def post_checking():
    global posting_queue
    global checked_queue
    acceptPost.init(posting_queue, checked_queue)


def submit(groups):
    global checked_queue
    global posting_queue
    vars = [var1.get(), var2.get()]
    for j in range(len(vars)):
        posting_queue.append([])
        checked_queue.append([])
        if vars[j] != 0:
            activated_groups.append(groups[vars[j]])

    for i in range(len(activated_groups)):

        if var.get() == 0:

            checked_queue[i] = posting_queue[i]

            t = threading.Thread(target=worker, args=(activated_groups[i], i,))  # jojo - 1  art - 2
            t.start()

            t = threading.Thread(target=posting, args=(i+1, i,))  # jojo - 1  art - 2
            t.start()
        elif var.get() == 1:

            t = threading.Thread(target=worker, args=(activated_groups[i], i,))  # jojo - 1  art - 2
            t.start()


            t = threading.Thread(target=posting, args=(i+1, i,))  # jojo - 1  art - 2
            t.start()
        sleep(5)
    window.destroy()

    if var.get() == 1:
        t = threading.Thread(target=post_checking, args=())  # jojo - 1  art - 2
        t.start()



window = Tk()
window.title("Добро пожаловать в приложение POD-505")
var = IntVar()
var.set(1)
var1 = IntVar()
var1.set(1)
var2 = IntVar()
var2.set(0)
r1 = Radiobutton(text='Без проверки', width=10, height=5, indicatoron=0, variable=var, value=0)
r1.grid(column=0, row=0)
r2 = Radiobutton(text='С проверкой', width=10, height=5, indicatoron=0, variable=var, value=1)
r2.grid(column=2, row=0)
c1 = Checkbutton(window, text='jojo', variable=var1, onvalue=1, offvalue=0)
c1.grid(column=0, row=1)
c2 = Checkbutton(window, text='art', variable=var2, onvalue=2, offvalue=0)
c2.grid(column=2, row=1)
jojo_groups = ("https://vk.com/standmemesunset https://vk.com/donut_heaven https://vk.com/iwatchjojo https://vk.com/public192447952 https://vk.com/club189404923 https://vk.com/club191279552 https://vk.com/stroheim_club https://vk.com/dioizm https://vk.com/jojofandom https://vk.com/bruhno_survived https://vk.com/polnobruh https://vk.com/public191711585 https://vk.com/jojobrazzers https://vk.com/lyajojo https://vk.com/somejojoshit https://vk.com/ordenpizdeca https://vk.com/po4kajotaro https://vk.com/fugomemes https://vk.com/memingqueen https://vk.com/madeinmorioh https://vk.com/jojosfunnyadventure https://vk.com/diobasement https://vk.com/za0warudo").strip().split(" ")
art_groups = ("https://vk.com/panda.cafe https://vk.com/acidillustrate https://vk.com/deti_lilith https://vk.com/red_lion_art https://vk.com/publicmoodart https://vk.com/just_art1 https://vk.com/art_of_depressive https://vk.com/art_of_depressive https://vk.com/pixel.arts https://vk.com/love_art_house").strip().split(" ")
groups = {
    1: jojo_groups,
    2: art_groups
}

submitBut = Button(text='Принять', width=20, height=10, command=partial(submit, groups))
submitBut.grid(column=0, row=2, columnspan=3)

window.mainloop()




print("\nAll Threads are queued, let's see when they finish!")

#https://vk.com/standmemesunset https://vk.com/donut_heaven https://vk.com/iwatchjojo https://vk.com/public192447952 https://vk.com/club189404923 https://vk.com/club191279552 https://vk.com/stroheim_club https://vk.com/dioizm https://vk.com/jojofandom https://vk.com/bruhno_survived https://vk.com/polnobruh https://vk.com/public191711585 https://vk.com/jojobrazzers https://vk.com/lyajojo https://vk.com/somejojoshit https://vk.com/ordenpizdeca https://vk.com/po4kajotaro https://vk.com/fugomemes https://vk.com/memingqueen https://vk.com/madeinmorioh https://vk.com/jojosfunnyadventure https://vk.com/diobasement https://vk.com/za0warudo
#https://vk.com/panda.cafe  https://vk.com/acidillustrate https://vk.com/deti_lilith https://vk.com/red_lion_art https://vk.com/publicmoodart https://vk.com/just_art1 https://vk.com/art_of_depressive https://vk.com/art_of_depressive https://vk.com/pixel.arts https://vk.com/love_art_house
