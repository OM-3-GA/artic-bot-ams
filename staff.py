import discord
from discord.ext import commands

class Staff(commands.Cog):

    def __init__(self, client):
        self.client = client

    #commands
    @commands.command(aliases=['clear'])
    @commands.has_permissions(manage_messages=True)
    async def Clear(self, ctx, amount : int):
        await ctx.channel.purge(limit=1)
        await ctx.channel.purge(limit=amount)

    @Clear.error
    async def Clear_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please specify an amount of messages to clear!')

    #Kick
    @commands.command()
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        await member.kick(reason=reason)

    #Ban
    @commands.command()
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        await member.ban(reason=reason)

    #Unban
    @commands.command()
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                return

    @commands.command(aliases=['promote'])
    @commands.has_permissions(manage_messages=True)
    async def Promote(self, ctx, player, town, rank):
        await ctx.channel.purge(limit=1)
        notifychannel = self.client.get_channel(627863713780727849)
        await notifychannel.send(f"**{player}**'s town of **{town}** has been promoted to **{rank}**!")

    @Promote.error
    async def Promote_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('**Usage:** !promote <player> <town> <rank>')

    @commands.command(aliases=['citizen'])
    @commands.has_permissions(administrator=True)
    async def Citizen(self, ctx, member : discord.Member):
        citrole = discord.utils.get(member.guild.roles, name='Verified')
        await member.add_roles(citrole)
        print(f'{member} was given {citrole}!')
        visrole = discord.utils.get(member.guild.roles, name='Not Verified')
        await member.remove_roles(visrole)
        print(f'{member} was removed from {visrole}!')
        citchannel = self.client.get_channel(627863713780727849)
        await citchannel.send(f"**{member.mention}** has been promoted to **Citizen**!")
        await ctx.channel.purge(limit=1)

    @Citizen.error
    async def Citizen_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('**Usage:** !citizen <player>')

def setup(client):
    client.add_cog(Staff(client))
