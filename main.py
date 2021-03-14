import discord
import os

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_member_join(member):
    await client.get_channel(820657549018660864).send("어서오세요!")
          embed = discord.Embed(title="[서버 입장 로그]", description=f"{member.mention} 님께서 입장하셨습니다", color=0x62c1cc)
          embed.add_field(name="[ 뉴비 인증 안내 ]", value="?????", inline=False)
          await message.channel.send(embed=embed)

@client.event
async def on_member_remove(member):
    await client.get_channel(820657549018660864).send(f"**{member}** 퇴장함")

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
