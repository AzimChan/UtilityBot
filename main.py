import discord
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option

import time
import os
import asyncio

GUILD_IDS=[939534579964973076]

bot = discord.ext.commands.Bot(command_prefix="/")
slash = SlashCommand(bot,sync_commands=True)

@bot.event
async def on_ready():
    print("Bot have been planted")

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
    punish_embed=discord.Embed(
        title=activity,
        description="Started at {0}".format(START_TIME),
        colour=discord.Colour.orange()
    )
    punish_embed.set_thumbnail(url=thumb)
    punish_embed.add_field(name="Organizer:", value="•`"+ctx.author.name+"`", inline=True)
    
    member_field = ""
    if voice_ch.voice_states.keys():
        for i in list(voice_ch.voice_states):
            member_field+=("•`"+(await bot.fetch_user(i)).name+"`\n")
    else:
        member_field+="•`Nobody`\n"

    punish_embed.add_field(name="Members:", value=member_field, inline=True)
    punish_embed.add_field(name="Lets chat together",value="[Click here to join](https://discord.gg/mccpGR9YeJ)",inline=False)

    punishment = await info_ch.send(ctx.author.mention+"@here",embed=punish_embed)

    await ctx.send("**Session have been created**\n[Click here to join](https://discord.gg/mccpGR9YeJ)")

    while True:
        await asyncio.sleep(10)
        if voice_ch.voice_states.keys():
            new_embed=discord.Embed(
                title=activity,
                description="Started at {0}".format(START_TIME),
                colour=discord.Colour.orange()
            )
            new_embed.set_thumbnail(url=thumb)
            new_embed.add_field(name="Organizer:", value="•`"+ctx.author.name+"`", inline=True)

            member_field = ""
            if voice_ch.voice_states.keys():
                for i in list(voice_ch.voice_states):
                    member_field+=("•`"+(await bot.fetch_user(i)).name+"`\n")
            else:
                member_field+="•`Nobody`\n"

            new_embed.add_field(name="Members:", value=member_field, inline=True)
            new_embed.add_field(name="Lets chat together",value="[Click here to join](https://discord.gg/mccpGR9YeJ)",inline=False)
            await punishment.edit(embed=new_embed)
        else:
            await punishment.delete()


bot.run(os.getenv("TOKEN"))