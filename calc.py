import discord
from discord.ext import commands

class Calc(commands.Cog):

    def __init__(self, client):
        self.client = client

    #commands
    @commands.command(aliases=['add'])
    async def Add(self, ctx, firstnum : int, secondnum : int):
        await ctx.send(f'{firstnum} + {secondnum} = {firstnum+secondnum}')

    @Add.error
    async def Add_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('**Usage:** !add <firstnumber> <secondnumber>')

    @commands.command(aliases=['subtract', 'sub', 'Sub'])
    async def Subtract(self, ctx, firstnum : int, secondnum : int):
        await ctx.send(f'{firstnum} - {secondnum} = {firstnum-secondnum}')

    @Subtract.error
    async def Subtract_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('**Usage:** !subtract <firstnumber> <secondnumber>')

    @commands.command(aliases=['multiply'])
    async def Multiply(self, ctx, firstnum : int, secondnum : int):
        await ctx.send(f'{firstnum} * {secondnum} = {firstnum*secondnum}')

    @Multiply.error
    async def Multiply_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('**Usage:** !multiply <firstnumber> <secondnumber>')

    @commands.command(aliases=['divide'])
    async def Divide(self, ctx, firstnum : int, secondnum : int):
        await ctx.send(f'{firstnum} / {secondnum} = {firstnum/secondnum}')

    @Divide.error
    async def Divide_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('**Usage:** !divide <firstnumber> <secondnumber>')

def setup(client):
    client.add_cog(Calc(client))
