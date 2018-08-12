import discord
import asyncio
import random
import lolizinha
import requests
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont, ImageOps


client = discord.Client ()
Cor = 0x25C4E4
token =lolizinha.seu_token()
msg_id = None
msg_user = None

@client.event
async def on_ready() :
           print('BOT ONLINE Olá Mundo!')
           print(client.user.name)
           print(client.user.id)
           print('-xxxx-xxxx-xxxx-xxxx-')

@client.event
async def on_member_join(member):
    url = requests.get(member.avatar_url)
    canal = client.get_channel('445324651279679490')
    avatar = Image.open (BytesIO (url.content))
    avatar = avatar.resize ( (120 , 119) )
    bigavatar = (avatar.size[ 0 ] * 3 , avatar.size[ 1 ] * 3)
    mascara = Image.new ( 'L' , bigavatar , 0 )
    recortar = ImageDraw.Draw ( mascara )
    recortar.ellipse ( (0 , 0 ,) + bigavatar , fill=255 )
    mascara = mascara.resize ( avatar.size , Image.ANTIALIAS )
    avatar.putalpha ( mascara )

    saida = ImageOps.fit ( avatar , mascara.size , centering=(0.5 , 0.5) )
    saida.putalpha ( mascara )
    saida.save ( 'avatar.png' )

    img = Image.open ( 'bemvindo.png' )
    fonte = ImageFont.truetype ( 'BebasNeue.ttf' , 50 )
    escrever = ImageDraw.Draw ( img )
    escrever.text ( xy=(210 , 194) , text=member.name , fill=(0 , 0 , 0) , font=fonte )
    img.paste ( avatar , (12 , 126) , avatar )
    img.save('bv.png')
    await client.send_file(canal, 'bv.png')

@client.event
async def on_message(message):
       if message.content.lower().startswith('!moeda'):
           await client.send_message(message.channel, "Olá Mundo, estou vivo.")


@client.event
async def on_message (message):
       choice =random.randint(1,2)
       if choice == 1:
           await client.add_reaction(message, '😀')
       if choice == 2:
           await client.add_reaction(message, '👑')



@client.event
async def on_member_remove(member):
            canal = client.get_channel("445324651279679490")
            msg = "Vai Te Embora carniça, vai vai desgraçaa!{} ".format(member.mention)
            await client.send_message(canal, msg)

players = {}
COR = 0x25C4E4

@client.event

async def on_message(message):
     if message.content.startswith('!chegae'):
        try:
            channel = message.author.voice.voice_channel
            await client.join_voice_channel(channel)
        except discord.errors.InvalidArgument:
            await client.send_message(message.channel, "O bot ja esta em um canal de voz")
        except Exception as error:
            await client.send_message(message.channel, "Ein Error: ```{error}```".format(error=error))

     if message.content.startswith('!vaza'):
        try:
            mscleave = discord.Embed(
                title="\n",
                color=COR,
                description="Sai daqui meu!! Vaaza daqui!"
            )
            voice_client = client.voice_client_in(message.server)
            await client.send_message(message.channel, embed=mscleave)
            await voice_client.disconnect()
        except AttributeError:
            await client.send_message(message.channel, "Eita porra do caralho, Agora fudeu de vez!")
        except Exception as Hugo:
            await client.send_message(message.channel, "Ein Error: ```{haus}```".format(haus=Hugo))

     if message.content.startswith('!play'):
        try:
            yt_url = message.content[6:]
            if client.is_voice_connected(message.server):
               try:
                   voice = client.voice_client_in(message.server)
                   players[message.server.id].stop()
                   player = await voice.create_ytdl_player('ytsearch: {}'.format(yt_url))
                   players[message.server.id] = player
                   player.start()
                   mscemb = discord.Embed(
                       title="Bora toca saporra ae:",
                       color=COR
                   )
                   mscemb.add_field(name="Nome:", value="`{}`".format(player.title))
                   mscemb.add_field(name="Visualizações:", value="`{}`".format(player.views))
                   mscemb.add_field(name="Enviado em:", value="`{}`".format(player.uploaded_date))
                   mscemb.add_field(name="Enviado por:", value="`{}`".format(player.uploadeder))
                   mscemb.add_field(name="Duraçao:", value="`{}`".format(player.uploadeder))
                   mscemb.add_field(name="Likes:", value="`{}`".format(player.likes))
                   mscemb.add_field(name="Deslikes:", value="`{}`".format(player.dislikes))
                   await client.send_message(message.channel, embed=mscemb)
               except Exception as e:
                   await client.send_message(message.server, "Error: [{error}]".format(error=e))

            if not client.is_voice_connected(message.server):
               try:
                   channel = message.author.voice.voice_channel
                   voice = await client.join_voice_channel(channel)
                   player = await voice.create_ytdl_player('ytsearch: {}'.format(yt_url))
                   players[message.server.id] = player
                   player.start()
                   mscemb2 = discord.Embed(
                       title="Bora toca saporra ae",
                       color=COR
                   )
                   mscemb2.add_field(name="Nome:", value="`{}`".format(player.title))
                   mscemb2.add_field(name="Visualizações:", value="`{}`".format(player.views))
                   mscemb2.add_field(name="Enviado em:", value="`{}`".format(player.upload_date))
                   mscemb2.add_field(name="Enviado por:", value="`{}`".format(player.uploader))
                   mscemb2.add_field(name="Duraçao:", value="`{}`".format(player.duration))
                   mscemb2.add_field(name="Likes:", value="`{}`".format(player.likes))
                   mscemb2.add_field(name="Deslikes:", value="`{}`".format(player.dislikes))
                   await client.send_message(message.channel, embed=mscemb2)
               except Exception as error:
                   await client.send_message(message.channel, "Error: [{error}]".format(error=error))
        except Exception as e:
           await client.send_message(message.channel, "Error: [{error}]".format(error=e))

     if message.content.startswith('!pause'):
        try:
            mscpause = discord.Embed(
                    title="\n" ,
                    color=COR ,
                    description="FILHOO DA PUTA PARA COM ESSA PORRA AI MERMÃO!"
            )
            await client.send_message(message.channel,embed=mscpause)
            players[message.server.id].pause()
        except Exception as error:
            await client.send_message( message.channel, "Error: [{error}]".format(error=error))
     if message.content.startswith('!resume'):
        try:
            mscresume = discord.Embed (
                    title="\n" ,
                    color=COR ,
                    description="Toca sa porra ai"
                )
            await client.send_message ( message.channel , embed=mscresume )
            players[ message.server.id ].resume ( )
        except Exception as error:
            await client.send_message ( message.channel , "Error: [{error}]".format ( error=error ) )

client.run(token)
