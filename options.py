import random


class Options:
    def __init__(self):
        self.themes_primary = {
            1: "#jojo #jjba #jojosbizzareadventure #jojokes #jojomemes",
            2: "#твиттер #selfcare #твит #тамблер #интересное",
            3: "#пошлость #любовь #секс #cute #pose #эротика"
        }

        self.themes_secondary = {
            1: "#joseph #josephmemes #jotaro #jojobizzareadventure #JoJo #JJBAmeme #jjbamemes #JJBAcringe #giorno #джоджо #memes #kakyoin #dio #meme #goldenwind #ventoaureo #giornogiovanna",
            2: "#твиттер_мемы #марвел #эстетика #книги #советы #тикток #cute #уходзалицом #милота #рекомендации #selfcarerussia #фикбук #сериалы #селфкейр #чтопосмотреть #twitter #twit #актуальные #тамблемемы #фандом #отп #мемы #сидимдома #сиэтл #саллифейс #threads #тред #мода",
            3: "#women #adorable #hot #gorgeous #face #fine #lips #love #beauty #sexy #fetish #чулочки #ступни #голые #вчулках #stockings #носки #красота #legs #ножки #nylon"
        }

        self.invitation = {
            1: "\n\n Подписочку! \n\n| \n\n",
            2: "Подписывайся! \nСтавь лайк!\nЭто очень помогает паблику\n.\n.\nтеги:",
            3: "Подписывайся, чтобы лучший контент всегда был в твоей ленте)\n.\n.\nтеги:"
        }

        self.groups = {
            1: "https://business.facebook.com/creatorstudio?tab=instagram_content_posts&mode=instagram&collection_id=all_pages&content_table=INSTAGRAM_POSTS",
            2: "https://business.facebook.com/creatorstudio?tab=instagram_content_posts&mode=instagram&collection_id=all_pages&content_table=INSTAGRAM_POSTS",
            3: "https://business.facebook.com/creatorstudio?tab=instagram_content_posts&mode=instagram&collection_id=all_pages&content_table=INSTAGRAM_POSTS"
        }

        self.group_names = {
            1: "overdrive_retro",
            2: "my_favourite_twitter",
            3: "cutie_creamies"
        }

    def description_create(self, theme):
        text_file_prim = self.themes_primary[theme].split(" ")
        text_file_sec = self.themes_secondary[theme].split(" ")

        hashtags = text_file_prim + (random.sample(text_file_sec, len(text_file_sec) // 2))
        random.shuffle(hashtags)
        hashtags = " ".join(hashtags)
        hashtags = self.invitation[theme] + hashtags

        return hashtags
