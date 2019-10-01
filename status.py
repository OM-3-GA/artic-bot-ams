import discord, datetime, time
from discord.ext import commands

start_time = time.time()


class Support(commands.Cog):

    def __init__(self, client):
        self.client = client

    #Uptime
    @commands.command(pass_context=True)
    async def uptime(self, ctx):
        current_time = time.time()
        difference = int(round(current_time - start_time))
        text = str(datetime.timedelta(seconds=difference))
        embed = discord.Embed(colour=0x009191)
        embed.add_field(name="Uptime", value=text)
        embed.set_footer(text="| ArticBOT | Version 1.0 | Developed by _O_M_3_G_A_#5296 |")
        try:
            await ctx.send(embed=embed)
        except discord.HTTPException:
            await ctx.send("Current uptime: " + text)

    #Latency
    @commands.command(aliases=['ping', 'latency', 'Latency'])
    async def Ping(self, ctx):

        embed = discord.Embed(colour=0x009191)
        embed.add_field(name="Ping", value=f"{round(self.client.latency * 1000)}ms")
        embed.set_footer(text="| ArticBOT | Version 1.0 | Developed by _O_M_3_G_A_#5296 |")

        await ctx.send(embed=embed)

    @commands.command()
    async def invite(ctx):
        await ctx.author.send("Invite other players with: https://discord.gg/P2akC4g")

def setup(client):
    client.add_cog(Support(client))
