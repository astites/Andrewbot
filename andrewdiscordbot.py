import discord

# Set up the bot with intents
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

# The user ID you want to monitor
TARGET_USER_ID = 1412420903987450029  # Replace with actual user ID

@client.event
async def on_ready():
    print(f'Bot is ready! Logged in as {client.user}')

@client.event
async def on_message(message):
    # Don't respond to the bot's own messages
    if message.author == client.user:
        return
    
    # Check if message is from the target user
    if message.author.id == TARGET_USER_ID:
        await message.channel.send(f"Hey {message.author.mention}, Shut the fuck up!")
        # Or reply directly to their message
        # await message.reply("I'm watching you! 👀")

# Run the bot
client.run('MTQyMzM0OTkwNDE1NTIxNzkyMA.G8q8N6._1qFZgPEWUt3cy34T7qXzzJCehQo27q_QraeX0')