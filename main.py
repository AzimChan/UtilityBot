import discord
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option

import time
import os
import asyncio
import codecs
import random

GUILD_IDS=[852858286779793479,939534579964973076]

bot = discord.ext.commands.Bot(command_prefix="/")
slash = SlashCommand(bot,sync_commands=True)

@bot.event
async def on_ready():
    print("Bot have been planted")

#session command
@slash.slash(
    name="session",
    description="creates game session",
    guild_ids=GUILD_IDS,
    options=[
        create_option(
            name="activity",
            description="Write down session activity",
            required=False,
            option_type=3,
            choices=[
                create_choice(
                    name="Minecraft",
                    value="Minecraft"
                ),
                create_choice(
                    name="Roblox",
                    value="Roblox"
                ),
                create_choice(
                    name="Valorant",
                    value="Valorant"
                )
            ]
        )
    ]
)
async def _session(ctx,activity="Chilling"):
    #activities
    if activity=="Roblox":
        thumb="https://pbs.twimg.com/profile_images/1131599526001692672/D40KVhLQ_400x400.png"
    elif activity=="Minecraft":
        thumb="https://www.minecraft.net/etc.clientlibs/minecraft/clientlibs/main/resources/img/minecraft-creeper-face.jpg"
    elif activity=="Valorant":
        thumb="https://inceptum-stor.icons8.com/eU4d89ZetaJy/Valorant.png"
    else:
        thumb="https://i.pinimg.com/564x/92/44/5a/92445a2b620b39da636552e2a999404b.jpg"
        
    info_ch=bot.get_channel(952173531150557275)
    voice_ch=bot.get_channel(947437258733133894)
    START_TIME=time.strftime("%X")

    await ctx.send("**Session have been created**\n[Click here to join](https://discord.gg/mccpGR9YeJ)")

    #session sending
    while True:
        punish_embed=discord.Embed(
            title=activity,
            description="Started at {0}".format(START_TIME),
            colour=discord.Colour.orange()
        )
        punish_embed.set_thumbnail(url=thumb)
        
        #members field
        punish_embed.add_field(name="Organizer:", value="•`"+ctx.author.name+"`", inline=True)    
        member_field = ""
        if voice_ch.voice_states.keys():
            for i in list(voice_ch.voice_states):
                member_field+=("•`"+(await bot.fetch_user(i)).name+"`\n")
        else:
            member_field+="•`Nobody`\n"
        punish_embed.add_field(name="Members:", value=member_field, inline=True)

        punish_embed.add_field(name="Lets chat together",value="[Click here to join](https://discord.gg/mccpGR9YeJ)",inline=False)
        try:
            await punishment.edit(embed=punish_embed)
        except:
            punishment = await info_ch.send(ctx.author.mention+"@her",embed=punish_embed)
        
        await asyncio.sleep(20)
        #close if nobody in vc
        if not list(voice_ch.voice_states):
            await punishment.delete()
            break


#motivation quotes command
#get quotes from txt
with codecs.open('eng_quotes.txt', 'r', "utf_8_sig") as reader:
    quotes_eng=list(map(lambda x: x.strip(),reader.readlines()))
with codecs.open('rus_quotes.txt', 'r', "utf_8_sig") as reader:
    quotes_rus=list(map(lambda x: x.strip(),reader.readlines()))
#command
@slash.slash(
    name="motivation",
    description="sends random motivational quotes",
    guild_ids=GUILD_IDS,
    options=[
        create_option(
            name="lang",
            description="Language of quote",
            required=False,
            option_type=3,
            choices=[
                create_choice(
                    name="rus",
                    value="rus"
                ),
                create_choice(
                    name="eng",
                    value="eng"
                ),
            ]
        )
    ]
)
async def _motivation(ctx,lang="eng"):
    if lang=="eng":
        await ctx.send(quotes_eng[random.randint(0,len(quotes_eng)-1)])
    else:
        await ctx.send(quotes_rus[random.randint(0,len(quotes_rus)-1)])


from keep_alive import keep_alive
keep_alive()
bot.run(os.getenv("TOKEN"))