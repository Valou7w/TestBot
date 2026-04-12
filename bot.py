import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
load_dotenv()

print("Lancement du bot...")
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Bot prêt.")
    # Synchroniser les commandes qu'on a crées
    try:
        #sync
        synced = await bot.tree.sync()
        print(f"Commandes synchronisées : {len(synced)}")
    except Exception as e:
        print(e)

@bot.event
async def on_message(message: discord.Message):
    # Empecher le bot de repondre a ses messages 
    if message.author.bot:
        return

    if message.content.lower() == 'bienvenu':
        welcome_channel = bot.get_channel(1492876792090857583)
        await welcome_channel.send("Bienvenue chez DEDSEC")

    if message.content.lower() == 'salut':
        channel = message.channel
        await channel.send("salut")

@bot.tree.command(name="instagram", description=("Affiche mon Instagram"))
async def instagram(interaction: discord.Interaction):
    await interaction.response.send_message("Voici mon Instagram : https://www.instagram.com/valou7w/")

@bot.tree.command(name="test", description=("test embed"))
async def test(interaction: discord.Interaction):
    embed = discord.Embed(
        title="Titre test",
        description="Description test",
        color=discord.Color.yellow()
    )
    embed.add_field(name="Test1", value="Test111111111111111111111", inline=False)
    embed.add_field(name="Test2", value="Test222222222222222222222", inline=False)
    embed.set_footer(text="Test pied de page... JaaJ")
    embed.set_author(name="DEDSEC")
    embed.set_image(url="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExc3M1eHp5cjByNHJtcDZodndpcng4d2JuaG4wM3VmdnlidHJpdWdyMiZlcD12MV9naWZzX3RyZW5kaW5nJmN0PWc/GpyS1lJXJYupG/giphy.gif")


    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="warn", description=("Averti un utilisateur"))
async def warn(interaction: discord.Interaction, member: discord.Member):
    await interaction.response.send_message("Avertissement envoyé.")
    await member.send("Ceci est un avertissement, calme toi s'il te plait.")
    















































bot.run(os.getenv('TOKEN'))