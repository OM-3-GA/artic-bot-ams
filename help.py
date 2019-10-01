import discord
from discord.ext import commands

class Help(commands.Cog):

    def __init__(self, client):
        self.client = client

    #commands
    @commands.command(aliases=['help'])
    async def Help(self, ctx):

        helpembed1=discord.Embed(title="Page One", description="All Commands Start With: !", color=0x009191)
        helpembed1.set_author(name="ArticBOT Help", icon_url="https://cdn.discordapp.com/avatars/611650632016986112/e494a679ae9e591d346ca498649235aa.png?size=128")
        helpembed1.add_field(name='**Calculator:**', value='** **', inline=False)
        helpembed1.add_field(name='Subtract', value='Subtract Two Numbers!', inline=True)
        helpembed1.add_field(name='Multiply', value='Multiply Two Numbers!', inline=True)
        helpembed1.add_field(name='Divide', value='Divide Two Numbers!', inline=True)
        helpembed1.add_field(name='Add', value='Add Two Numbers!', inline=True)
        helpembed1.add_field(name='** **', value='** **', inline=True)
        helpembed1.add_field(name='** **', value='** **', inline=True)
        helpembed1.add_field(name='**Links:**', value='** **', inline=False)
        helpembed1.add_field(name='Links', value='View All Links!', inline=True)
        helpembed1.add_field(name='IP', value='Get The Servers IP!', inline=True)
        helpembed1.add_field(name='Website', value='The Servers Website!', inline=True)
        helpembed1.add_field(name='Rules', value='The Servers Rules!', inline=True)
        helpembed1.add_field(name='Map', value='The Servers Map!', inline=True)
        helpembed1.add_field(name='Status', value='The Servers Status Page!', inline=True)
        helpembed1.add_field(name='**Games:**', value='** **', inline=False)
        helpembed1.add_field(name='8', value='Ask The 8Ball A Question!', inline=True)
        helpembed1.add_field(name='Flip', value='Flip A Coin!', inline=True)
        helpembed1.add_field(name='Roll', value='Roll The Dice!', inline=True)
        helpembed1.set_footer(text="| ArticBOT | Version 1.0 | Developed by _O_M_3_G_A_#5296 |")

        helpembed2=discord.Embed(title="Page Two", description="All Commands Start With: !", color=0x009191)
        helpembed2.set_author(name="ArticBOT Help", icon_url="https://cdn.discordapp.com/avatars/611650632016986112/e494a679ae9e591d346ca498649235aa.png?size=128")
        helpembed2.add_field(name='**Voice:**', value='** **', inline=False)
        helpembed2.add_field(name='Join', value='Join the voice channel!', inline=True)
        helpembed2.add_field(name='Leave', value='Leave the voice channel!', inline=True)
        helpembed2.add_field(name='Play', value='Play Music (Must Be URL)!', inline=True)
        helpembed2.add_field(name='Pause', value='Pause the Music!', inline=True)
        helpembed2.add_field(name='Resume', value='Continue the Music!', inline=True)
        helpembed2.add_field(name='Stop', value='Stop playing the Music!', inline=True)
        helpembed2.add_field(name='Queue', value='Add Music to the Queue!', inline=True)
        helpembed2.add_field(name='Next', value='Next Song in the Queue!', inline=True)
        helpembed2.add_field(name='** **', value='** **', inline=True)
        helpembed2.add_field(name='**Status:**', value='** **', inline=False)
        helpembed2.add_field(name='Ping', value='Get the Latency of the Bot!', inline=True)
        helpembed2.add_field(name='Uptime', value='Get the bot uptime!', inline=True)
        helpembed2.add_field(name='** **', value='** **', inline=True)
        helpembed2.set_footer(text="| ArticBOT | Version 1.0 | Developed by _O_M_3_G_A_#5296 |")

        await ctx.author.send(embed=helpembed1)
        await ctx.author.send(embed=helpembed2)

    @commands.command(aliases=['staffhelp', 'Staffhelp', 'shelp'])
    async def StaffHelp(self, ctx):

        shelpembed=discord.Embed(title="Page One", description="All Commands Start With: !", color=0x009191)
        shelpembed.set_author(name="ArticBOT Staff Help", icon_url="https://cdn.discordapp.com/avatars/611650632016986112/e494a679ae9e591d346ca498649235aa.png?size=128")
        shelpembed.add_field(name='**Moderation:**', value='** **', inline=False)
        shelpembed.add_field(name='Clear', value='Clear an amount of Messages!', inline=True)
        shelpembed.add_field(name='**Notification:**', value='** **', inline=False)
        shelpembed.add_field(name='Promote', value='Notify the server of a members promotion!', inline=True)

        await ctx.author.send(embed=shelpembed)


def setup(client):
    client.add_cog(Help(client))
