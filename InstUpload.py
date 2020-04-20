from selenium import webdriver
import traceback
from time import sleep
import time
import sqlite3
import requests
from threading import Timer
from options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from PIL import Image


def expand_to_square(file_path: str, fill_color=(255, 255, 255)) -> None:
    """
    увеличивает изображение по адресу 'file_path' до размеров квадрата.
    Пустое пространство заполняется цветом 'fill_color'.
    """
    im = Image.open(file_path)
    size = im.size
    long_side = max(size)

    new_im = Image.new('RGB', (long_side, long_side), fill_color)
    new_im.paste(im, ((long_side - size[0]) // 2, (long_side - size[1]) // 2))

    new_im.save(file_path.split('//')[-1])


def inst_login(login, password, driver):
    try:
        driver.get('https://www.facebook.com/')
        sleep(5)
        driver.find_element_by_xpath("//input[@type=\"email\"]").send_keys(login)
        driver.find_element_by_xpath("//input[@type=\"password\"]").send_keys(password)
        driver.find_element_by_xpath("//input[@type=\"submit\"]").click()
        sleep(5)

    except:
        print(traceback.format_exc())


def inst_upload(theme, img_links, driver):
    options_class = Options()
    hashtags = options_class.description_create(theme)
    
    theme = int(theme)
    sleep(2)

    if len(img_links) != 0:
        for kek in range(len(img_links)):
            while True:
                try:
                    resp = requests.get((img_links[kek]), stream=True).content
                    out = open("images/"+options_class.group_names[theme] + str(kek)+".jpg", "wb")
                    out.write(resp)
                    out.close()
                    # wait = WebDriverWait(driver, 60)
                    # wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type=\"file\"]")))
                    expand_to_square("C:/Users/123/Desktop/Flask/ekzflask/Python-VKtoINST-Bot — копия/images/"+options_class.group_names[theme] + str(kek)+".jpg")
                    break
                except:
                    print(traceback.format_exc())
                    sleep(30)
                    # driver = webdriver.Chrome()
                    # inst_login("+79207921760", "bagira2001", driver)
                
    # actions = webdriver.ActionChains(driver)
    # actions.move_to_element(driver.find_element_by_xpath("//div[@id=\"photo\"]")).click().send_keys(
    #     "C:/Users/123/Desktop/someones_draw/" + group_name + str(index) + "/img" + str(0) + ".jpg").perform()
    # sleep(2)
    # driver.find_element_by_xpath("//a[@class=\"button button-cta primary-btn rounded raised\"]").click()
    driver.get(options_class.groups[theme])
    wait = WebDriverWait(driver, 60)
    wait.until(EC.presence_of_element_located((By.XPATH, "//a[@type=\"button\"]")))
 
    driver.find_element_by_xpath("//a[@type=\"button\"]").click()
    sleep(3)
    driver.find_element_by_xpath("//li[@role=\"menuitem\"]/div").click()
    sleep(5)
    amount_of_divs = len(driver.find_elements_by_xpath("//div[contains(text(), '"+options_class.group_names[theme]+"')]"))
    driver.find_elements_by_xpath("//div[contains(text(), '"+options_class.group_names[theme]+"')]")[amount_of_divs-1].click()
    sleep(3)

    driver.find_element_by_class_name("notranslate").send_keys(hashtags)
    sleep(2)

    if len(img_links) != 0:
        for k in range(len(img_links)):
            print(len(driver.find_elements_by_xpath("//div[@aria-haspopup=\"true\"]")))
            driver.find_elements_by_xpath("//div[@aria-haspopup=\"true\"]")[1].click()
            sleep(3)
            driver.find_element_by_xpath("//input[@type=\"file\"]").send_keys(
                "C:/Users/123/Desktop/Flask/ekzflask/Python-VKtoINST-Bot — копия/images/"+options_class.group_names[theme] + str(k)+".jpg")
            sleep(3)

        sleep(3)

        driver.find_element_by_xpath("//*[@id=\"creator_studio_sliding_tray_root\"]/div/div/div[3]/div[2]/button").click()


def posting(driver, theme, img_ind):
    conn = sqlite3.connect('table.db', check_same_thread=False)
    cur = conn.cursor()
    conn.commit()
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
        cur.execute('''DELETE FROM images_queue WHERE ROWID = ?''', (img_ind,))
        conn.commit()
        print("posted!")
        return True


pause_themes = []


def timer(theme):
    global main_ind
    main_ind = stopped_ind[theme-1]

    pause_themes.remove(theme)

def init(sleep_time):
    # ua = dict(DesiredCapabilities.CHROME)
    # options = webdriver.ChromeOptions()
    # #options.add_argument('headless')
    # options.add_argument('window-size=1600x1000')
    driver = webdriver.Chrome()
    conn = sqlite3.connect('table.db', check_same_thread=False)
    cur = conn.cursor()
    conn.commit()
    inst_login("", "", driver)
    options_class = Options()
    themes_amount = len(options_class.groups)
    global main_ind
    global stopped_ind
    main_ind = 0
    stopped_ind = [0]*themes_amount

    while True:
        cur.execute('''SELECT * FROM images_queue WHERE ROWID = ?''', (main_ind,))
        post = cur.fetchone()
        if post is not None and int(post[1]) not in pause_themes:
            theme = int(post[1])
            print(str(theme)+"     -     theme")

            if posting(driver, theme, main_ind) == True:
                pause_themes.append(theme)
                t = Timer(sleep_time, timer, args=[theme])
                t.start()

            if post[1] in pause_themes:
                stopped_ind[post[1]-1] = main_ind

        main_ind += 1
        sleep(0.5)






