import PostCreator_queue
import InstUpload
import acceptPost
import threading
from collections import deque

posting_queue = deque()
checked_queue = deque()
activated_groups = []


def worker(jojo, ind):
    global posting_queue
    PostCreator_queue.InstaBot(jojo, posting_queue[ind])


def posting(theme, ind, sleep_time):
    print(theme)
    global checked_queue
    InstUpload.init(theme, sleep_time)


def post_checking():
    global posting_queue
    acceptPost.init(posting_queue[0])


def submit(groups, sleep_time):
    global checked_queue
    global posting_queue

    posting_queue.append([])
    checked_queue.append([])

    activated_groups.append(groups)

    t = threading.Thread(target=worker, args=(activated_groups[0], 0, ))  # jojo - 1  art - 2
    t.start()

    t = threading.Thread(target=posting, args=(1, 0, sleep_time))  # jojo - 1  art - 2
    t.start()

    t = threading.Thread(target=post_checking, args=())  # jojo - 1  art - 2
    t.start()


def init():
    jojo_groups = (
        "https://vk.com/standmemesunset https://vk.com/donut_heaven https://vk.com/iwatchjojo https://vk.com/public192447952 https://vk.com/club189404923 https://vk.com/club191279552 https://vk.com/stroheim_club https://vk.com/dioizm https://vk.com/jojofandom https://vk.com/bruhno_survived https://vk.com/polnobruh https://vk.com/public191711585 https://vk.com/jojobrazzers https://vk.com/lyajojo https://vk.com/somejojoshit https://vk.com/ordenpizdeca https://vk.com/po4kajotaro https://vk.com/fugomemes https://vk.com/memingqueen https://vk.com/madeinmorioh https://vk.com/jojosfunnyadventure https://vk.com/diobasement https://vk.com/za0warudo").strip().split(
        " ")
    art_groups = (
        "https://vk.com/panda.cafe https://vk.com/acidillustrate https://vk.com/deti_lilith https://vk.com/red_lion_art https://vk.com/publicmoodart https://vk.com/just_art1 https://vk.com/art_of_depressive https://vk.com/art_of_depressive https://vk.com/pixel.arts https://vk.com/love_art_house").strip().split(
        " ")
    groups = {
        1: jojo_groups,
        2: art_groups
    }
    submit(jojo_groups, 1800)
init()
print("\nAll Threads are queued, let's see when they finish!")

#https://vk.com/standmemesunset https://vk.com/donut_heaven https://vk.com/iwatchjojo https://vk.com/public192447952 https://vk.com/club189404923 https://vk.com/club191279552 https://vk.com/stroheim_club https://vk.com/dioizm https://vk.com/jojofandom https://vk.com/bruhno_survived https://vk.com/polnobruh https://vk.com/public191711585 https://vk.com/jojobrazzers https://vk.com/lyajojo https://vk.com/somejojoshit https://vk.com/ordenpizdeca https://vk.com/po4kajotaro https://vk.com/fugomemes https://vk.com/memingqueen https://vk.com/madeinmorioh https://vk.com/jojosfunnyadventure https://vk.com/diobasement https://vk.com/za0warudo
#https://vk.com/panda.cafe  https://vk.com/acidillustrate https://vk.com/deti_lilith https://vk.com/red_lion_art https://vk.com/publicmoodart https://vk.com/just_art1 https://vk.com/art_of_depressive https://vk.com/art_of_depressive https://vk.com/pixel.arts https://vk.com/love_art_house
