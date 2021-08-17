from os import getenv
import discord
import asyncio

client = discord.Client()

'''
@client.event
async def on_voice_state_update(member, before, after):

    if before.channel != after.channel:
        # 通知メッセージを書き込むテキストチャンネル（チャンネルIDを指定）
        botRoom = client.get_channel(600996774336790539)
        # 入退室を監視する対象のボイスチャンネル（チャンネルIDを指定）
        announceChannelIds = [600996774336790541]

        # 退室通知
        if before.channel is not None and before.channel.id in announceChannelIds:
            await botRoom.send("**" + before.channel.name + "** から、__" + member.name + "__  が抜けましたけど...")
        # 入室通知
        if after.channel is not None and after.channel.id in announceChannelIds:
            await botRoom.send("**" + after.channel.name + "** に、__" + member.name + "__  が参加しましたけど...")
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
        #botRoom = client.get_channel(600996774336790539)
        botRoom = "<TextChannel id=600996774336790540 name='一般' position=0 nsfw=False news=False category_id=600996774336790539>"
        if before.channel is None:
            #msg = f'{member.name} さんが {after.channel.name} に参加しましたけど...'
            await botRoom.send('入りましたけど...')


@client.event
async def on_message(message):
    if message.content.startswith("hello"):
        m = "こんにちは...ですけど"
        await message.channel.send(m)


token = getenv('DISCORD_BOT_TOKEN')
client.run(token)
