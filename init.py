
import vk_stealer
import instUpload
import threading
import acceptPost
from collections import deque

posting_queue = deque()
checked_queue = deque()


def vkontakte_stealer(jojo, ind):
    global posting_queue
    vk_stealer.InstaBot(jojo, posting_queue[ind])


def posting(theme, sleep_time):
    print(theme)
    global checked_queue
    instUpload.init(theme, sleep_time)


def post_checking(theme):
    global posting_queue
    acceptPost.init(posting_queue, theme)


def submit(groups, sleep_time):
    global checked_queue
    global posting_queue
    for i in range(len(groups)):
        posting_queue.append([])
        checked_queue.append([])
        if groups[i+1][0].find("https://vk.com/") != -1:

            t = threading.Thread(target=vkontakte_stealer, args=(groups[i+1], i,))  # jojo - 1  art - 2
            t.start()
        if groups[i+1][0].find("https://twitter.com/") != -1:

            t = threading.Thread(target=twitter_stealer, args=(groups[i+1], i,))  # jojo - 1  art - 2
            t.start()

        t = threading.Thread(target=post_checking, args=(i,))  # jojo - 1  art - 2
        t.start()

        # t = threading.Thread(target=posting, args=(i+1, sleep_time))  # jojo - 1  art - 2
        # t.start()


def init():
    vk_jojo_groups = (
        "https://vk.com/standmemesunset https://vk.com/donut_heaven https://vk.com/iwatchjojo https://vk.com/public192447952 https://vk.com/club189404923 https://vk.com/club191279552 https://vk.com/stroheim_club https://vk.com/dioizm https://vk.com/jojofandom https://vk.com/bruhno_survived https://vk.com/polnobruh https://vk.com/public191711585 https://vk.com/jojobrazzers https://vk.com/lyajojo https://vk.com/somejojoshit https://vk.com/ordenpizdeca https://vk.com/po4kajotaro https://vk.com/fugomemes https://vk.com/memingqueen https://vk.com/madeinmorioh https://vk.com/jojosfunnyadventure https://vk.com/diobasement https://vk.com/za0warudo").strip().split(
        " ")
    twitter_news_groups = (
        "https://twitter.com/VRSoloviev https://twitter.com/pidarasinaaa https://twitter.com/oldLentach https://twitter.com/lentaruofficial https://twitter.com/tvrain https://twitter.com/navalny https://twitter.com/aavst https://twitter.com/EchoMskRu https://twitter.com/bbcrussian https://twitter.com/SvobodaRadio").strip().split(
        " ")
    groups = {
        1: vk_jojo_groups,
        2: twitter_news_groups
    }
    submit(groups, 1500)


init()
print("\nAll Threads are queued, let's see when they finish!")
