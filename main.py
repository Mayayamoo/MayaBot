import discord
import os
import random
from discord.ext import commands
from keepalive import keep_alive
from discord.ext.commands import Cog
from lib.db import db

client = commands.Bot(command_prefix=".")




@client.command()
async def maya(ctx):
    await ctx.send('Maya is sooo cool and sexy!')
    await ctx.send('<a:SkirtDance:824068380985917471>')


@client.command()
async def based(ctx):
    await ctx.send(
        'https://cdn.discordapp.com/attachments/441778432767164427/765875762657886218/HELLO_BASED_DEPARTMENT.mp4'
    )


@client.command()
async def youre(ctx):
    await ctx.send('https://tenor.com/boGte.gif')


@client.command()
async def bitches(ctx):
    await ctx.send('get some bitches')


@client.command()
async def luh(ctx):
    await ctx.send('do you luh black people?')


@client.command()
async def houngry(ctx):
    await ctx.send('who is houngry')


@client.command()
async def whoishoungry(ctx):
    await ctx.send('uhh ummm uhhh')
    await ctx.send('<:MonkaS:787173222872645662>')


@client.command()
async def liar(ctx):
    await ctx.send(
        'https://cdn.discordapp.com/attachments/787153421174046743/817418073958776892/What_a_weaselly_liar_dude._SOURCE_1.mp4'
    )


@client.command()
async def pronouns(ctx):
    embed = discord.Embed(title='Pronouns', colour=discord.Colour.red())
    embed.add_field(name='He/Him      :heart:', value=False, inline=False)
    embed.add_field(name='She/Her', value=':green_heart:', inline=False)
    embed.add_field(name='They/Them', value=':purple_heart:', inline=False)
    embed.add_field(name='Any/All', value=':blue_heart:', inline=False)
    embed.add_field(name='Ask', value=':yellow_heart:', inline=False)
    await ctx.send(embed=embed)


@client.command()
async def age(ctx):
    embed = discord.Embed(title='Age', colour=discord.Colour.red())
    embed.add_field(name='<18', value=':underage:', inline=False)
    embed.add_field(name='Boomer', value=':older_man:', inline=False)
    await ctx.send(embed=embed)


magic8 = [
    'No lol', 'thats funny', '...', 'just...keep on trying', 'it seems likely',
    'only if you beg', 'mmm ok', '100%', 'stop wasting my time',
    'im busy, come back later', 'of course! not', 'of course, duh',
    ' it is likely', 'no shot bucko', 'im a bot, how am i supposed to know',
    'sure, whatever', 'why do *you* want to know?'
]


@client.command()
async def m8b(ctx):
    lucky_num = random.randint(0, len(magic8) - 1)
    await ctx.send(magic8[lucky_num])


class Welcome(Cog):
    def __init__(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.cogs_ready.ready_up("welcome!")

    @Cog.listener()
    async def on_member_join(self, member):
        db.execute("INSERT INTO exp (UserID) VALUES (?)", member.id)
        await self.bot.get_channel(787172074039935036).send(
            f"whats up {member.mention}!, Remember to select your <#787169031018643476>"
        )

    @Cog.listener()
    async def on_member_leave(self, member):
        pass


def setup(bot):
    bot.add_cog(Welcome(bot))


keep_alive()
client.run(os.getenv('TOKEN'))
