import discord
from discord.ext import commands
import openai #ai

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

openai.api_key = 'КЛЮЧ_OpenAi' # тут ключ Open AI

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def ask(ctx, *, question):
    response = openai.Completion.create(
        engine='davinci', #движок
        prompt=question, # тип вопроса
        max_tokens=50 #ограничение в токинах
    )
    await ctx.send(response.choices[0].text) #отправка ответа

@bot.group()
async def cool(ctx):
    """Says if a user is cool.

    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not cool')

@bot.command()
async def help(ctx):
   # """Выводит список комманд."""
    command_list = [command.name for command in bot.commands]
    await ctx.send(f'Available commands: {", ".join(command_list)}')

bot.run('Ключ_бота_дискорд')
