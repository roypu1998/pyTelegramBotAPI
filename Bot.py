from telebot import TeleBot

import datetime
import MarkUp



TOKEN = "<your_bot_TOKEN>"

bot=TeleBot(TOKEN)



def calc_age():
    born = datetime.date(1998,12,17)
    today = datetime.date.today()
    age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
    return age

age = calc_age()


text = "My name is Roi Putterman, I'm {} years old,I'm live in Rishon Lezion Israel,\ni'm studying software engineering at SCE College and is currently in my third year. \nHolder of a full matriculation certificate and 6 study units in accounting"

#Text
text_about = text.format(age)

text_Knowledge = "During the degree I acquired knowledge in related courses such as: software requirements management and software quality testing.\n" \
               "In addition I took courses of algorithms,Data Structure, Data bases,computers communication, C, node.js, HTML5, CSS, OOP - C++, JAVA (Develop, GUI and Design Patterns) , PYTHON .\n" \
               "I'm also have knowledge in SQL, MongoDB, Selenium ."
text_work="I am looking for my first junior job in the software field as: a programmer, software tester (manual or automatic), automation developer and any job that connects to the software field and can make me develop and learn.\n" \
          " So if you are looking for a person who likes to work with high self-learning who will not give up any piece of task and will not rest until the task is completed I would be happy to send a resume."

# Social - Media
telegram = "https://telegram.me/{}".format("<@username>_(without '@')>")
github = "https://github.com/roypu1998"
linkedin = "https://www.linkedin.com/in/roi-putterman-7024591b4/"
instagram = "https://www.instagram.com/roiputterman/"
facebook = "https://www.facebook.com/royputterman1/"

# Contact
whatsapp = "https://api.whatsapp.com/send?phone=+972505710075&amp;text=Hello! I would be happy if we could set to speak :)"
email = "royputtermanjob@gmail.com"
phone = "<your_phone"

markup = MarkUp.MarkUp()




@bot.callback_query_handler(func=lambda call: True)
def answer_callback_query(call):
    if call.data == "about":
        bot.edit_message_text(text=text_about,chat_id=call.message.chat.id,message_id=call.message.message_id,reply_markup=markup.set_markup_return_menu())

    elif call.data == "knowledge":
        bot.edit_message_text(text=text_Knowledge,chat_id=call.message.chat.id,message_id=call.message.message_id,reply_markup=markup.set_markup_return_menu())

    elif call.data == "resume":
        try:
            cv_resume = open("files/קו_ח עברית.pdf", 'rb')
            bot.send_document(call.message.chat.id,data=cv_resume)
            bot.send_message(chat_id=call.message.chat.id,text="Choose Option You Want :",reply_markup=markup.gen_markup())
            cv_resume.close()
        except:
            pass

    elif call.data == "media":
        bot.edit_message_text( text="Choose The Social-Media That You Want :",chat_id=call.message.chat.id,message_id=call.message.message_id, reply_markup=markup.gen_markup_media())

    elif call.data == "cont":
        bot.edit_message_text( text="Choose Option To Contact Me :",chat_id=call.message.chat.id,message_id=call.message.message_id, reply_markup=markup.gen_markup_contact())

    elif call.data == "site":
        bot.edit_message_text( text="Enter To My WebSite",chat_id=call.message.chat.id,message_id=call.message.message_id, reply_markup=markup.create_inline_keyboard_btn("My WebSite","https://personal-website-roiputterman.herokuapp.com/"))

    elif call.data == "work":
        bot.edit_message_text( text=text_work,chat_id=call.message.chat.id,message_id=call.message.message_id, reply_markup=markup.set_markup_return_menu())

    elif call.data == "git":
        bot.edit_message_text(text="Git Repository", chat_id=call.message.chat.id,message_id=call.message.message_id,reply_markup=markup.create_inline_keyboard_btn_media("GitHub",github))

    elif call.data == "link":
        bot.edit_message_text(text="My LinkedIn", chat_id=call.message.chat.id,message_id=call.message.message_id,reply_markup=markup.create_inline_keyboard_btn_media("LinkedIn",linkedin))

    elif call.data == "telegram":
        bot.edit_message_text(text="User Telegram", chat_id=call.message.chat.id,message_id=call.message.message_id,reply_markup=markup.create_inline_keyboard_btn_media("Telegram",telegram))

    elif call.data == "insta":
        bot.edit_message_text(text="My Instagram", chat_id=call.message.chat.id,message_id=call.message.message_id,reply_markup=markup.create_inline_keyboard_btn_media("Instagram",instagram))

    elif call.data == "facebook":
        bot.edit_message_text(text="My Facebook", chat_id=call.message.chat.id,message_id=call.message.message_id,reply_markup=markup.create_inline_keyboard_btn_media("Facebook",facebook))

    elif call.data == "email":
        bot.edit_message_text(text=email, chat_id=call.message.chat.id,message_id=call.message.message_id,reply_markup=markup.create_markup("Return To Contact Menu","return_cont"))

    elif call.data == "whatsapp":
        bot.edit_message_text(text="My WhatsApp", chat_id=call.message.chat.id,message_id=call.message.message_id,reply_markup=markup.create_inline_keyboard_btn_contact("WhatApp",whatsapp))

    elif call.data == "Phone":
        bot.edit_message_text(text=phone, chat_id=call.message.chat.id,message_id=call.message.message_id,reply_markup=markup.create_markup("Return To Contact Menu","return_cont"))

    elif call.data == 'return':
        bot.edit_message_text( text="Choose Option You Want :",chat_id=call.message.chat.id,message_id=call.message.message_id, reply_markup=markup.gen_markup())

    elif call.data == 'return_media':
        bot.edit_message_text( text="Choose The Social-Media That You Want :",chat_id=call.message.chat.id,message_id=call.message.message_id, reply_markup=markup.gen_markup_media())

    elif call.data == "return_cont":
        bot.edit_message_text( text="Choose Option To Contact Me :",chat_id=call.message.chat.id,message_id=call.message.message_id, reply_markup=markup.gen_markup_contact())

    elif call.data == "bye":
        bot.edit_message_text( text="Thank You ! GoodBye",chat_id=call.message.chat.id,message_id=call.message.message_id)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_chat_action(message.chat.id,"typing")
    bot.send_message(chat_id=message.chat.id,text="Choose Option You Want :",reply_markup=markup.gen_markup())


bot.polling()
