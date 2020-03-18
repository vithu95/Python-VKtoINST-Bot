from selenium import webdriver
from time import sleep
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import traceback


class InstaBot:
    def download_new_post(self, new_post):
        sleep(5)
        new_post = new_post.find_element_by_class_name("wall_text")
        images_in_post = new_post.find_elements_by_class_name("page_post_thumb_wrap")

        img_links_amount = len(images_in_post)
        print(img_links_amount)
        img_links = []
        for i in range(img_links_amount):
            try:
                sleep(2)
                images_in_post[i].click()
                sleep(5)
                img_links.append(self.driver.find_element_by_xpath("//div[@id=\"pv_photo\"]").find_element_by_xpath(
                    "//img").get_attribute('src'))
                while True:
                    try:
                        self.driver.find_element_by_xpath("//div[@class=\"pv_close_btn\"]").click()
                        break
                    except:
                        sleep(1)
                sleep(4)

                print(img_links[i])
            except:
                print(traceback.format_exc())
                try:
                    url = self.driver.current_url()
                    url = url.replace("vk.com", "m.vk.com")
                    self.driver.get(url)
                    sleep(5)
                    video_link = self.driver.find_element_by_xpath("//source[@type=\"video/mp4\"]").get_attribute("src")
                    img_links.append(video_link)
                except:
                    print(traceback.format_exc())

        return img_links

    def check_new_posts(self, all_posts_date, old_posts_date, page_num):

        for i in range(5):
            if old_posts_date[page_num][i] != all_posts_date[i]:
                return i
        return -1

    def posts_date_get(self):
        posts = self.driver.find_elements_by_xpath("//div[@class=\"_post_content\"]")
        posts_date = []
        for i in range(5):
            try:
                posts_date.append(posts[i].find_element_by_class_name("rel_date").get_attribute('abs_time'))
                if posts_date[i] is None:
                    posts_date[i] = posts[i].find_element_by_class_name("rel_date").text
            except:
                print(traceback.format_exc())
                posts_date.append("bug")
        return posts_date

    def __init__(self, groups, posting_queue):

        ua = dict(DesiredCapabilities.CHROME)
        options = webdriver.ChromeOptions()
        #options.add_argument('headless')
        options.add_argument('window-size=1600x1000')
        self.driver = webdriver.Chrome(chrome_options=options)
        groups_amount = len(groups)

        sleep(2)
        group_names = []
        old_posts_date = []

        for group in range(groups_amount):
            self.driver.execute_script("window.open('"+groups[group]+"','_blank');")
            self.driver.switch_to.window(self.driver.window_handles[group+1])
            old_posts_date.append([])
            old_posts_date[group] = self.posts_date_get()
            group_names.append(groups[group].replace("https://vk.com/", ""))
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        sleep(2)
        page_num = 0

        while True:
            answer = -1
            while answer == -1:
                self.driver.refresh()
                sleep(1)
                all_posts_date = self.posts_date_get()
                for index in range(5):
                    if len(all_posts_date) == 0:
                        self.driver.refresh()
                        sleep(5)
                        all_posts_date = self.posts_date_get()
                        if index == 4:
                            exit(105)

                answer = self.check_new_posts(all_posts_date, old_posts_date, page_num)
                if answer == -1:
                    page_num += 1
                else:
                    old_posts_date[page_num].clear()
                    break
                if page_num == groups_amount:
                    page_num = 0

                self.driver.switch_to.window(self.driver.window_handles[page_num])

            posts = self.driver.find_elements_by_xpath("//div[@class=\"_post_content\"]")
            new_post = posts[answer]
            print("  New post!!! " + group_names[page_num])
            while True:
                try:
                    img_links = self.download_new_post(new_post)
                    if (len(img_links)) != 0:
                        posting_queue.append(img_links)
                    break
                except:
                    self.driver.refresh()
                    print("Ошибка в download_new_post")
                    continue
            print(posting_queue)
            self.driver.get(groups[page_num])
            sleep(3)
            old_posts_date[page_num] = self.posts_date_get()



                       # https://vk.com/nrsvl https://vk.com/standmemesunset https://vk.com/donut_heaven
                                            # https://vk.com/panda.cafe https://vk.com/ordenpizdeca https://vk.com/acidillustrate
                                            # https://vk.com/polnobruh

