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

      
    

client.run('NULL')