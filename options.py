import random


class Options:
    def __init__(self):
        self.themes_primary = {
            1: "#jojo #jjba #jojosbizzareadventure #jojokes #jojomemes",
            2: "#procreatedrawing #procreateart #digitalillustration ",
            3: ""
        }

        self.themes_secondary = {
            1: "#joseph #josephmemes #jotaro #jojobizzareadventure #JoJo #JJBAmeme #jjbamemes #JJBAcringe #giorno #джоджо #memes #kakyoin #dio #meme #goldenwind #ventoaureo #giornogiovanna",
            2: "#inktober #digitalart #digitalpainting #art #artwork #drawing #draw #sketch #sketchbook #sketching #digitalsketchbook #sketchbooks #artistsoninstagram #artsy #arts #procreate #procreateapp #ipadpro #ipadproart #arttutorial #painting #paint #drawthisinyourstyle #dtiys #sketches #procreatetutorial #wipart",
            3: ""
        }

        self.invitation = {
            1: "\n\n Подписочку! \n\n| \n\n",
            2: "|\n|\n Подписывайся на @acid.illustrate \n|\n|\n"
        }

        self.groups = {
            1: "https://business.facebook.com/creatorstudio?tab=instagram_content_posts&mode=instagram&collection_id=all_pages&content_table=INSTAGRAM_POSTS",
            2: "https://postingram.ru/account/42346/"
        }

    def description_create(self, theme):
        text_file_prim = self.themes_primary[theme].split(" ")
        text_file_sec = self.themes_secondary[theme].split(" ")

        hashtags = text_file_prim + (random.sample(text_file_sec, len(text_file_sec) // 2))
        random.shuffle(hashtags)
        hashtags = " ".join(hashtags)
        hashtags = self.invitation[theme] + hashtags

        return hashtags
