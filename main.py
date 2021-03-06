import discord
import os
import spotify

from discord.ext import commands

bot = commands.Bot(command_prefix='$')
bot.remove_command('help')

@bot.event
async def on_ready():
  print('login successful')

@bot.command()
async def followers(context):
  r = spotify.followers(context.message.content)
  if r == -1:
    await context.send("Artist not found. Please try again")
  else:
    await context.send(r)

@bot.command()
async def topsongs(context):
  r = spotify.topSongs(context.message.content)
  if r == -1:
    await context.send("Artist not found. Please try again")
  else:
    await context.send(r)

@bot.command()
async def related(context):
  r = spotify.related(context.message.content)
  if r == -1:
    await context.send("Artist not found. Please try again")
  else:
    await context.send(r)

@bot.command()
async def albums(context):
  r = spotify.albums(context.message.content)
  if r == -1:
    await context.send("Artist not found. Please try again")
  else:
    await context.send(r)

@bot.command(aliases=['help'])
async def commands(context):
  dirname = os.path.dirname(__file__)
  with open(dirname + '/commands.txt') as f:
    txt = f.read()
  embed=discord.Embed(title="Command List", description=txt, color=0xFF5733)
  await context.send(embed=embed)

bot.run(os.getenv('SpotifyBotKey'))