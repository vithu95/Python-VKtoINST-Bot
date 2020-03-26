from selenium import webdriver
import traceback
from time import sleep
import time
import random
import sqlite3


def inst_login(login, password, driver):
    try:
        driver.get('https://postingram.ru/user/login/')
        sleep(5)
        driver.find_element_by_id("User_loginLogin").send_keys(login)
        driver.find_element_by_id("User_passwordLogin").send_keys(password)
        driver.find_element_by_xpath("//input[@type=\"submit\"]").click()
        sleep(5)
    except:
        print(traceback.format_exc())
        return 0


def inst_upload(theme, img_links, driver):
    themes_primary = {
        1: "#jojo #jjba #jojosbizzareadventure #jojokes #jojomemes",
        2: "#procreatedrawing #procreateart #digitalillustration ",
        3: ""
    }

    themes_secondary = {
        1: "#joseph #josephmemes #jotaro #jojobizzareadventure #JoJo #JJBAmeme #jjbamemes #JJBAcringe #giorno #джоджо #memes #kakyoin #dio #meme #goldenwind #ventoaureo #giornogiovanna",
        2: "#inktober #digitalart #digitalpainting #art #artwork #drawing #draw #sketch #sketchbook #sketching #digitalsketchbook #sketchbooks #artistsoninstagram #artsy #arts #procreate #procreateapp #ipadpro #ipadproart #arttutorial #painting #paint #drawthisinyourstyle #dtiys #sketches #procreatetutorial #wipart",
        3: ""
    }

    invitation = {
        1: "|\n|\nПодписывайся на @overdrive_retro \n|\n|\n",
        2: "|\n|\nПодписывайся на @acid.illustrate \n|\n|\n"
    }

    groups = {
        1: "https://postingram.ru/account/42309/",
        2: "https://postingram.ru/account/42346/"
    }
    driver.get(groups[theme])
    print(theme)
    sleep(2)

    text_file_prim = themes_primary[theme].split(" ")
    text_file_sec = themes_secondary[theme].split(" ")

    hashtags = text_file_prim + (random.sample(text_file_sec, len(text_file_sec) // 3))
    random.shuffle(hashtags)
    hashtags = " ".join(hashtags)
    hashtags = invitation[theme] + hashtags

    # actions = webdriver.ActionChains(driver)
    # actions.move_to_element(driver.find_element_by_xpath("//div[@id=\"photo\"]")).click().send_keys(
    #     "C:/Users/123/Desktop/someones_draw/" + group_name + str(index) + "/img" + str(0) + ".jpg").perform()
    # sleep(2)
    # driver.find_element_by_xpath("//a[@class=\"button button-cta primary-btn rounded raised\"]").click()

    
    driver.find_element_by_xpath("//a[@href=\"#modalCreatePost\"]").click()
    sleep(2)
    if len(img_links) != 0:

        driver.find_element_by_xpath("//label[@for=\"Post_post_type_8\"]").click()
        for k in range(len(img_links)):
            driver.find_element_by_xpath("//input[@id=\"Post_media_url\"]").send_keys(img_links[k])
            sleep(1)
            driver.find_elements_by_xpath("//button[contains(text(), 'Добавить')]")[2].click()
            sleep(5)
        sleep(1)
        driver.find_element_by_xpath("//a[@href=\"#tabFormalizationPost\"]").click()
        sleep(4)
        # driver.find_elements_by_xpath("//input[@name=\"Post[enable_first_comment]\"]")[1].click()
        # sleep(2)
        # driver.find_elements_by_xpath("//div[@class=\"emojionearea-editor emojionearea-editor_padding-bottom\"]")[1].send_keys(hashtags)
        driver.find_element_by_xpath(
            "//a[@class=\"col-xs-12 border-simple-l js-app-submit-and-publish\"]").click()


def init(theme, sleep_time):
    # ua = dict(DesiredCapabilities.CHROME)
    # options = webdriver.ChromeOptions()
    # #options.add_argument('headless')
    # options.add_argument('window-size=1600x1000')
    driver = webdriver.Chrome()

    inst_login("tezart@mail.ru", "bagira2001", driver)
    conn = sqlite3.connect('table.db', check_same_thread=False)
    cur = conn.cursor()
    conn.commit()
    print(str(theme) + " -- theme")
    img_ind = 0
    post = None
    while post is None:
        cur.execute('''SELECT * FROM images_queue WHERE ROWID = ?''', (img_ind,))
        post = cur.fetchone()
        if post is None:
            img_ind += 1

    print(img_ind)
    while True:
        cur.execute('''SELECT * FROM images_queue WHERE ROWID = ?''', (img_ind, ))
        post = cur.fetchone()
        if post is not None:

            cur.execute('''DELETE FROM images_queue WHERE ROWID = ?''', (img_ind, ))
            conn.commit()

            links = post[0].strip().split(" ")
            print(str(len(links)) + " -- links amount")
            print(time.ctime(time.time()))
            while True:
                try:
                    inst_upload(theme, links, driver)
                    break
                except:
                    continue
            print("posted!")
            sleep(sleep_time)
            img_ind += 1
        else:
            sleep(10)


