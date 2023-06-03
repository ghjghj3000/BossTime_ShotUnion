import asyncio

import discord

import datetime

import threading

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
channel = client.get_channel(1114405355741528124) #****보낼 채널 ID****

gigamTime = datetime.datetime.now()+datetime.timedelta(days=365)
gudeTime= datetime.datetime.now()+datetime.timedelta(days=365)
ifTime= datetime.datetime.now()+datetime.timedelta(days=365)
pinyxTime= datetime.datetime.now()+datetime.timedelta(days=365)
mayoTime= datetime.datetime.now()+datetime.timedelta(days=365)
dehugTime= datetime.datetime.now()+datetime.timedelta(days=365)
sedeTime= datetime.datetime.now()+datetime.timedelta(days=365)
sede2Time= datetime.datetime.now()+datetime.timedelta(days=365)
jungdeTime= datetime.datetime.now()+datetime.timedelta(days=365)
dongdeTime= datetime.datetime.now()+datetime.timedelta(days=365)
arTime= datetime.datetime.now()+datetime.timedelta(days=365)
jakTime= datetime.datetime.now()+datetime.timedelta(days=365)
kapaTime= datetime.datetime.now()+datetime.timedelta(days=365)
warmTime= datetime.datetime.now()+datetime.timedelta(days=365)
deathTime= datetime.datetime.now()+datetime.timedelta(days=365)
curchTime= datetime.datetime.now()+datetime.timedelta(days=365)
greenTime= datetime.datetime.now()+datetime.timedelta(days=365)
redTime= datetime.datetime.now()+datetime.timedelta(days=365)
sanduTime= datetime.datetime.now()+datetime.timedelta(days=365)

tmp_gigamTime = datetime.datetime.now()+datetime.timedelta(days=365)
tmp_gudeTime= datetime.datetime.now()+datetime.timedelta(days=365)
tmp_ifTime= datetime.datetime.now()+datetime.timedelta(days=365)
tmp_pinyxTime= datetime.datetime.now()+datetime.timedelta(days=365)
tmp_mayoTime= datetime.datetime.now()+datetime.timedelta(days=365)
tmp_dehugTime= datetime.datetime.now()+datetime.timedelta(days=365)
tmp_sedeTime= datetime.datetime.now()+datetime.timedelta(days=365)
tmp_sede2Time= datetime.datetime.now()+datetime.timedelta(days=365)
tmp_jungdeTime= datetime.datetime.now()+datetime.timedelta(days=365)
tmp_dongdeTime= datetime.datetime.now()+datetime.timedelta(days=365)
tmp_arTime= datetime.datetime.now()+datetime.timedelta(days=365)
tmp_jakTime= datetime.datetime.now()+datetime.timedelta(days=365)
tmp_kapaTime= datetime.datetime.now()+datetime.timedelta(days=365)
tmp_warmTime= datetime.datetime.now()+datetime.timedelta(days=365)
tmp_deathTime= datetime.datetime.now()+datetime.timedelta(days=365)
tmp_curchTime= datetime.datetime.now()+datetime.timedelta(days=365)
tmp_greenTime= datetime.datetime.now()+datetime.timedelta(days=365)
tmp_redTime= datetime.datetime.now()+datetime.timedelta(days=365)
tmp_sanduTime= datetime.datetime.now()+datetime.timedelta(days=365)

gigamTimeString = '99:99:99'
gudeTimeString = '99:99:99'
ifTimeString = '99:99:99'
mayoTimeString = '99:99:99'
pinyxTimeString = '99:99:99'
dehugTimeString = '99:99:99'
sedeTimeString = '99:99:99'
sede2TimeString = '99:99:99'
jungdeTimeString = '99:99:99'
dongdeTimeString = '99:99:99'
arTimeString = '99:99:99'
jakTimeString = '99:99:99'
kapaTimeString = '99:99:99'
warmTimeString = '99:99:99'
deathTimeString = '99:99:99'
curchTimeString = '99:99:99'
greenTimeString = '99:99:99'
redTimeString = '99:99:99'
sanduTimeString = '99:99:99'

tmp_gigamTimeString = ''
tmp_gudeTimeString = ''
tmp_ifTimeString = ''
tmp_mayoTimeString = ''
tmp_pinyxTimeString = ''
tmp_dehugTimeString = ''
tmp_sedeTimeString = ''
tmp_sede2TimeString = ''
tmp_jungdeTimeString = ''
tmp_dongdeTimeString = ''
tmp_arTimeString = ''
tmp_jakTimeString = ''
tmp_kapaTimeString = ''
tmp_warmTimeString = ''
tmp_deathTimeString = ''
tmp_curchTimeString = ''
tmp_greenTimeString = ''
tmp_redTimeString = ''
tmp_sanduTimeString = ''

gigamFlag = False
gudeFlag = False
ifFlag = False
mayoFlag = False
pinyxFlag = False
dehugFlag = False
sedeFlag = False
sede2Flag = False
jungdeFlag = False
dongdeFlag = False
arFlag = False
jakFlag = False
kapaFlag = False
warmFlag = False
deathFlag = False
curchFlag = False
greenFlag = False
redFlag = False
sanduFlag = False

nowTimeString = '1'

# 1-6에서 생성된 토큰을 이곳에 입력해주세요.
token = 'MTExMjYyNjA3NTM0OTA0MTE3Mw.GKePVu.giiGHFeri80ltQVVAZNYXxehIYyqcXr5_ygEgo'

#channel = client.get_channel(1112656268826525807) #****보낼 채널 ID****

async def my_background_task():
    await client.wait_until_ready()

    global channel
    global nowTimeString

    global gigamTime
    global gudeTime
    global ifTime
    global mayoTime
    global pinyxTime
    global dehugTime
    global sedeTime
    global sede2Time
    global jungdeTime
    
    global gigamTimeString
    global gudeTimeString
    global ifTimeString
    global mayoTimeString
    global pinyxTimeString
    global dehugTimeString
    global sedeTimeString
    global sede2TimeString
    global jungdeTimeString

    global tmp_gigamTimeString
    global tmp_gudeTimeString
    global tmp_ifTimeString
    global tmp_mayoTimeString
    global tmp_pinyxTimeString
    global tmp_dehugTimeString
    global tmp_sedeTimeString
    global tmp_sede2TimeString
    global tmp_jungdeTimeString


    global gigamFlag
    global gudeFlag
    global ifFlag
    global mayoFlag
    global pinyxFlag
    global dehugFlag
    global sedeFlag
    global sede2Flag
    global jungdeFlag

    while not client._closed:
        now = datetime.datetime.now()
        priv = now+datetime.timedelta(minutes=1)
        privTimeString = priv.strftime('%H:%M:%S')
        nowTimeString = now.strftime('%H:%M:%S')
        print('loop channeleck ' + gigamTime.strftime('%H:%M:%S') + ' ' + nowTimeString + ' ' + privTimeString)

        if channel != '':

            if gigamTime <= now:
                gigamFlag = False
                tmp_gigamTime = gigamTime
                gigamTimeString = '99:99:99'
                gigamTime = now+datetime.timedelta(days=365)
                embed = discord.Embed(description = '젠) 화탕지옥', color = 0x8258FA)
                await channel.send(embed = embed)                
                
            if gudeTime <= now:
                gudeFlag = False
                tmp_gudeTime = gudeTime
                gudeTimeString = '99:99:99'
                gudeTime = now+datetime.timedelta(days=365)
                embed = discord.Embed(description = '젠) 폭 화탕지옥', color = 0x8258FA)
                await channel.send(embed = embed)

            if ifTime <= now:
                ifFlag = False
                tmp_ifTime = ifTime
                ifTimeString = '99:99:99'
                ifTime = now+datetime.timedelta(days=365)
                embed = discord.Embed(description = '젠) 한빙지옥', color = 0x8258FA)
                await channel.send(embed = embed)

            if mayoTime <= now:
                mayoFlag = False
                tmp_mayoTime = mayoTime
                mayoTimeString = '99:99:99'
                mayoTime = now+datetime.timedelta(days=365)
                embed = discord.Embed(description = '젠) 폭 한빙지옥', color = 0x8258FA)
                await channel.send(embed = embed)

            if pinyxTime <= now:
                pinyxFlag = False
                tmp_pinyxTime = pinyxTime
                pinyxTimeString = '99:99:99'
                pinyxTime = now+datetime.timedelta(days=365)
                embed = discord.Embed(description = '젠) 거해지옥', color = 0x8258FA)
                await channel.send(embed = embed)

            if dehugTime <= now:
                dehugFlag = False
                tmp_dehugTime = dehugTime
                dehugTimeString = '99:99:99'
                dehugTime = now+datetime.timedelta(days=365)
                embed = discord.Embed(description = '젠) 폭 거해지옥', color = 0x8258FA)
                await channel.send(embed = embed)

            if sedeTime <= now:
                sedeFlag = False
                tmp_sedeTime = sedeTime
                sedeTimeString = '99:99:99'
                sedeTime = now+datetime.timedelta(days=365)
                embed = discord.Embed(description = '젠) 폭 중앙장군', color = 0x8258FA)
                await channel.send(embed = embed)

            if sede2Time <= now:
                sede2Flag = False
                tmp_sede2Time = sede2Time
                sede2TimeString = '99:99:99'
                sede2Time = now+datetime.timedelta(days=365)
                embed = discord.Embed(description = '젠) 폭 북장군', color = 0x8258FA)
                await channel.send(embed = embed)

            if gigamTime <= priv:
                if gigamFlag == False:
                    gigamFlag = True
                    await channel.send( '>>화탕지옥 1분 전 입니다<<')
                
            if gudeTime <= priv:
                if gudeFlag == False:
                    gudeFlag = True
                    await channel.send( '>>폭 화탕지옥 1분 전 입니다<<')

            if ifTime <= priv:
                if ifFlag == False:
                    ifFlag = True
                    await channel.send( '>>한빙지옥 1분 전 입니다<<')

            if mayoTime <= priv:
                if mayoFlag == False:
                    mayoFlag = True
                    await channel.send( '>>폭 한빙지옥 1분 전 입니다<<')

            if pinyxTime <= priv:
                if pinyxFlag == False:
                    pinyxFlag = True
                    await channel.send( '>>거해지옥 1분 전 입니다<<')

            if dehugTime <= priv:
                if dehugFlag == False:
                    dehugFlag = True
                    await channel.send( '>>폭 거해지옥 1분 전 입니다<<')

            if sedeTime <= priv:
                if sedeFlag == False:
                    sedeFlag = True
                    await channel.send( '>>폭 중앙장군 1분 전 입니다<<')

            if sede2Time <= priv:
                if sede2Flag == False:
                    sede2Flag = True
                    await channel.send( '>>폭 북장군 1분 전 입니다<<')

            
        await asyncio.sleep(1) # task runs every 60 seconds
        

# async def joinVoicechannelannel():
#     channel = client.get_channelannel("일반")
#     await client.join_voice_channelannel(channelannel)
    

# 봇이 구동되었을 때 동작되는 코드입니다
@client.event
async def on_ready():
    print("Logged in as ") #화면에 봇의 아이디, 닉네임이 출력됩니다
    print(client.user.name)
    print(client.user.id)
    print("===========")

    #await joinVoicechannelannel()
    
    client.loop.create_task(my_background_task())
    
    # 디스코드에는 현재 본인이 어떤 게임을 플레이하는지 보여주는 기능이 있습니다
    # 이 기능을 사용하여 봇의 상태를 간단하게 출력해줄 수 있습니다
    # await client.channelange_presence(game=discord.Game(name="반갑습니다 :D", type=1))

    

# 봇이 새로운 메시지를 수신했을때 동작되는 코드입니다
@client.event
async def on_message(message):
    if message.author.bot: #만약 메시지를 보낸사람이 봇일 경우에는
        return None #동작하지 않고 무시합니다

    global channel
    global client
    global nowTimeString

    global gigamTime
    global gudeTime
    global ifTime
    global mayoTime
    global pinyxTime
    global dehugTime
    global sedeTime
    global sede2Time

    global gigamTimeString
    global gudeTimeString
    global ifTimeString
    global mayoTimeString
    global pinyxTimeString
    global dehugTimeString
    global sedeTimeString
    global sede2TimeString

    global tmp_gigamTimeString
    global tmp_gudeTimeString
    global tmp_ifTimeString
    global tmp_mayoTimeString
    global tmp_pinyxTimeString
    global tmp_dehugTimeString
    global tmp_sedeTimeString
    global tmp_sede2TimeString

    global gigamFlag
    global gudeFlag
    global ifFlag
    global mayoFlag
    global pinyxFlag
    global dehugFlag
    global sedeFlag
    global sede2Flag

    id = message.author.id #id라는 변수에는 메시지를 보낸사람의 ID를 담습니다
    channel = client.get_channel(1114405355741528124) #****보낼 채널 ID****
    modify = ''
    try:
        hello = message.content
        length = len(hello)     # UTF-8로 인코딩 했을 때 바이트 수를 구함
        print(hello)
        print(length)
    
        if length == 11:
            hours = hello[6:8]
            minutes = hello[9:11]
            now = datetime.datetime.now()
            now = now.replace(hour=int(hours), minute=int(minutes))
        elif length == 12:
            hours = hello[7:9]
            minutes = hello[10:12]
            now = datetime.datetime.now()
            now = now.replace(hour=int(hours), minute=int(minutes))
        elif length == 10:
            hours = hello[5:7]
            minutes = hello[8:10]
            now = datetime.datetime.now()
            now = now.replace(hour=int(hours), minute=int(minutes))
        else :
            now = datetime.datetime.now()
            nowTimeString = now.strftime('%H:%M:%S')
    except:
        print('exception')
        now = datetime.datetime.now()
        nowTimeString = now.strftime('%H:%M:%S')


    if message.content.startswith('!화탕지옥 컷'):
        gigamFlag = False
        gigamTime = nextTime = now+datetime.timedelta(hours=4)
        tmp_gigamTimeString = gigamTimeString = nextTime.strftime('%H:%M:%S')
        await channel.send( '(다음 화탕지옥 ' + gigamTimeString +' )' )
        
    if message.content.startswith('!폭 화탕지옥 컷'):
        gudeFlag = False
        gudeTime = nextTime = now+datetime.timedelta(hours=4)
        tmp_gudeTimeString = gudeTimeString = nextTime.strftime('%H:%M:%S')
        await channel.send( '(다음 폭 화탕지옥 ' + gudeTimeString +' )')

    if message.content.startswith('!한빙지옥 컷'):
        ifFlag = False
        ifTime = nextTime = now+datetime.timedelta(hours=4)
        tmp_ifTimeString = ifTimeString = nextTime.strftime('%H:%M:%S')
        await channel.send( '(다음 한빙지옥 ' + ifTimeString +' )')

    if message.content.startswith('!폭 한빙지옥 컷'):
        mayoFlag = False
        mayoTime = nextTime = now+datetime.timedelta(hours=4)
        tmp_mayoTimeString = mayoTimeString = nextTime.strftime('%H:%M:%S')
        await channel.send( '(다음 폭 한빙지옥 ' + mayoTimeString +' )')

    if message.content.startswith('!거해지옥 컷'):
        pinyxFlag = False
        pinyxTime = nextTime = now+datetime.timedelta(hours=4)
        tmp_pinyxTimeString = pinyxTimeString = nextTime.strftime('%H:%M:%S')
        await channel.send( '(다음 거해지옥 ' + pinyxTimeString +' )')

    if message.content.startswith('!폭 거해지옥 컷'):
        dehugFlag = False
        dehugTime = nextTime = now+datetime.timedelta(hours=4)
        tmp_dehugTimeString = dehugTimeString = nextTime.strftime('%H:%M:%S')
        await channel.send( '(다음 폭 거해지옥 ' + dehugTimeString +' )')

    if message.content.startswith('!폭 중앙장군 컷'):
        sedeFlag = False
        sedeTime = nextTime = now+datetime.timedelta(hours=3)
        tmp_sedeTimeString = sedeTimeString = nextTime.strftime('%H:%M:%S')
        await channel.send( '(다음 폭 중앙장군 ' + sedeTimeString +' )')

    if message.content.startswith('!폭 북장군 컷'):
        sede2Flag = False
        sede2Time = nextTime = now+datetime.timedelta(hours=3)
        tmp_sede2TimeString = sede2TimeString = nextTime.strftime('%H:%M:%S')
        await channel.send( '(다음 폭 북장군 ' + sede2TimeString +' )')


    if message.content.startswith('!화탕지옥 젠'):
        gigamFlag = False
        gigamTime = nextTime = now
        tmp_gigamTimeString = gigamTimeString = nextTime.strftime('%H:%M:%S')
        await channel.send( '(다음 화탕지옥 ' + gigamTimeString +' )')
        
    if message.content.startswith('!폭 화탕지옥 젠'):
        gudeFlag = False
        gudeTime = nextTime = now
        tmp_gudeTimeString = gudeTimeString = nextTime.strftime('%H:%M:%S')
        await channel.send( '(다음 폭 화탕지옥 ' + gudeTimeString +' )')

    if message.content.startswith('!한빙지옥 젠'):
        ifFlag = False
        ifTime = nextTime = now
        tmp_ifTimeString = ifTimeString = nextTime.strftime('%H:%M:%S')
        await channel.send( '(다음 한빙지옥 ' + ifTimeString +' )')

    if message.content.startswith('!폭 한빙지옥 젠'):
        mayoFlag = False
        mayoTime = nextTime = now
        tmp_mayoTimeString = mayoTimeString = nextTime.strftime('%H:%M:%S')
        await channel.send( '(다음 폭 한빙지옥 ' + mayoTimeString +' )')

    if message.content.startswith('!거해지옥 젠'):
        pinyxFlag = False
        pinyxTime = nextTime = now
        tmp_pinyxTimeString = pinyxTimeString = nextTime.strftime('%H:%M:%S')
        await channel.send( '(다음 거해지옥 ' + pinyxTimeString +' )')

    if message.content.startswith('!폭 거해지옥 젠'):
        dehugFlag = False
        dehugTime = nextTime = now
        tmp_dehugTimeString = dehugTimeString = nextTime.strftime('%H:%M:%S')
        await channel.send( '(다음 폭 거해지옥 ' + dehugTimeString +' )')

    if message.content.startswith('!폭 중앙장군 젠'):
        sedeFlag = False
        sedeTime = nextTime = now
        tmp_sedeTimeString = sedeTimeString = nextTime.strftime('%H:%M:%S')
        await channel.send( '(다음 폭 중앙장군 ' + sedeTimeString +' )')

    if message.content.startswith('!폭 북장군 젠'):
        sede2Flag = False
        sede2Time = nextTime = now
        tmp_sede2TimeString = sede2TimeString = nextTime.strftime('%H:%M:%S')
        await channel.send( '(다음 폭 북장군 ' + sede2TimeString +' )')


    try:
        if message.content.startswith('!폭 화탕지옥 멍'):
            gudeFlag = False
            now = tmp_gudeTime
            gudeTime = nextTime = now+datetime.timedelta(hours=4)
            gudeTimeString = gudeTime.strftime('%H:%M:%S')
            await channel.send( '(다음 폭 화탕지옥 ' + gudeTimeString +' )')

        if message.content.startswith('!한빙지옥 멍'):
            ifFlag = False
            now = tmp_ifTime
            ifTime = nextTime = now+datetime.timedelta(hours=4)
            ifTimeString = ifTime.strftime('%H:%M:%S')
            await channel.send( '(다음 한빙지옥 ' + ifTimeString +' )')

        if message.content.startswith('!폭 한빙지옥 멍'):
            mayoFlag = False
            now = tmp_mayoTime
            mayoTime = nextTime = now+datetime.timedelta(hours=4)
            mayoTimeString = mayoTime.strftime('%H:%M:%S')
            await channel.send( '(다음 폭 한빙지옥 ' + mayoTimeString +' )')

        if message.content.startswith('!거해지옥 멍'):
            pinyxFlag = False
            now = tmp_pinyxTime
            pinyxTime = nextTime = now+datetime.timedelta(hours=4)
            pinyxTimeString = pinyxTime.strftime('%H:%M:%S')
            await channel.send( '(다음 거해지옥 ' + pinyxTimeString +' )')

    except:
        await channel.send( '입력 오류 ')



    if message.content.startswith('!불러오기'):
        file = open("C:\my_bot.db", 'r')
        
        while True:
            line = file.readline()
            
            if not line: break
            
            #await channel.send( line)
            
            if (line.startswith(' - 화탕지옥 : ')):
                hours = line[8:10]
                minutes = line[11:13]
                now2 = datetime.datetime.now()
                now2 = now.replace(hour=int(hours), minute=int(minutes))
                gigamTime = now2
                gigamTimeString = gigamTime.strftime('%H:%M:%S')

            if (line.startswith(' - 폭 화탕지옥 : ')):
                hours = line[8:10]
                minutes = line[11:13]
                now2 = datetime.datetime.now()
                now2 = now.replace(hour=int(hours), minute=int(minutes))
                gudeTime = now2
                gudeTimeString = gudeTime.strftime('%H:%M:%S')

            if (line.startswith(' - 한빙지옥 : ')):
                hours = line[8:10]
                minutes = line[11:13]
                now2 = datetime.datetime.now()
                now2 = now.replace(hour=int(hours), minute=int(minutes))
                ifTime = now2
                ifTimeString = ifTime.strftime('%H:%M:%S')

            if (line.startswith(' - 폭 한빙지옥 : ')):
                hours = line[8:10]
                minutes = line[11:13]
                now2 = datetime.datetime.now()
                now2 = now.replace(hour=int(hours), minute=int(minutes))
                mayoTime = now2
                mayoTimeString = mayoTime.strftime('%H:%M:%S')

            if (line.startswith(' - 거해지옥 : ')):
                hours = line[8:10]
                minutes = line[11:13]
                now2 = datetime.datetime.now()
                now2 = now.replace(hour=int(hours), minute=int(minutes))
                pinyxTime = now2
                pinyxTimeString = pinyxTime.strftime('%H:%M:%S')

            if (line.startswith(' - 폭 거해지옥 : ')):
                hours = line[8:10]
                minutes = line[11:13]
                now2 = datetime.datetime.now()
                now2 = now.replace(hour=int(hours), minute=int(minutes))
                dehugTime = now2
                dehugTimeString = dehugTime.strftime('%H:%M:%S')

            if (line.startswith(' - 폭 중앙장군 : ')):
                hours = line[9:11]
                minutes = line[12:14]
                now2 = datetime.datetime.now()
                now2 = now.replace(hour=int(hours), minute=int(minutes))
                sedeTime = now2
                sedeTimeString = sedeTime.strftime('%H:%M:%S')

            if (line.startswith(' - 폭 북장군 : ')):
                hours = line[9:11]
                minutes = line[12:14]
                now2 = datetime.datetime.now()
                now2 = now.replace(hour=int(hours), minute=int(minutes))
                sede2Time = now2
                sede2TimeString = sede2Time.strftime('%H:%M:%S')

                
        file.close()
        await channel.send( '불러오기 완료')
    

    if message.content.startswith('!보스탐'):

        datelist=[gigamTimeString, gudeTimeString, ifTimeString, mayoTimeString, pinyxTimeString, dehugTimeString,
                  sedeTimeString, sede2TimeString, jungdeTimeString,]

        information = '----- 보스탐 정보 -----\n'
        
        for timestring in sorted(datelist):
            #print(timestring)
        
            if timestring == gigamTimeString:
                if gigamTimeString != '99:99:99':
                    information += ' - 화탕지옥 : ' + gigamTimeString + '\n'

            elif timestring == gudeTimeString:
                if gudeTimeString != '99:99:99':
                    information += ' - 폭 화탕지옥 : ' + gudeTimeString + '\n'

            elif timestring == ifTimeString:     
                if ifTimeString != '99:99:99':
                    information += ' - 한빙지옥 : ' + ifTimeString + '\n'

            elif timestring == mayoTimeString:        
                if mayoTimeString != '99:99:99':
                    information += ' - 폭 한빙지옥 : ' + mayoTimeString + '\n'

            elif timestring == pinyxTimeString:        
                if pinyxTimeString != '99:99:99':
                    information += ' - 거해지옥 : ' + pinyxTimeString + '\n'

            elif timestring == dehugTimeString:       
                if dehugTimeString != '99:99:99':
                    information += ' - 폭 거해지옥 : ' + dehugTimeString + '\n'

            elif timestring == sedeTimeString:       
                if sedeTimeString != '99:99:99':
                    information += ' - 폭 중앙장군 : ' + sedeTimeString + '\n'
                    
            elif timestring == sede2TimeString:        
                if sede2TimeString != '99:99:99':
                    information += ' - 폭 북장군 : ' + sede2TimeString + '\n'


     
        if gigamTimeString == '99:99:99':
            information += ' - 화탕지옥 - 입력 안됨\n'
        if gudeTimeString == '99:99:99':
            information += ' - 폭 - 화탕지옥 입력 안됨\n'
        if ifTimeString == '99:99:99':
            information += ' - 한빙지옥 - 입력 안됨\n'
        if mayoTimeString == '99:99:99':
            information += ' - 폭 한빙지옥 - 입력 안됨\n'
        if pinyxTimeString == '99:99:99':
            information += ' - 거해지옥 - 입력 안됨\n'
        if dehugTimeString == '99:99:99':
            information += ' - 폭 거해지옥 - 입력 안됨\n'
        if sedeTimeString == '99:99:99':
            information += ' - 폭 중앙장군 - 입력 안됨\n'        
        if sede2TimeString == '99:99:99':
            information += ' - 폭 북장군 - 입력 안됨\n'

        await channel.send( information)

        file = open("c:\my_bot.db", 'w')
        file.write(information)
        file.close()

    if message.content.startswith('!현재시간'):
        await channel.send( datetime.datetime.now().strftime('%H:%M:%S'))

client.run(token)