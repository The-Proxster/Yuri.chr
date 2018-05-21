#Yuri.chr bot. Made for The Holy Yuri Empire. Made by Prox.
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import os

bot = commands.Bot(command_prefix='Y! ')
@bot.event
async def on_ready():
    print ("Yuri.chr Bot online.")
    await bot.change_presence(game=discord.Game(name='with knives.'))

@bot.command(pass_context=True)
async def praise(ctx):
    await bot.say("All hail Yuri, our lord and master. She is the one who gives us life. Praise Yuri, hail Yuri!", tts=True)

@bot.command(pass_context=True)
async def lewd(ctx):
    await bot.say("https://cdn.discordapp.com/attachments/436743371873058817/437040460163317761/image.jpg")

@bot.command(pass_context=True)
async def monihate(ctx):
    await bot.say("FUCK MONIKA!", tts=True)
    await bot.say("https://cdn.discordapp.com/attachments/433405166960508938/435671290188398602/image.jpg")

@bot.command(pass_context=True)
async def spine(ctx):
    await bot.say("https://cdn.discordapp.com/attachments/415681439456296980/437021088476561408/unknown.png")

@bot.command(pass_context=True)
async def dontleave(ctx):
    await bot.say("Please don't leave us, leave me. We will miss you, I will miss you.~")
    await bot.say("https://i.redd.it/jgrci9wr4pq01.png")

@bot.command(pass_context=True)
async def answer(ctx):
    await bot.say()

@bot.command(pass_context=True)
async def surprised(ctx):
    await bot.say("https://cdn.discordapp.com/attachments/415681439456296980/437066780146532352/unknown.png")

@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say("https://cdn.discordapp.com/attachments/415681439456296980/437066780146532352/unknown.png")
    await bot.say("You must like me r-right?~")
    

bot.run(os.environ['BOT_TOKEN'])
