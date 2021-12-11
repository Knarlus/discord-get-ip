from discord.ext import commands
from discord_slash import SlashCommand  # pip install discord-py-slash-command

from KnarlusGetIp import get_ip
from KnarlusLogConsole import log_to_console
from KnarlusReadConfig import get_token, get_guild_ids


from datetime import datetime

token = get_token()

guild_ids = get_guild_ids()

bot = commands.Bot("¥")
slash = SlashCommand(bot)

last_ip = get_ip()
last_ip_time = datetime.now()


@bot.event
async def on_ready():
    log_to_console(log_msg=f"bot is logged in as {bot.user.name} (id {bot.user.id})", log_function_name="on_ready",
                   log_type="inf")
    for guild in bot.guilds:
        if guild.id in guild_ids:
            log_to_console(
                log_msg=f"bot is member of guild {guild.name} (id {guild.id}) and has the id already registered, \
therefore has slash commands enabled", log_function_name="on_ready", log_type="inf")
        else:
            log_to_console(
                log_msg=f"bot is member of guild {guild.name} (id {guild.id}) but not yet registered, enabling \
slash commands for this startup", log_function_name="on_ready", log_type="war")
            guild_ids.append(guild.id)


@slash.slash(name="ip", description="print the ipv4 to connect to the minecraft server", guild_ids=guild_ids, options=
[{"name": "force_reload", "description": "forces ip reload in case the program did use the last one, assuming it has \
not changed since the last request\n0 => no force (just like not giving this), any other number => force reload",
  "required": False, "type": 4}])
async def ip(ctx, force_reload: int = 0):
    global last_ip_time, last_ip
    if force_reload != 0 or (datetime.now() - last_ip_time).seconds > 3600:
        last_ip = get_ip()
        last_ip_time = datetime.now()
        await ctx.send(f"Hello {ctx.author.name}!\nThe current ip is `{last_ip}`.")
    else:
        await ctx.send(f"Hello {ctx.author.name}!\nThe current ip is `{last_ip}`.")


if __name__ == "__main__":
    bot.run(token)
