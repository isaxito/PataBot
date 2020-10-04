import random
import discord
from discord.ext import commands
import asyncio
from webserver import keep_alive
import os
from texto import *

bot = commands.Bot(command_prefix=';', description="Bot corrugado de prueba")
bot.remove_command('help')

# Funciones
def fraseDescanso(sujeto):
    frasesDormilonas = ["ya iría siendo la hora de dormir, no " + sujeto + "?",
                        sujeto + " ya se tiene que ir",
                        sujeto + " solo vino a saludar, ya se va",
                        "tenes toda la razon "+sujeto+", en serio pa",
                        sujeto+" lo hizo de nuevo",
                        sujeto+ " merece la muerte"]
    if(len(sujeto)<14):
      return frasesDormilonas[random.randint(0,len(frasesDormilonas)-1)]
    else:
      return "circula capo..."

def frasesElegir(eleccion1, eleccion2):
    frasesDeEleccion = [eleccion1+" me parece lo correcto",
                        eleccion1+" la re sube",
                        "por que alguien pensaría en "+eleccion2+" teniendo "+eleccion1+"??",
                        mccaco+" por "+eleccion1,
                        "te la hago corta capo, "+eleccion1,
                        "por que tanto odioo? "+eleccion1,
                        "algo me dice que el corru elegiría "+eleccion1+" porque "+eleccion2+" no es para el",
                        "esto puede ser una mentira pero me parece que "+eleccion1]
    return frasesDeEleccion[random.randint(0,len(frasesDeEleccion)-1)]

@bot.command()
async def comandos(ctx):
    embed = discord.Embed(title="Ayuda para normies", description=comandin,color=discord.Color.dark_orange())
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/384151156869431300/704037908729954334/iu.png")
    await ctx.send(embed=embed)
# Comandos graciosos
@bot.command()
async def icecube(ctx):
    await ctx.send(frasesIceCube[random.randint(0,len(frasesIceCube)-1)])
@bot.command()
async def mclovin(ctx):
    await ctx.send(frasesMclovin[random.randint(0, len(frasesMclovin)-1)])
@bot.command()
async def worms(ctx):
    await ctx.send('@everyone quien para jugar worms armageddon?')
@bot.command()
async def csgo(ctx):
    await ctx.send('@everyone quien para jugar csgo? (jungla/mm(lol)).')
@bot.command()
async def dota2(ctx):
    await ctx.send('@everyone quien para jugar dota2?')
@bot.command()
async def askFran(ctx):
    await ctx.send(frasesFran[random.randint(0, len(frasesFran)-1)])
@bot.command()
async def askMasi(ctx):
    await ctx.send(frasesMasi[random.randint(0, len(frasesMasi)-1)])
@bot.command()
async def askCorru(ctx):
    await ctx.send(frasesCorrugadas[random.randint(0,len(frasesCorrugadas)-1)])
@bot.command()
async def coronavirus(channel):
    await channel.send(file=discord.File('corona.png'))
    await channel.send("él")
@bot.command()
async def si(ctx, persona):
    await ctx.send(fraseDescanso(persona))
@bot.command()
async def elegir(ctx, op1, op2):
    if((len(op1)<16 and (len(op2)<16))):
      c = random.randint(1,2)
      if c == 1:
          await ctx.send(frasesElegir(op1, op2))
      else:
          await ctx.send(frasesElegir(op2, op1))
    else:
      await ctx.send("deja de intentarlo capo")
@bot.command()
async def hueno(channel):
    await channel.send(file=discord.File('Humpty_Dumpty.png'))
@bot.command()
async def biblia(ctx):
    await ctx.send(frasesBiblia[random.randint(0,len(frasesBiblia)-1)])
@bot.command()
async def redpill(ctx):
    await ctx.send(linkRedpill[random.randint(0,len(linkRedpill)-1)])
@bot.command()
async def windows10(channel):
    await channel.send(file=discord.File('windows10.png'))
@bot.command()
async def askMoya(ctx):
    await ctx.send("quien")


# Eventos
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name=";comandos"))
    print("Patabot funca")

keep_alive()
TOKEN = os.environ.get("DISCORD_BOT")
bot.run(TOKEN)
