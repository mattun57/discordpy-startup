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
    if member.guild.id == 600996774336790538:
        txtRoom = client.get_channel(600996774336790540)
        if before.channel is None:
            msg = f'**{member.name}**さんが **しーめい** に参加しましたけど...'
            await txtRoom.send(msg)


@client.event
async def on_message(message):
    if message.content.startswith("ありがとねぇ"):
        await message.channel.send("どういたしまして...ですけど...")

    if message.content.startswith("やあ"):
        await message.channel.send("こんにちは...ですけど")

    if message.content.startswith("世界時間"):
        await message.channel.send("https://www.time-j.net/WorldTime/Country/JP")

    if message.content.startswith("yaeh"):
        await message.channel.send("That's exactly what l've been wanting BOOMERANG!!!")


token = getenv('DISCORD_BOT_TOKEN')
client.run(token)
