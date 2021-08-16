from discord.ext import commands
from os import getenv
import traceback

bot = commands.Bot(command_prefix='/')


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def shibuya(ctx):
    await ctx.send('渋谷は苦手ですけど...')
    

@bot.command()
async def mori(ctx):
    await ctx.send('都会の公園を走るリスさんのように♪')
    
    
    
@bot.command()
async def mattun(ctx):
    await ctx.send('プロデューサーさん...ありがとうございます...')
    
    
@bot.command()
async def miyagawa(ctx):
    await ctx.send('ひっ...')
    
"""    
@client.event
async def on_voice_state_update(member, before, after):
 
    # チャンネルへの入室ステータスが変更されたとき（ミュートON、OFFに反応しないように分岐）
    if before.channel != after.channel:
        # 通知メッセージを書き込むテキストチャンネル（チャンネルIDを指定）
        botRoom = client.get_channel(876803479006486550)
 
        # 入退室を監視する対象のボイスチャンネル（チャンネルIDを指定）
        announceChannelIds = [876803479006486551]

        # 入室通知
        if after.channel is not None and after.channel.id in announceChannelIds:
            await botRoom.send("**" + after.channel.name + "** に、__" + member.name + "__  が入ってきましたけど...")
"""

token = getenv('DISCORD_BOT_TOKEN')
bot.run(token)
