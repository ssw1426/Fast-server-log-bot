import discord

client = discord.Client()
token = "ODE4NjQ0OTcyMTEwMDg2MTY0.YEbEiw.-Jh_BGdqL5ddim6q4LSMqIThxpU"

@client.event
async def on_ready():
    print("봇이 온라인으로 전환되었습니다.")

@client.event
async def on_message(message):
    if message.content.startswith("?on"):
        await message.channel.send("@everyone")
        embed = discord.Embed(title="서버 온 안내", description="저희 Next 서버는 최선을 다합니다", color=0x62c1cc)
        embed.add_field(name="다이렉트 주소", value="connect cfx.re/join/qrzma4", inline=False)
        await message.channel.send(embed=embed)
    if message.content.startswith("?r"):
        await message.channel.send("@everyone")
        embed = discord.Embed(title="서버 리붓 안내", description="서버 문제 및 패치로 서버리붓되었습니다", color=0x62c1cc)
        embed.add_field(name="서버 온 되면 들어와주세요", value="저희 Next 서버는 패치 및 버그에 최선를 다합니다", inline=False)
        await message.channel.send(embed=embed)
    if message.content.startswith("?off"):
        await message.channel.send("@everyone")
        embed = discord.Embed(title="서버 오프 안내", description="서버 문제 및 패치로 서버가 닫혔습니다", color=0xff0000)
        embed.add_field(name="서버 온 되면 들어와주세요", value="저희 Next 서버는 패치 및 버그에 최선를 다합니다", inline=False)
        await message.channel.send(embed=embed)

client.run(token)