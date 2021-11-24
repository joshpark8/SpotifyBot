import discord
import os
import requests
from pathlib import Path
import spotify

from discord.ext import commands

bot = commands.Bot(command_prefix='$')
    
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

@bot.command()
async def commands(context):
  txt = Path('.\commands.txt').read_text()
  embed=discord.Embed(title="Command List", description=txt, color=0xFF5733)
  await context.send(embed=embed)

bot.run(os.getenv('DiscordKey'))
