import discord
from discord.ext import commands

class Links(commands.Cog):

    def __init__(self, client):
        self.client = client

    #commands
    @commands.command(aliases=['links'])
    async def Links(self, ctx):
        await ctx.send('**ArticMetroSystem Links:**\n**IP:** articmetrosystem.com\n**Website:** https://articmetrosystem.com\n**Map:** https://articmetrosystem.com/map\n**Rules:** https://articmetrosystem.com/rules\n**Status:** https://status.articmetrosystem.com')

    @commands.command(aliases=['ip', 'Ip'])
    async def IP(self, ctx):
        await ctx.send('**IP:**\narticmetrosystem.com')

    @commands.command(aliases=['website', 'web', 'Web'])
    async def Website(self, ctx):
        await ctx.send('**Website:**\nhttps://articmetrosystem.com')

    @commands.command(aliases=['map'])
    async def Map(self, ctx):
        await ctx.send('**Map:**\nhttps://articmetrosystem.com/map')

    @commands.command(aliases=['rules'])
    async def Rules(self, ctx):
        await ctx.send('**Rules:**\nhttps://articmetrosystem.com/rules')

    @commands.command(aliases=['status'])
    async def Status(self, ctx):
        await ctx.send('**Status:**\nhttps://status.articmetrosystem.com')

def setup(client):
    client.add_cog(Links(client))
