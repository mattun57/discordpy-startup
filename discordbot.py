from discord.ext import commands
from os import getenv
import traceback

import discord
import asyncio

bot = commands.Bot(command_prefix='/')
client = discord.Client()

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def shibuya(ctx):
    await ctx.send('本田は嫌いですけど...')
    
@bot.command()
async def mori(ctx):
    await ctx.send('こんにちは、お元気にしてますか？私は今、もりのくにで暮らしています。')
       
@bot.command()
async def mattun(ctx):
    await ctx.send('プロデューサーさん...いつもありがとうございます...')
    
@bot.command()
async def miyagawa(ctx):
    await ctx.send('ひん')
    
@bot.command()
async def no(ctx):
    await ctx.send('今日はむりくぼですけど...')
    
@bot.command()
async def yes(ctx):
    await ctx.send('今すぐいけますけど...')
    
@bot.command()
async def wait(ctx):
    await ctx.send('ちょっと待ってくださいぃ...')
    
@bot.command()
async def ass(ctx):
    await ctx.send('ケツの穴臭すぎですけど...')
    
@bot.command()
async def time(ctx):
    await ctx.send('https://www.time-j.net/WorldTime/Country/JP')
    
@bot.command()
async def yeah(ctx):
    await ctx.send("Yeah! That's exactly what l've been wanting BOOMERANG!!!")
    
@bot.command()
async def dare(ctx):
    await ctx.send('森久保ですけど...')
    
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
        text_ch = client.get_channel(600996774336790539)
        if before.channel is None: 
            msg = f'{member.name} が {after.channel.name} に参加しました。'
            await text_ch.send(msg)
'''
@client.event
async def on_message(message):
    if message.content.startswith("hello"):
        m = "こんにちは"
        await client.send_message(message.channel,m)
'''
        
           
token = getenv('DISCORD_BOT_TOKEN')
bot.run(token)
#client.run(token)
