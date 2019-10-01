import discord
from discord.ext import commands

class Support(commands.Cog):

    def __init__(self, client):
        self.client = client

    #commands
    @commands.command()
    async def nick(ctx, ign, nickname):
        notifychannel = self.client.get_channel(628338403276226591)

        nickembed=discord.Embed(title=f"{ctx.author}", description="Change the Users Nickname", color=0x009191)
        nickembed.set_author(name=f"Nickname Change Request", icon_url=f"{ctx.author.avatar_url}")
        nickembed.add_field(name='**Player:**', value=f'{ctx.author}', inline=False)
        nickembed.add_field(name='**Current IGN:**', value=f'{ign}', inline=False)
        nickembed.add_field(name='**Nickname:**', value=f'{nickname}', inline=False)

        await notifychannel.send(embed=nickembed)

def setup(client):
    client.add_cog(Support(client))
