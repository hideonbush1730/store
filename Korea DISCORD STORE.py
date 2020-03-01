import discord
import asyncio
import os

client = discord.Client()

@client.event
async def on_ready():
    print("ready")
    print(client.user.id)
    print(client.user.name)
    print('=====================================')
 
@client.event
async def on_message(message):
    if message.content.startswith('!판매'):
        embed=discord.Embed(title='', color=0x64FE2E,  timestamp=message.created_at)
        embed.add_field(name="판매알림", value=f'•—— 👑 프로필 1번 타입 👑 ——•\n\n\n👑 문화상품권 : 5천원\n\n\n👑 계좌 : 4천원\n\n\n👑 문의는 ! NICK#2727 개인dm 넣어주세요!\n\n👑 제작시간 :  10 ~ 15분\n(😅 개인 사정으로 30 ~ 45분 까지 지연될수 있습니다.)\n\n👑 제작후 색깔 및 글씨 색 변경은 1번 가능합니다.\n❗무단 복제시 법적 처벌 강력 대응하겠습니다.❗️', inline=True)
        embed.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
        await message.channel.send(embed=embed)
        await message.channel.send(message.content[4:])
    
    if message.content.startswith('$공지'):
        msg = message.content[4:]
        if message.author.id == 581396513108918295 or message.author.id == 527084544525074432:
            embed=discord.Embed(colour=0xB2EBF4, timestamp=message.created_at, title="공지")
            embed.add_field(name="E Y E N I X", value=msg, inline=True)
            embed.set_footer(text=f"오늘도 저희 E Y E N I X 에 방문해주셔서 감사합니다")
            for i in message.guild.members:
                if i.bot == True:
                    pass
                else:
                    await i.send(embed=embed)
        else:
            await message.channel.send('사용이 불가한 커맨드')
    if message.content == '!출근':
        if message.author.id ==527084544525074432 or message.author.id == 581396513108918295:
            embed=discord.Embed(title='정상 출근처리되셧습니다', color=0xff00, timestamp=message.created_at)
            embed.add_field(name="출.퇴근 알림", value=f'{message.author} 님이 출근하셧습니다.즐거운하루되세요!', inline=True)
            embed.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
            await message.channel.send(embed=embed)
        else:
            await message.channel.send('❌ 이런 존재하지않는 명령어또는 권한이없어요!')
    if message.content == '!퇴근':
        if message.author.id ==527084544525074432 or message.author.id == 581396513108918295:
            embed=discord.Embed(title='정상 퇴근처리 되셧습니다', color=0xFF0000, timestamp=message.created_at)
            embed.add_field(name="출.퇴근 알림", value=f'{message.author} 님이 퇴근하셧습니다.수고하셧습니다!.', inline=True)
            embed.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
            await message.channel.send(embed=embed)
        else:
            await message.channel.send('❌ 이런 존재하지않는 명령어또는 권한이없어요!')
    if message.content.startswith('!EYENIX'):
        author = message.guild.get_member(int(message.author.id))
        role = discord.utils.get(message.guild.roles, name="😁ㅣ손님ㅣ😁")
        await author.add_roles(role)
        await message.channel.send('인증이완료되었습니다')
            
async def my_background_task():
    await client.wait_until_ready()
    while not client.is_closed():
        game = discord.Game("벤츠서버 질문받는중")
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(5)
        game = discord.Game(f'{len(client.guilds)}개의 서버에 참여중')
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(5)
        game = discord.Game(f'{len(client.users)}명의 유저들과 소통하는중')
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(5)
client.loop.create_task(my_background_task())


access_token = os.environ["BOT_TOKEN"]        
client.run(access_token)
