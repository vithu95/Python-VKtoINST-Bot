
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


def posting(sleep_time):
    instUpload.init(sleep_time)


def post_checking(theme, to_check):
    global posting_queue
    acceptPost.init(posting_queue, theme, to_check)


def submit(checking, groups, sleep_time):
    global checked_queue
    global posting_queue
    for i in range(len(groups)):
        posting_queue.append([])
        checked_queue.append([])
        if groups[i+1][0].find("https://vk.com/") != -1:

            t = threading.Thread(target=vkontakte_stealer, args=(groups[i+1], i,))  # jojo - 1  art - 2
            t.start()

        t = threading.Thread(target=post_checking, args=(i, checking[i+1]))  # jojo - 1  art - 2
        t.start()

    t = threading.Thread(target=posting, args=(sleep_time, ))  # jojo - 1  art - 2
    t.start()


def init():
    vk_jojo_groups = (
        "https://vk.com/standmemesunset https://vk.com/donut_heaven https://vk.com/iwatchjojo https://vk.com/public192447952 https://vk.com/club189404923 https://vk.com/club191279552 https://vk.com/stroheim_club https://vk.com/dioizm https://vk.com/jojofandom https://vk.com/bruhno_survived https://vk.com/polnobruh https://vk.com/public191711585 https://vk.com/jojobrazzers https://vk.com/lyajojo https://vk.com/somejojoshit https://vk.com/ordenpizdeca https://vk.com/po4kajotaro https://vk.com/fugomemes https://vk.com/memingqueen https://vk.com/madeinmorioh https://vk.com/jojosfunnyadventure https://vk.com/diobasement https://vk.com/za0warudo").strip().split(
        " ")
    my_favourite_twitter = (
        "https://vk.com/public184586152 https://vk.com/my_lovely_jam https://vk.com/sunnylittle https://vk.com/yourplant https://vk.com/myolittle https://vk.com/dnthng https://vk.com/soulmatelove https://vk.com/vk.whyy https://vk.com/rainboowrain https://vk.com/avenue24th https://vk.com/hospital_room https://vk.com/whrazb https://vk.com/twi_pub https://vk.com/wtf.twitterr https://vk.com/twittsy https://vk.com/public_tnrs https://vk.com/twittonator https://vk.com/piceveryd https://vk.com/zaanoza https://vk.com/pinkburger https://vk.com/sketch.books").strip().split(
        " ")
    cutie_creamies = (
        "https://vk.com/telochkictatu https://vk.com/otchenashmaso https://vk.com/public122155357 https://vk.com/girls_informal666 https://vk.com/feitnv https://vk.com/unreal4iksibiksi https://vk.com/kisazaika").strip().split(" ")
    groups = {
        1: vk_jojo_groups,
        2: my_favourite_twitter,
        3: cutie_creamies
    }

    checking = {
        1: True,
        2: False,
        3: True
    }
    submit(checking, groups, 1500)


init()
print("\nAll Threads are queued, let's see when they finish!")
