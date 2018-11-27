import discord
import asyncio

lexia = discord.Client()

@lexia.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@lexia.event
async def on_message(message):
    if message.content.startswith('!test'):
        counter = 0
        tmp = await latina.send_message(message.channel, 'Calculating messages...')
        async for log in latina.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await latina.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await latna.send_message(message.channel, 'Done sleeping')

lexia.run('token')
