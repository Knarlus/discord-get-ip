import discord

import KnarlusToken as KnToken

token = KnToken.get_token()

client = discord.Client()

if __name__ == "__main__":
    client.run(token)
