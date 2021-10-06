# bot.py
import os
import discord

bot = discord.Client()

prefix = "!"


@bot.event # when it's in a server
async def on_ready():
    guild_count = 0

    for guild in bot.guilds:
        print(f"- {guild.id} (name: {guild.name})")

    guild_count = guild_count + 1

    print("Miscellaneous Bot is in " + str(guild_count))


@bot.event # when message is sent to a channel
async def on_message(message):
    if message.content == prefix + "What's up?":
        await message.channel.send("Whaddup")
    elif message.content == prefix + "prefix":
        await message.channel.send(prefix) # TODO: !prefix x changes prefix to x


bot.run("ODk0NjM4ODkwODY5MTk4ODk5.YVs7ZQ.K2rv7Uaw9gQO7RRFel7_nYB3p_k")
