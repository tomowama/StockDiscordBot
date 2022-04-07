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
        await message.channel.send('Hey there connor, I am currently running on a always on replit')
    
    if message.content.startswith('$tom'):
        await message.channel.send('I love tom so so so much')
    





client.run('OTYxNDYyMTk4OTc3MzIzMDYw.Yk5Vcw.But9t4ASGoHX_U7mBv0SV6HDfGY')