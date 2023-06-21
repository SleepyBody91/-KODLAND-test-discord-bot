import discord
from discord.ext import commands
import openai
import requests
import os
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

openai.api_key = 'api' # тут ключ Open AI

def get_dog_image_url():
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command(name='собака')
async def dog(ctx):
    image_url = get_dog_image_url()
    await ctx.send(image_url)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh=5):
    await ctx.send("he" * count_heh)

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def ask(ctx, *, question):
    response = openai.Completion.create(
        engine='davinci', # движок
        prompt=question, # тип вопроса
        max_tokens=50 # ограничение в токенах
    )
    await ctx.send(response.choices[0].text) # отправка ответа

@bot.command()
async def e_help(ctx):
    await ctx.send("команды сервера префикс бота = (command_prefix),команды: ask - отправить запрос ИИ (токин не дам, add - добавляет a + b = c)")

@bot.group()
async def cool(ctx):
    """Says if a user is cool.

    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not cool')

@bot.command()
async def mem(ctx):
    random_mem = random.randint(1, 2)
    if random_mem == 1:
        with open('images/mem1.jpg', 'rb') as f:
            picture = discord.File(f)
            await ctx.send(file=picture)
    elif random_mem == 2:
        with open('images/mem2.jpg', 'rb') as f:
            picture = discord.File(f)
            await ctx.send(file=picture)

bot.run('api_key')
