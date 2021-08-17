from os import getenv
import discord
import asyncio

client = discord.Client()

'''
@client.event
async def on_voice_state_update(member, before, after):

    if before.channel != after.channel:
        # 通知メッセージを書き込むテキストチャンネル（チャンネルIDを指定）
        botRoom = client.get_channel(600996774336790540)
        # 入退室を監視する対象のボイスチャンネル（チャンネルIDを指定）
        announceChannelIds = [600996774336790541]

        # 退室通知
        if before.channel is not None and before.channel.id in announceChannelIds:
            await botRoom.send("**しーめい** から、__" + member.name + "__  が抜けましたけど...")
        # 入室通知
        if after.channel is not None and after.channel.id in announceChannelIds:
            await botRoom.send("**しーめい** に、__" + member.name + "__  が参加しましたけど...")
'''

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')


@client.event
async def on_voice_state_update(member, before, after):
    if member.guild.id == 600996774336790538:
        botRoom = client.get_channel(600996774336790540)
        print(client.get_channel(600996774336790539))
        print(client.get_channel(600996774336790540))
        if before.channel is None:
            msg = f'**{member.name}**さんが **しーめい** に参加しましたけど...'
            await botRoom.send(msg)


@client.event
async def on_message(message):
    if message.content.startswith("ありがとねぇ"):
        m = "どういたしまして...ですけど..."
        await message.channel.send(m)

    if message.content.startswith("やあ"):
        await message.channel.send("こんにちは...ですけど")


token = getenv('DISCORD_BOT_TOKEN')
client.run(token)
