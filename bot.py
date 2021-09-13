import discord
from discord.ext import commands, tasks
import asyncio
from handlers.commands import *
from handlers.events import *

bot = commands.Bot(command_prefix="!", help_command=None)

@bot.event
async def on_ready():
  pass

## Commands

@bot.command() ## Simple command
async def one(ctx):
  await example1.run(ctx=ctx)
  
## Events

@bot.event ## Advanced event
async def on_command_error(ctx, error):
  await command_error.event(ctx=ctx, error=error)
  
bot.run("TOKEN")
