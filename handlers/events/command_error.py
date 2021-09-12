import discord
from discord.ext import commands
import asyncio
from datetime import datetime

async def event(ctx, error):
  if(isinstance(error, commands.CommandNotFound)):
    embed = discord.Embed(
    title=None, 
    description=":x: Error. Command not found!",
    timestamp=datetime.utcnow(),
    color=discord.Colour.darkred()
    )
  if(isinstance(error, commands.MissingPermissions)):
    embed = discord.Embed(
    title=None, 
    description=":x: Error. Missing permissions!",
    timestamp=datetime.utcnow(),
    color=discord.Colour.darkred()
    )
  await ctx.send(embed=embed)
