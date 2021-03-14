import discord
import os

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    game = discord.Game('입퇴장 로그 확인')
    await client.change_presence(status=discord.Status.online, activity=game)
    print("봇이 온라인으로 변경되었습니다")

@client.event
async def on_member_join(member):
    await client.get_channel(820657549018660864).send(f"{member.mention} 입장함")

@client.event
async def on_member_remove(member):
    await client.get_channel(820657549018660864).send(f"**{member}** 퇴장함")

access_token = os.environ["BOT_TOKEN"]
client.run(access_token) 
