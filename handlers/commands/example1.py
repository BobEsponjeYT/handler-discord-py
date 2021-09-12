
import discord
from discord.ext import commands
import asyncio

async def run(ctx=None):
  await ctx.send("Example")
  await asyncio.sleep(5)
  msg = await ctx.send("Example")
  await asyncio.sleep(5)
  await msg.delete()
