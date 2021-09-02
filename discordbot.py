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
    if member.guild.id == 849955942015565824:
        txtRoom = client.get_channel(849955942015565827)
        if before.channel is None:
            if member.id == 522369401878478848:
                msg = f'**人間のクズ**が **{member.guild.name}** に入ってきましたけど...'
            else:
                msg = f'**{member.name}**さんが **{member.guild.name}** に参加しましたけど...'
            await txtRoom.send(msg)


@client.event
async def on_message(message):
    if message.content.startswith("やあ"):
        msg = f'**{message.member.name}**さん、こんにちはですけど...'
        await message.channel.send(msg)

    if message.content.startswith("time"):
        await message.channel.send("https://www.time-j.net/WorldTime/Country/JP")

    if message.content.startswith("のー"):
        msg = f'**{message.member.name}**さんは今日むーりぃーみたいですけど...'
        await message.channel.send(msg)

    if message.content.startswith("ひん"):
        msg = f'**{message.member.name}**さん、元気出してくださいぃ...'
        await message.channel.send(msg)


token = getenv('DISCORD_BOT_TOKEN')
client.run(token)
