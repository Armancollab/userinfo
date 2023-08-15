from pyrogram import *

print("This Bot Created By Mohammad Arman\nTG Username : @devnull9\nGithub : https://github.com/Armancollab")
bot = Client("Sample_userinfobot",api_id="API_ID",api_hash="API_HASH",bot_token="BOT_TOKEN")

@bot.on_message(filters.private)
async def private_chat(client , message):
      firstname = message.from_user.first_name
      userid    : str = str(message.from_user.id)
      username  : str = message.from_user.username
      lastname  : str = message.from_user.last_name
      text      : str = f"First Name : {firstname}\nLast Name : {lastname}\nUsername : {username}\nUser ID : {userid}"
      await bot.send_message(chat_id=message.chat.id , text=text)

@bot.on_message(filters.group)
async def group_chat(client , message):
       if message.text == "/start":
          chat_id     : str = str(message.chat.id)
          chat_name   : str = message.chat.title
          chat_member : str = str(message.chat.members_count)
          text        : str = f"Chat Name : {chat_name}\nChat ID : {chat_id}\nChat Members : {chat_member}"
          await bot.send_message(chat_id=message.chat.id , text=text)



if __name__ == "__main__":
    bot.run()
