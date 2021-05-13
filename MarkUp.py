from telebot.types import InlineKeyboardMarkup

from telebot.types import InlineKeyboardButton

class MarkUp:

    def gen_markup(self):
        markup = InlineKeyboardMarkup()
        markup.row_width = 7
        markup.add(InlineKeyboardButton("About Me", callback_data="about"))
        markup.add(InlineKeyboardButton("Knowledge", callback_data="knowledge"))
        markup.add(InlineKeyboardButton("Resume", callback_data="resume"))
        markup.add(InlineKeyboardButton("Social Media", callback_data="media"))
        markup.add(InlineKeyboardButton("Contact Me", callback_data="cont"))
        markup.add(InlineKeyboardButton("WebSite", callback_data="site"))
        markup.add(InlineKeyboardButton("Desires", callback_data="work"))
        markup.add(InlineKeyboardButton("I Want To Quit", callback_data="bye"))

        return markup

    def gen_markup_media(self):
        markup = InlineKeyboardMarkup()
        markup.row_width = 6
        markup.add(InlineKeyboardButton("GitHub", callback_data="git"))
        markup.add(InlineKeyboardButton("LinkedIn", callback_data="link"))
        markup.add(InlineKeyboardButton("Telegram", callback_data="telegram"))
        markup.add(InlineKeyboardButton("Instagram", callback_data="insta"))
        markup.add(InlineKeyboardButton("Facebook", callback_data="facebook"))
        markup.add(InlineKeyboardButton("Return To Menu", callback_data="return"))

        return markup

    def gen_markup_contact(self):
        markup = InlineKeyboardMarkup()
        markup.row_width = 4
        markup.add(InlineKeyboardButton("Email", callback_data="email"))
        markup.add(InlineKeyboardButton("WhatsApp", callback_data="whatsapp"))
        markup.add(InlineKeyboardButton("Phone", callback_data="Phone"))
        markup.add(InlineKeyboardButton("Return To Menu", callback_data="return"))

        return markup

    def set_markup_return_menu(self):
        markup = InlineKeyboardMarkup()
        markup.row_width = 1
        markup.add(InlineKeyboardButton("Return To Menu", callback_data="return"))
        return markup

    def set_markup_return_social_menu(self):
        markup = InlineKeyboardMarkup()
        markup.row_width = 1
        markup.add(InlineKeyboardButton("Return To Media Menu", callback_data="return_media"))
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
        markup.add(InlineKeyboardButton("Return To Menu", callback_data="return"))

        return markup

    def create_inline_keyboard_btn_media(self, string, url):
        markup = InlineKeyboardMarkup()
        markup.row_width = 2
        markup.add(InlineKeyboardButton(text=string, url=url))
        markup.add(InlineKeyboardButton("Return To Media Menu", callback_data="return_media"))
        return markup

    def create_inline_keyboard_btn_contact(self, string, url):
        markup = InlineKeyboardMarkup()
        markup.row_width = 2
        markup.add(InlineKeyboardButton(text=string, url=url))
        markup.add(InlineKeyboardButton("Return To Contact Menu", callback_data="return_cont"))
        return markup