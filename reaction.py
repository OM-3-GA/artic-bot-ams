import discord
from discord.ext import commands, tasks
from discord.utils import get
from itertools import cycle
import os
import youtube_dl
import shutil
from os import system

class Reaction(commands.Cog):

    def __init__(self, client):
        self.client = client

    #events
    @commands.Cog.listener #628316287373934611
    async def on_raw_reaction_add(self, payload):
        message_id = payload.message_id
        if message_id == 628316287373934611:
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)

            if payload.emoji.name == "exclamation_point":
                role = discord.utils.get(guild.roles, name="!")
            elif payload.emoji.name == "equals":
                role = discord.utils.get(guild.roles, name="=")
            elif payload.emoji.name == "minus":
                role = discord.utils.get(guild.roles, name="-")
            elif payload.emoji.name == "greater_than":
                role = discord.utils.get(guild.roles, name=">")
            elif payload.emoji.name == "slash":
                role = discord.utils.get(guild.roles, name="/")
            elif payload.emoji.name == "period":
                role = discord.utils.get(guild.roles, name=".")

            if role is not None:
                member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.add_roles(role)
                    print(f"Added {role.name} to {member}!")
                else:
                    print("Member not Found.")
            else:
                print("Role not Found.")

    @commands.Cog.listener #628316287373934611
    async def on_raw_reaction_remove(self, payload):
        message_id = payload.message_id
        if message_id == 628316287373934611:
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)

            if payload.emoji.name == "exclamation_point":
                role = discord.utils.get(guild.roles, name="!")
            elif payload.emoji.name == "equals":
                role = discord.utils.get(guild.roles, name="=")
            elif payload.emoji.name == "minus":
                role = discord.utils.get(guild.roles, name="-")
            elif payload.emoji.name == "greater_than":
                role = discord.utils.get(guild.roles, name=">")
            elif payload.emoji.name == "slash":
                role = discord.utils.get(guild.roles, name="/")
            elif payload.emoji.name == "period":
                role = discord.utils.get(guild.roles, name=".")

            if role is not None:
                member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.remove_roles(role)
                    print(f"Removed {role.name} from {member}!")
                else:
                    print("Member not Found.")
            else:
                print("Role not Found.")


def setup(client):
    client.add_cog(Reaction(client))
