import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord.ext.commands import permissions

import asyncio
import time

client = commands.Bot(command_prefix ="!")

@client.event
async def on_ready():
	print("Bot is running")

	 await client.change_presence(status=discord.Status.do_not_disturb, 
 	activity=discord.Activity(type=discord.ActivityType.playing, name="github.com/devmaul"))

@client.command()
async def github(ctx):
	await ctx.send("Github: github.com/devmaul")


# Key goes in the ""'s below.
client.run("")