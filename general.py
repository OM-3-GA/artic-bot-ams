import discord
from discord.ext import commands

class General(commands.Cog):

    def __init__(self, client):
        self.client = client

    #events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Cogs Are Loaded.')

    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f'{member} has joined the server.')
        visrole = discord.utils.get(member.guild.roles, name='Not Verified')
        await member.add_roles(visrole)
        print(f'{member} was given {visrole}!')
        joinleavechannel = self.client.get_channel(627828473888505856)
        await joinleavechannel.send(f':white_check_mark: {member.mention} ({member}) has joined the server!')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f'{member} has left a server.')
        joinleavechannel = self.client.get_channel(627828473888505856)
        await joinleavechannel.send(f':x: {member.mention} ({member}) has left the server!')


    #commands

def setup(client):
    client.add_cog(General(client))
