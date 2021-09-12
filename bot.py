import discord
from discord.ext import commands, tasks
import asyncio
from handlers.commands import *

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
  pass

## Commands

@bot.command() ## Simple command
async def one(ctx):
  await example1.run(ctx=ctx)
  
  
bot.run("TOKEN")
