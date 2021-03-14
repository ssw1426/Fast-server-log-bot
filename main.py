import discord
import os

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_member_join(member):
    await client.get_channel(820657549018660864).send(f"{member.mention} 입장함")

@client.event
async def on_member_remove(member):
    await client.get_channel(820657549018660864).send(f"**{member}** 퇴장함")

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
