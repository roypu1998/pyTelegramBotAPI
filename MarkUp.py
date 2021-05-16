from telebot.types import InlineKeyboardMarkup

from telebot.types import InlineKeyboardButton

class MarkUp:


    def gen_markup(self):
        markup = InlineKeyboardMarkup()
        markup.row_width = 7
        markup.add(InlineKeyboardButton("About Me 📝", callback_data="about"))
        markup.add(InlineKeyboardButton("Knowledge 🧠", callback_data="knowledge"))
        markup.add(InlineKeyboardButton("Resume 📇", callback_data="resume"))
        markup.add(InlineKeyboardButton("Social Media 📲", callback_data="media"))
        markup.add(InlineKeyboardButton("Contact Me ☎️", callback_data="cont"))
        markup.add(InlineKeyboardButton("WebSite 🧑‍💻", callback_data="site"))
        markup.add(InlineKeyboardButton("Desires 🎯", callback_data="work"))
        markup.add(InlineKeyboardButton("🇮🇱 Change Language 🇺🇸", callback_data="setLan"))
        markup.add(InlineKeyboardButton("I Want To Quit 👋", callback_data="bye"))

        return markup

    def gen_markup_media(self):
        markup = InlineKeyboardMarkup()
        markup.row_width = 6
        markup.add(InlineKeyboardButton("GitHub", callback_data="git"))
        markup.add(InlineKeyboardButton("LinkedIn", callback_data="link"))
        markup.add(InlineKeyboardButton("Telegram", callback_data="telegram"))
        markup.add(InlineKeyboardButton("Instagram", callback_data="insta"))
        markup.add(InlineKeyboardButton("Facebook", callback_data="facebook"))
        markup.add(InlineKeyboardButton("Return To Menu 🔁", callback_data="return"))

        return markup

    def gen_markup_contact(self):
        markup = InlineKeyboardMarkup()
        markup.row_width = 4
        markup.add(InlineKeyboardButton("Email 📧", callback_data="email"))
        markup.add(InlineKeyboardButton("WhatsApp", callback_data="whatsapp"))
        markup.add(InlineKeyboardButton("Phone 📱", callback_data="Phone"))
        markup.add(InlineKeyboardButton("Return To Menu 🔁", callback_data="return"))

        return markup

    def set_markup_return_menu(self):
        markup = InlineKeyboardMarkup()
        markup.row_width = 1
        markup.add(InlineKeyboardButton("Return To Menu 🔁", callback_data="return"))
        return markup

    def set_markup_return_social_menu(self):
        markup = InlineKeyboardMarkup()
        markup.row_width = 1
        markup.add(InlineKeyboardButton("Return To Media Menu 🔁", callback_data="return_media"))
        return markup


    def create_markup(self,string,callback_data):
        markup = InlineKeyboardMarkup()
        markup.row_width = 1
        markup.add(InlineKeyboardButton(string, callback_data=callback_data))
        return markup

    def create_inline_keyboard_btn(self, string, url):
        markup = InlineKeyboardMarkup()
        markup.row_width = 2
        markup.add(InlineKeyboardButton(text=string, callback_data='return', url=url))
        markup.add(InlineKeyboardButton("Return To Menu 🔁", callback_data="return"))

        return markup

    def create_inline_keyboard_btn_media(self, string, url):
        markup = InlineKeyboardMarkup()
        markup.row_width = 2
        markup.add(InlineKeyboardButton(text=string, url=url))
        markup.add(InlineKeyboardButton("Return To Media Menu 🔁", callback_data="return_media"))
        return markup

    def create_inline_keyboard_btn_contact(self, string, url):
        markup = InlineKeyboardMarkup()
        markup.row_width = 2
        markup.add(InlineKeyboardButton(text=string, url=url))
        markup.add(InlineKeyboardButton("Return To Contact Menu 🔁", callback_data="return_cont"))
        return markup

####################################################################
######################## Hebrew MarkUps ############################

    def gen_markup_hb(self):
        markup = InlineKeyboardMarkup()
        markup.row_width = 7
        markup.add(InlineKeyboardButton("קצת עליי 📝", callback_data="a"))
        markup.add(InlineKeyboardButton("הידע שלי 🧠", callback_data="k"))
        markup.add(InlineKeyboardButton("קורות חיים 📇", callback_data="r"))
        markup.add(InlineKeyboardButton("מדיה חברתית 📲", callback_data="m"))
        markup.add(InlineKeyboardButton("צור קשר ☎️", callback_data="c"))
        markup.add(InlineKeyboardButton("האתר שלי 🧑‍💻", callback_data="s"))
        markup.add(InlineKeyboardButton("שאיפות 🎯", callback_data="w"))
        markup.add(InlineKeyboardButton("🇮🇱 שנה שפה 🇺🇸", callback_data="set"))
        markup.add(InlineKeyboardButton("רוצה לצאת? 👋", callback_data="b"))

        return markup

    def gen_markup_media_hb(self):
        markup = InlineKeyboardMarkup()
        markup.row_width = 6
        markup.add(InlineKeyboardButton("גיטהאב", callback_data="g"))
        markup.add(InlineKeyboardButton("לינקדאין", callback_data="l"))
        markup.add(InlineKeyboardButton("טלגרם", callback_data="t"))
        markup.add(InlineKeyboardButton("אינסטגרם", callback_data="i"))
        markup.add(InlineKeyboardButton("פייסבוק", callback_data="f"))
        markup.add(InlineKeyboardButton("חזרה לתפריט הראשי 🔁", callback_data="ret"))

        return markup


    def gen_markup_contact_hb(self):
        markup = InlineKeyboardMarkup()
        markup.row_width = 4
        markup.add(InlineKeyboardButton("אימייל 📧", callback_data="e"))
        markup.add(InlineKeyboardButton("וואטסאפ", callback_data="what"))
        markup.add(InlineKeyboardButton("טלפון 📱", callback_data="P"))
        markup.add(InlineKeyboardButton("חזרה לתפריט הראשי 🔁", callback_data="ret"))

        return markup

    def set_markup_return_menu_hb(self):
        markup = InlineKeyboardMarkup()
        markup.row_width = 1
        markup.add(InlineKeyboardButton("חזרה לתפריט הראשי 🔁", callback_data="ret"))
        return markup

    def set_markup_return_social_menu_hb(self):
        markup = InlineKeyboardMarkup()
        markup.row_width = 1
        markup.add(InlineKeyboardButton("חזרה לתפריט המדיה 🔁", callback_data="ret_media"))
        return markup


    def create_markup_hb(self,string,callback_data):
        markup = InlineKeyboardMarkup()
        markup.row_width = 1
        markup.add(InlineKeyboardButton(string, callback_data=callback_data))
        return markup

    def create_inline_keyboard_btn_hb(self, string, url):
        markup = InlineKeyboardMarkup()
        markup.row_width = 2
        markup.add(InlineKeyboardButton(text=string, callback_data='ret', url=url))
        markup.add(InlineKeyboardButton("חזרה לתפריט הראשי 🔁", callback_data="ret"))

        return markup

    def create_inline_keyboard_btn_media_hb(self, string, url):
        markup = InlineKeyboardMarkup()
        markup.row_width = 2
        markup.add(InlineKeyboardButton(text=string, url=url))
        markup.add(InlineKeyboardButton("חזרה לתפריט המדיה 🔁", callback_data="ret_media"))
        return markup

    def create_inline_keyboard_btn_contact_hb(self, string, url):
        markup = InlineKeyboardMarkup()
        markup.row_width = 2
        markup.add(InlineKeyboardButton(text=string, url=url))
        markup.add(InlineKeyboardButton("חזרה לתפריט יצירת הקשר 🔁", callback_data="ret_cont"))
        return markup


    def create_hb_en_btn(self):
        markup = InlineKeyboardMarkup()
        markup.row_width = 2
        markup.add(InlineKeyboardButton("עברית 🇮🇱", callback_data="hebrew"))
        markup.add(InlineKeyboardButton("English 🇺🇸", callback_data="english"))
        return markup
