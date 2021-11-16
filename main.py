from discord.ext import commands
from AntiScam import AntiScam

whitelist_s4vi = [500430447105540109,432228347074838538,871889282653106217,524301093014994956,270904126974590976,776030790189973524,667161053150445572,435067826483494934,400007985000087572,638410936457101315,430842153048997901,109060495348092928,685461041215307796]

s4vibot = commands.Bot(command_prefix='>')
s4vibot.remove_command('help')

@s4vibot.listen()
async def on_message(message):
    await AntiScam(message, bot = s4vibot, whitelist = whitelist_s4vi, muted_role='Muted', verified_role='Verificado', logs_channel=884844932307763310)

s4vibot.run('ODcxODg5MjgyNjUzMTA2MjE3.YQh4Kw.t7WiaYgY-3_uBRkWVE3O1g85Yv4')