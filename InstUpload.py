from selenium import webdriver
import traceback
from time import sleep
import time
import random
import sqlite3
import requests


def inst_login(login, password, driver):
    try:
        driver.get('https://www.facebook.com/')
        sleep(5)
        driver.find_element_by_xpath("//input[@type=\"email\"]").send_keys(login)
        driver.find_element_by_xpath("//input[@type=\"password\"]").send_keys(password)
        driver.find_element_by_xpath("//input[@type=\"submit\"]").click()
        sleep(5)
        try:
            driver.get("https://www.kapwing.com/tools/resize-video")
            sleep(1)
            driver.find_element_by_xpath("//div[contains(text(), 'Sign In')]").click()
            sleep(2)
            driver.find_element_by_class_name("sign-in-dialog-facebook-button").click()
            sleep(4)
        except:
            print(traceback.format_exc())
            return 0
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
        1: "\n\n\n\n Подписочку! \n\n\n\n",
        2: "|\n|\n Подписывайся на @acid.illustrate \n|\n|\n"
    }

    groups = {
        1: "https://business.facebook.com/creatorstudio?tab=instagram_content_posts&mode=instagram&collection_id=all_pages&content_table=INSTAGRAM_POSTS",
        2: "https://postingram.ru/account/42346/"
    }

    print(theme)
    sleep(2)

    text_file_prim = themes_primary[theme].split(" ")
    text_file_sec = themes_secondary[theme].split(" ")

    hashtags = text_file_prim + (random.sample(text_file_sec, len(text_file_sec) // 2))
    random.shuffle(hashtags)
    hashtags = " ".join(hashtags)
    hashtags = invitation[theme] + hashtags

    if len(img_links) != 0:
        for kek in range(len(img_links)):
            try:
                resp = requests.get((img_links[kek]), stream=True).content
                out = open("images\img"+str(kek)+".jpg", "wb")
                out.write(resp)
                out.close()
                driver.get("https://www.kapwing.com/tools/resize-video")
                sleep(3)
                driver.find_element_by_xpath("//input[@type=\"file\"]").send_keys("C:/Users/123/Desktop/Flask/ekzflask/Python-VKtoINST-Bot — копия/images/img"+str(kek)+".jpg")
                sleep(20)
                driver.find_element_by_class_name("create-button").click()
                sleep(40)
                img_links[kek] = driver.find_element_by_xpath("//img[@alt=\"Final\"]").get_attribute("src")
                resp = requests.get((img_links[kek]), stream=True).content
                out = open("images\img" + str(kek) + ".jpg", "wb")
                out.write(resp)
                out.close()
            except:
                continue
    # actions = webdriver.ActionChains(driver)
    # actions.move_to_element(driver.find_element_by_xpath("//div[@id=\"photo\"]")).click().send_keys(
    #     "C:/Users/123/Desktop/someones_draw/" + group_name + str(index) + "/img" + str(0) + ".jpg").perform()
    # sleep(2)
    # driver.find_element_by_xpath("//a[@class=\"button button-cta primary-btn rounded raised\"]").click()
    driver.get(groups[theme])
    driver.find_element_by_xpath("//a[@type=\"button\"]").click()
    sleep(3)
    driver.find_element_by_xpath("//li[@role=\"menuitem\"]/div").click()
    sleep(5)
    amount_of_divs = len(driver.find_elements_by_xpath("//div[contains(text(), 'overdrive_retro')]"))
    driver.find_elements_by_xpath("//div[contains(text(), 'overdrive_retro')]")[amount_of_divs-1].click()
    sleep(3)

    driver.find_element_by_class_name("notranslate").send_keys(hashtags)
    sleep(2)

    if len(img_links) != 0:
        for k in range(len(img_links)):
            print(len(driver.find_elements_by_xpath("//div[@aria-haspopup=\"true\"]")))
            driver.find_elements_by_xpath("//div[@aria-haspopup=\"true\"]")[1].click()
            sleep(3)
            driver.find_element_by_xpath("//input[@type=\"file\"]").send_keys("C:/Users/123/Desktop/Flask/ekzflask/Python-VKtoINST-Bot — копия/images/img"+str(k)+".jpg")
            sleep(3)

        sleep(1)
        # driver.find_elements_by_xpath("//input[@name=\"Post[enable_first_comment]\"]")[1].click()
        # sleep(2)
        # driver.find_elements_by_xpath("//div[@class=\"emojionearea-editor emojionearea-editor_padding-bottom\"]")[1].send_keys(hashtags)
        print(len(driver.find_elements_by_xpath("//button[@aria-disabled=\"false\"]")))

        driver.find_elements_by_xpath("//button[@aria-disabled=\"false\"]")[13].click()



def init(theme, sleep_time):
    # ua = dict(DesiredCapabilities.CHROME)
    # options = webdriver.ChromeOptions()
    # #options.add_argument('headless')
    # options.add_argument('window-size=1600x1000')
    driver = webdriver.Chrome()

    inst_login("FBlogin", "FBpassword", driver)
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
            links = post[0].strip().split(" ")
            print(str(len(links)) + " -- links amount")
            print(time.ctime(time.time()))
            while True:
                try:
                    inst_upload(theme, links, driver)
                    break
                except:
                    print(traceback.format_exc())
                    return -1
            cur.execute('''DELETE FROM images_queue WHERE ROWID = ?''', (img_ind,))
            conn.commit()
            print("posted!")
            sleep(sleep_time-120)

        img_ind += 1


