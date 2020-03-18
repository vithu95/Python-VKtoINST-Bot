from tkinter import *
import requests
from PIL import Image, ImageTk
from functools import partial


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
    try:
        checked_queue.append(posting_queue[0])
        posting_queue.popleft()
        print(checked_queue)
        index = 0
    except:
        print("Ошибка")


def decline(posting_queue):
    try:
        posting_queue.popleft()
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
    window = Tk()
    window.title("Добро пожаловать в приложение POD-505")
    canvas = Canvas(height=650, width=1300)
    canvas.grid(column=0, row=0, columnspan=8)

    label_posts = Label()
    label_posts.grid(column=1, row=2)

    btn_accept = Button(window, text="Принять", bg="lightgray", fg="green",
                        command=partial(accept, checked_queue, posting_queue), height=5, width=10)
    btn_accept.grid(column=1, row=1)

    btn_decline = Button(window, text="Отклонить", bg="lightgray", fg="red",
                         command=partial(decline, posting_queue), height=5, width=10)
    btn_decline.grid(column=7, row=1)

    btn_next = Button(window, text="Следующая картинка", bg="lightgray", fg="blue", command=partial(next, posting_queue), height=5, width=20)
    btn_next.grid(column=3, row=1)
    btn_previous = Button(window, text="Предыдущая картинка", bg="lightgray", fg="blue", command=previous, height=5, width=20)
    btn_previous.grid(column=5, row=1)
    img = None  # initially only need a canvas image place-holder
    image_id = canvas.create_image(500, 300, image=img)
    tk_img = None

    canvas.after(1000, refresh_image, posting_queue, canvas, image_id, label_posts, img, tk_img)

    window.mainloop()


index = 0
