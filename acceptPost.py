from tkinter import *
import requests
from PIL import Image, ImageTk
from functools import partial
from tkinter import ttk


def next(posting_queue):
    global index
    try:
        if index < len(posting_queue[0]):
            index += 1
    except:
        print("Ошибка")


def previous():
    global index
    if index != 0:
        index -= 1


def accept(checked_queue, posting_queue):
    global index
    print(posting_queue)
    print(checked_queue)
    try:
        checked_queue.append(posting_queue[0])
        del posting_queue[0]
        print(checked_queue)
        index = 0
    except:
        print("Ошибка")


def decline(posting_queue):
    try:
        del posting_queue[0]
        print("not cringe")

    except:
        print("Ошибка")


def refresh_image(posting_queue, canvas, image_id, label_posts, img=None, tk_img=None):
    global index
    try:
        resp = requests.get(posting_queue[0][index], stream=True).raw
        img = Image.open(resp)
        width, height = img.size
        if width or height > 500:
            size = (width // 2, height // 2)
        else:
            size = (width, height)
        img = img.resize(size)
        tk_img = ImageTk.PhotoImage(img)
        canvas.itemconfigure(image_id, image=tk_img)

        amount_of_posts = len(posting_queue)
        label_posts["text"] = amount_of_posts
    except:
        img = None
    canvas.after(1000, refresh_image, posting_queue, canvas, image_id, label_posts, img, tk_img)


def init(posting_queue, checked_queue):
    global index
    index = 0
    window = Tk()
    window.title("Добро пожаловать в приложение POD-505")
    tab_control = ttk.Notebook(window)
    tab1 = ttk.Frame(tab_control)
    tab_control.add(tab1, text='Первая')
    tab_control.pack(expand=1, fill='both')

    tab2 = ttk.Frame(tab_control)
    tab_control.add(tab2, text='Вторая')
    tab_control.pack(expand=1, fill='both')

    canvas = Canvas(tab1, height=650, width=1300)
    canvas.grid(column=0, row=0, columnspan=8)

    label_posts = Label(tab1)
    label_posts.grid(column=1, row=2)

    btn_accept = Button(tab1, text="Принять", bg="lightgray", fg="green",
                        command=partial(accept, checked_queue[0], posting_queue[0]), height=5, width=10)
    btn_accept.grid(column=1, row=1)

    btn_decline = Button(tab1, text="Отклонить", bg="lightgray", fg="red",
                         command=partial(decline, posting_queue[0]), height=5, width=10)
    btn_decline.grid(column=7, row=1)

    btn_next = Button(tab1, text="Следующая картинка", bg="lightgray", fg="blue", command=partial(next, posting_queue[0]), height=5, width=20)
    btn_next.grid(column=3, row=1)
    btn_previous = Button(tab1, text="Предыдущая картинка", bg="lightgray", fg="blue", command=previous, height=5, width=20)
    btn_previous.grid(column=5, row=1)
    img = None  # initially only need a canvas image place-holder
    image_id = canvas.create_image(500, 300, image=img)
    tk_img = None

    canvas.after(1000, refresh_image, posting_queue[0], canvas, image_id, label_posts, img, tk_img)
    #cringe
    canvas2 = Canvas(tab2, height=650, width=1300)
    canvas2.grid(column=0, row=0, columnspan=8)

    label_posts2 = Label(tab2)
    label_posts2.grid(column=1, row=2)

    btn_accept2 = Button(tab2, text="Принять", bg="lightgray", fg="green",
                        command=partial(accept, checked_queue[1], posting_queue[1]), height=5, width=10)
    btn_accept2.grid(column=1, row=1)

    btn_decline2 = Button(tab2, text="Отклонить", bg="lightgray", fg="red",
                         command=partial(decline, posting_queue[1]), height=5, width=10)
    btn_decline2.grid(column=7, row=1)

    btn_next2 = Button(tab2, text="Следующая картинка", bg="lightgray", fg="blue",
                      command=partial(next, posting_queue[1]), height=5, width=20)
    btn_next2.grid(column=3, row=1)
    btn_previous2 = Button(tab2, text="Предыдущая картинка", bg="lightgray", fg="blue", command=previous, height=5,
                          width=20)
    btn_previous2.grid(column=5, row=1)
    img2 = None  # initially only need a canvas image place-holder
    image_id2 = canvas2.create_image(500, 300, image=img)
    tk_img2 = None

    canvas2.after(1000, refresh_image, posting_queue[1], canvas2, image_id2, label_posts2, img2, tk_img2)

    window.mainloop()



