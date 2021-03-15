import discord
import asyncio
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
    embed = discord.Embed(title="[서버 입장 로그]", description=f"{member.mention} 님께서 입장하셨습니다", color=0x62c1cc)
    embed.add_field(name="[ 뉴비 인증 안내 ]", value="?????", inline=False)
    embed.set_footer(text=f"{member}")
    await client.get_channel(820657549018660864).send(embed=embed)

@client.event
async def on_member_remove(member):
    embed = discord.Embed(title="[서버 퇴장 로그]", description=f"**{member}** 님께서 퇴장하셨습니다", color=0x62c1cc)
    await client.get_channel(820657549018660864).send(embed=embed)

@client.event
async def on_message(message):
    if message.content.startswith("!on"):
        try:
            if message.author.guild_permissions.manage_messages:
                await message.channel.send("@everyone")
                embed = discord.Embed(title="[ FAST Server System ON ]", description="- 접속 후 서버 플레이에 지장이 있다면 DM 남겨주세요.", color=0x62c1cc)
                embed.add_field(name="[ Direct Address ]", value="connect cfx.re/join/m4ma39", inline=False)
                embed.add_field(name="[ KOREA FAST RP Server ]", value="- 24시간 ON 상태 입니다. 열심히 노력하는 FAST RP Server 가 되도록하겠습니다.", inline=False)
                await message.channel.send(embed=embed)
                await message.delete()
            else:
                await message.channel.send('```명령어 사용권한이 없습니다.```')
                await message.delete()
        except:
            pass

    if message.content.startswith("!re"):
        try:
            if message.author.guild_permissions.manage_messages:
                await message.channel.send("@everyone")
                embed = discord.Embed(title="[ FAST Server System REBOOT ]", description="-FAST RP 서버가 현재 리붓중입니다", color=0xFFE400)
                embed.add_field(name="[ Direct Address ]", value="connect cfx.re/join/m4ma39", inline=False)
                embed.add_field(name="[ KOREA FAST RP Server ]", value="- 24시간 ON 상태 입니다. 열심히 노력하는 FAST RP Server 가 되도록하겠습니다.", inline=False)
                await message.channel.send(embed=embed)
                await message.delete()
            else:
                await message.channel.send('```명령어 사용권한이 없습니다.```')
                await message.delete()
        except:
            pass
    if message.content.startswith("!off"):
        try:
            if message.author.guild_permissions.manage_messages:
                await message.channel.send("@everyone")
                embed = discord.Embed(title="[ FAST Server System OFF ]", description="- 현재 서버 문제 및 패치로 서버가 닫혔습니다. 오픈되면 들어와주세요", color=0xff0000)
                embed.add_field(name="[ Direct Address ]", value="connect cfx.re/join/m4ma39", inline=False)
                embed.add_field(name="[ KOREA FAST RP Server ]", value="- 24시간 ON 상태 입니다. 열심히 노력하는 FAST RP Server 가 되도록하겠습니다.", inline=False)
                await message.channel.send(embed=embed)
                await message.delete()
            else:
                await message.channel.send('```명령어 사용권한이 없습니다.```')
                await message.delete()
        except:
            pass

@client.event
async def on_message(message):
    if message.content.startswith('!클린'):
        try:
            # 메시지 관리 권한 있을시 사용가능
            if message.author.guild_permissions.manage_messages:
                amount = message.content[4:]
                await message.delete()
                await message.channel.purge(limit=int(amount))
                message = await message.channel.send(embed=discord.Embed(title='🧹' + str(amount) + '개의 메시지가 삭제되었습니다', colour=discord.Colour.green()))
                await asyncio.sleep(2)
                await message.delete()
            else:
                await message.channel.send('```명령어 사용권한이 없습니다.```')
        except:
            pass


access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
