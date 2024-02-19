# AntiScam
Discord bot code to stop users that are scamming with fake messages of free discord nitro on servers in order to steal users accounts.  

# How to use
The simplest bot you can create using this repo is just running the AntiScam.py file with python3 (after creating the bot at the discord developers portal and replacing <bot-token> with the token).  

To run the bot, the discord.py module must be installed (on linux, `pip3 install discord.py`).  
More info about how to install discord.py is in their docs: https://discordpy.readthedocs.io/en/stable/intro.html  
If you found any trouble, you can report it at the issues section.  

If you don't know how to create a discord bot or how to manage server permissions, here is a video made by S4vitar of how to do that: https://youtu.be/k0e_AnL5UeE  
Thanks to S4vitar and all those Hack4u moderators who helped me with the testing and for improving this bot with the aim of stoping this type of scam on discord servers!  

# Update
Because of a Discord API modification, you might need to enable the "Message Content Intent" option on the Discord Developer Portal.  
That's also why this repo have been updated, it was deprecated because of the change on the Discord API.

**IMPORTANT:** Because of the change on the API, the python module dependency has been changed so if you already had a bot working with the old codethe py-cord module, you will need to uninstall it and install instead the discord.py module.
