from AntiScam import AntiScam

whitelist = [] # Here you can add the IDs of the users allowed to bypass the AntiScam system.
logs_channel = None # Here you can add the ID of the channel where the logs will be sent.

intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)

@bot.event
async def on_message(message):
    await AntiScam(message, bot = bot, whitelist = whitelist, muted_role='Muted', verified_role='Verified', logs_channel=logs_channel) # Here you can change the names of the roles.

bot.run('<bot-token>') # Change <bot-token> with the bot token (do not remove the '')
