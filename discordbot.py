from discord.ext import commands
from os import getenv
import traceback
import discord

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
    await ctx.send('都会の公園を走るリスさんのように♪')
       
    
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
async def ass(ctx):
    await ctx.send('ケツの穴臭すぎですけど...')
    
    
@bot.command()
async def test(ctx):
    await ctx.send('テストですけど...')
    
    
@bot.command()
async def he(ctx):
    await ctx.send('オナラですけど...')
    
    
@bot.command()
async def dare(ctx):
    await ctx.send('森久保ですけど...')
    
  
'''
# チャンネル入退室時の通知処理
@client.event
async def on_voice_state_update(member, before, after):
 
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
async def on_voice_state_update(member,before,after):
    if before.channel != after.channel:
        # before.channelとafter.channelが異なるなら入退室
        if after.channel and len(after.channel.members) == 1:
            # もし、ボイスチャットが開始されたら
            send("**" + after.channel.name + "** に、__" + member.name + "__  が参加しましたけど...")

        if before.channel and len(before.channel.members) == 0:
            # もし、ボイスチャットが終了したら
            send("**" + before.channel.name + "** から、__" + member.name + "__  が抜けましたけど...")
            
token = getenv('DISCORD_BOT_TOKEN')
bot.run(token)
client.run(token)
