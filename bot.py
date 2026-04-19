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
#                          Réaction a un evenement specifique                         #
#######################################################################################

@bot.event
# Empecher le bot de repondre à ses messages ou ceux d'un autre bot
async def on_message(message: discord.Message):
    if message.author.bot:
        return

# Le bot répond au message "salut" dans le channel d'envoi du message
    if message.content.lower() == "salut":
        channel = message.channel
        await channel.send("Salut")

@bot.event
async def on_member_join(member):
        role = discord.utils.get(member.guild.roles, name="Membre")
        await member.add_roles(role)
        welcome_channel = bot.get_channel(1494674270108913794)
        await welcome_channel.send(f"Bienvenue chez DEDSEC {member} !")
    

#######################################################################################
#                 Commandes de test a supprimer ou modifier plus tard                 #
#######################################################################################

# Commande /instagram
@bot.tree.command(name="instagram", description=("Affiche mon Instagram"))
async def instagram(interaction: discord.Interaction):
    await interaction.response.send_message("Voici mon Instagram : https://www.instagram.com/valou7w/")

# Commande /testembed
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

# Commande /reseaux
@bot.tree.command(name="reseaux", description=("Affiche les reseaux du créateur."))
async def testembed(interaction: discord.Interaction):
    embed = discord.Embed(
        title="Reseaux de Whitedream",
        color=discord.Color.blurple()
    )
    embed.add_field(name="Instagram", value="https://www.instagram.com/valou7w/", inline=False)
    embed.add_field(name="Discord", value="whitedream_", inline=False)
    embed.add_field(name="Steam", value="https://steamcommunity.com/profiles/76561199055041812/", inline=False)

    await interaction.response.send_message(embed=embed, ephemeral=True)

#######################################################################################
#                               Commandes de moderation                               #
#######################################################################################

#Commande /clear
@bot.tree.command(name="clear", description=("Supprime autant de messages que défini (par defaut : 10)"))
@discord.app_commands.default_permissions(manage_messages=True)
async def clear(interaction: discord.Interaction, amount: int = 10):
    embed = discord.Embed(
        title=f"{amount} messages ont été supprimés.",
        color=discord.Color.blurple()
    )

    await interaction.response.send_message(embed=embed, ephemeral=True)
    await interaction.channel.purge(limit = amount)

# Commande /warn
@bot.tree.command(name="warn", description=("Averti un utilisateur"))
@discord.app_commands.default_permissions(manage_messages=True)
async def warn(interaction: discord.Interaction, member: discord.Member):
    embed = discord.Embed(
        title=f"Avertissement envoyé à {member}",
        color=discord.Color.blurple()
    )

    await interaction.response.send_message(embed=embed, ephemeral=True)
    await member.send("Ceci est un avertissement, calme toi s'il te plait.")

# Commande /kick
@bot.tree.command(name="kick", description=("Expulse un utilisateur"))
@discord.app_commands.default_permissions(ban_members=True)
async def kick(interaction: discord.Interaction, member: discord.Member):
    embed = discord.Embed(
        title=f"{member} a été expulsé.",
        color=discord.Color.blurple()
    )

    await interaction.response.send_message(embed=embed, ephemeral=True)
    await member.send("Tu as été expulsé.")
    await member.kick()

# Commande /ban
@bot.tree.command(name="ban", description=("Banni un utilisateur"))
@discord.app_commands.default_permissions(ban_members=True)
async def ban(interaction: discord.Interaction, member: discord.Member):
    embed = discord.Embed(
        title=f"{member} a été banni.",
        color=discord.Color.blurple()
    )

    await interaction.response.send_message(embed=embed, ephemeral=True)
    await member.send("Tu as été banni.")
    await member.ban()
 











































bot.run(os.getenv('TOKEN'))