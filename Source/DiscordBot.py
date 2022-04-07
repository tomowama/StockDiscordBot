import discord
import os

client = discord.Client()



@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    
    
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
      
    if message.content.startswith('$connor'):
      await message.channel.send('hello there my BRB')
    if message.content.startswith('$tom'):
      await message.channel.send('hello there my creator')

    if ' tom ' in message.content:
      await message.channel.send('you called?')
    if message.author.id == 290327583843942400:
      
      f = open("messageStats.txt", "r")
      oldNum = int(f.read())
      print(oldNum)
      num = oldNum +1
      f.close()
      f = open("messageStats.txt", "w")
      f.write(f"{num}")
      f.close()
      await message.channel.send(f"The number of annoying messages from Jake is {num}")

    
    

client.run('OTYxNDYyMTk4OTc3MzIzMDYw.Yk5Vcw.YJjPwSS6feEQ99L_jAevVDF3o5M')
numOfTomMessages = 0