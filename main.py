import discord
import os

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    game = discord.Game('서버 입퇴장 기록')
    await client.change_presence(status=discord.Status.online, activity=game)
    print("봇이 온라인으로 변경되었습니다")

@client.event
async def on_member_join(member):
    embed = discord.Embed(title="[😀서버 입장 로그😀]", description=f"{member.mention} 님께서 LEGO 서버에 입장하셨습니다", color=0x62c1cc)
    embed.set_footer(text=f"{member}")
    await client.get_channel(820938809100337155).send(embed=embed)

@client.event
async def on_member_remove(member):
    embed = discord.Embed(title="[😓서버 퇴장 로그😓]", description=f"{member.mention} 님께서 LEGO 서버에서 퇴장하셨습니다", color=0x62c1cc)
    embed.set_footer(text=f"{member}")
    await client.get_channel(820938809100337155).send(embed=embed)

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
