# This example requires the 'message_content' intent.

import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} 로그인 완료')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$밍피티$'):
        await message.channel.send('왜요?')

client.run('MTE4MjMwODM2NTIxMzM3NjUxMg.GSgZ9W.LpimBjU1i3LLTo5c5pZDAV5gWdliiHyX94ocd4')
