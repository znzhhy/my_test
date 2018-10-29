from wxpy import *

bot = Bot(console_qr = True,cache_path = True)

tuling = Tuling(api_key='d40730a549f0483eac71621471095f2b')

@bot.register([my_friend, Group], TEXT)
def auto_reply_all(msg):
    tuling.do_reply(msg)

embed()
