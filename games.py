import discord
import random
from discord.ext import commands

class Games(commands.Cog):

    def __init__(self, client):
        self.client = client

    #commands
    @commands.command(aliases=['8'])
    async def _8ball(self, ctx, *, question):
        responses8ball = ['It is certain.', 'For sure', 'Without a doubt', 'Yes definitely', 'Chances are low', 'Wouldnt count on it.', 'Nope', 'Try again']
        await ctx.send(f"**Question:** {question}\n**Answer:** {random.choice(responses8ball)}")

    @commands.command(aliases=['flip'])
    async def Flip(self, ctx):
        responsesflip = ['_flips a coin and its TAILS_', '_flips a coin and its HEADS_']
        await ctx.send(f"{random.choice(responsesflip)}")

    @commands.command(aliases=['roll'])
    async def Roll(self, ctx):
        responsesroll = ['1', '2', '3', '4', '5', '6']
        await ctx.send(f":game_die:Rolled A Dice: {random.choice(responsesroll)}:game_die:")

    @commands.command()
    async def rps(self, ctx, option):
        response = [f'{ctx.author.mention}, My awnser is: :page_facing_up:!', f'{ctx.author.mention}, My awnser is: :moyai:!', f'{ctx.author.mention}, My awnser is: :scissors:!']
        await ctx.send(f"{random.choice(response)}")

def setup(client):
    client.add_cog(Games(client))
