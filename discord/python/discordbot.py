# importeer de discord module
import discord
from discord.ext import commands

# token van op https://discord.com/developers, zie README.md
bot_token = ""

# opzetten van de bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents)

# registreer een commando
@bot.command()
# dit is een subroutine (functie) voor een commando met naam "hello"
async def hello(ctx):
    # geef antwoord terug
    await ctx.send('Coderdojo!')

# start de bot
bot.run(bot_token)

