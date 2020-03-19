from selenium import webdriver
import traceback
from time import sleep
import time
import random


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
    themes = {
        1: "#jojo #jjba #jojosbizzareadventure #jojokes #jojomemes #joseph #josephmemes #jotaro #jojobizzareadventure #JoJo #JJBAmeme #jjbamemes #JJBAcringe",
        2: "#procreatedrawing #procreateart #digitalillustration #inktober #digitalart #digitalpainting #art #artwork #drawing #draw #sketch #sketchbook #sketching #digitalsketchbook #sketchbooks #artsy #arts #procreate #procreateapp #ipadpro #ipadproart #arttutorial #painting #paint #drawthisinyourstyle #dtiys #sketches #procreatetutorial #wipart",
        3: ""
    }

    groups = {
        1: "https://postingram.ru/account/42309/",
        2: "https://postingram.ru/account/42346/"
    }
    # actions = webdriver.ActionChains(driver)
    # actions.move_to_element(driver.find_element_by_xpath("//div[@id=\"photo\"]")).click().send_keys(
    #     "C:/Users/123/Desktop/someones_draw/" + group_name + str(index) + "/img" + str(0) + ".jpg").perform()
    # sleep(2)
    # driver.find_element_by_xpath("//a[@class=\"button button-cta primary-btn rounded raised\"]").click()
    driver.get(groups[theme])
    print(theme)
    sleep(2)
    text_file = themes[theme].split(" ")
    hashtags = ""
    random.shuffle(text_file)
    for i in range(len(text_file)):
        if random.randint(0, 10) != 10:
            hashtags += text_file[i]
            hashtags += " "


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
        sleep(2)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(2)
        driver.find_element_by_xpath(
            "//div[@class=\"emojionearea-editor emojionearea-editor_padding-bottom\"]").send_keys(hashtags)
        driver.find_element_by_xpath(
            "//a[@class=\"col-xs-12 border-simple-l js-app-submit-and-publish\"]").click()


def init(posting_queue, theme):
    driver = webdriver.Chrome()
    driver.set_window_size(1000, 2000)
    inst_login("tezart@mail.ru", "bagira2001", driver)

    print(str(theme) + " -- theme")
    while True:

        if len(posting_queue) != 0:
            print(str(len(posting_queue[0])) + " -- links")
            print(time.ctime(time.time()))
            while True:
                try:
                    inst_upload(theme, posting_queue[0], driver)
                    break
                except:
                    continue
            print("posted!")
            del posting_queue[0]
            sleep(900)
        else:
            sleep(10)


