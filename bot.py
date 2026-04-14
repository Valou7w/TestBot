import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
load_dotenv()

#######################################################################################
#                                Initialisation du bot                                #
#######################################################################################

print("Lancement du bot...")
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Bot prêt.")
    # Synchronisation des commandes @bot.tree.command
    try:
        synced = await bot.tree.sync()
        print(f"Commandes synchronisées : {len(synced)}")
    except Exception as e:
        print(e)

#######################################################################################
#                           Réaction a un message specifique                          #
#######################################################################################

@bot.event
# Empecher le bot de repondre à ses messages ou ceux d'un autre bot
async def on_message(message: discord.Message):
    if message.author.bot:
        return
    
# Le bot répond au message "bienvenue" dans le channel "1492876792090857583"
    if message.content.lower() == "bienvenue":
        welcome_channel = bot.get_channel(1492876792090857583)
        await welcome_channel.send("Bienvenue chez DEDSEC")

# Le bot répond au message "salut" dans le channel d'envoi du message
    if message.content.lower() == "salut":
        channel = message.channel
        await channel.send("Salut")

#######################################################################################
#                 Commandes de test a supprimer ou modifier plus tard                 #
#######################################################################################

@bot.tree.command(name="instagram", description=("Affiche mon Instagram"))
async def instagram(interaction: discord.Interaction):
    await interaction.response.send_message("Voici mon Instagram : https://www.instagram.com/valou7w/")

@bot.tree.command(name="testembed", description=("Commande de test pour les messages de type 'embed'."))
async def testembed(interaction: discord.Interaction):
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


#######################################################################################
#                               Commandes de moderation                               #
#######################################################################################

@bot.tree.command(name="warn", description=("Averti un utilisateur"))
async def warn(interaction: discord.Interaction, member: discord.Member):
    await interaction.response.send_message(f"Avertissement envoyé à {member}", ephemeral=True)
    await member.send("Ceci est un avertissement, calme toi s'il te plait.")

@bot.tree.command(name="ban", description=("Banni un utilisateur"))
async def warn(interaction: discord.Interaction, member: discord.Member):
    await interaction.response.send_message(f"{member} a été banni.", ephemeral=True)
    await member.send("Tu as été banni.")
    await member.ban()
 
@bot.tree.command(name="clear", description=("Supprime autant de messages que défini (par defaut : 10)"))
async def clear(interaction: discord.Interaction, amount: int = 10):
    await interaction.response.send_message(f"{amount} messages ont été supprimés.", ephemeral=True)
    await interaction.channel.purge(limit = amount)











































bot.run(os.getenv('TOKEN'))