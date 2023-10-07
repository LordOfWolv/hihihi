import random
import discord
from discord.ext import commands
from bot_logic import gen_pass, gen_coin
import os
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    return password

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hello! Im live in Russia {bot.user}!')

@bot.command()
async def helpp(ctx):
    await ctx.send(f'Go to my telegram channel to learn more about the functions and commands of the bot')

@bot.command()
async def password(ctx):
    await ctx.send(gen_pass())

@bot.command()
async def coin(ctx):
    await ctx.send(gen_coin())

@bot.command()
async def busya(ctx):
    lst = os.listdir('busya')
    rand_img = random.choice(lst)
    with open('busya/' + rand_img, 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)

@bot.command()
async def animals(ctx):
    lst = os.listdir('animals')
    rand_img = random.choice(lst)
    with open('animals/' + rand_img, 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)
    




bot.run('')
