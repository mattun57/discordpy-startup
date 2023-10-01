from os import getenv
import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
	print("Logged in as")
	print(client.user.name)
	print(client.user.id)
	print("------")


@client.event
async def on_voice_state_update(member, before, after):
    if member.guild.id == 'サーバーIDをここに記入（クォート不要）':
        txt_room = client.get_channel('テキストチャンネルIDをここに記入（クォート不要）')
        if before.channel is None:
            msg = f'**{member.name}**さんが **{member.guild.name}** に参加しました。'
            await txtRoom.send(msg)


@client.event
async def on_message(message):
    if message.content.startswith("time"):
        await message.channel.send("https://www.time-j.net/WorldTime/Country/JP")

    if message.content.startswith("no"):
        msg = f'**{message.member.name}**さんは今日参加できないようです。'
        await message.channel.send(msg)

token = getenv('DISCORD_BOT_TOKEN')
client.run(token)
