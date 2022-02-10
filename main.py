import discord
import os
import random
from discord.ext import commands
from keepalive import keep_alive
import json
from discord.ext.commands import Cog
from discord.ext.commands import command
from mybot.db import db
import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener

client = commands.Bot(command_prefix=".", intents=discord.Intents.all())
consumer_key = "YvopGZ7fUskZPhXsX34CkKTpx"
consumer_secret = "V3sdvQrzPNkISikC3nkuvGkUWWzcmPoyzfdsMCI0CsoVqiBmgK"

### tweet notifs wip
###
callback_uri = "oob"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret, callback_uri)
redirect_url = auth.get_authorization_url()


### member join and leave notif wip
@client.event
async def on_message_join(member):
    channel = client.get_channel(787172074039935036)
    await channel.send(f"Welcome to the Maya Cult {member.name}!")


### all of these are just cute little fun commands
###


@client.command()
async def hard(ctx):
    await ctx.send(
        "Imagine pretending to be hard when you're actually smashing your keyboard on the verge of tears BEGGING your friends on Discord to PLEASE RATIO THIS GUY ON TWITTER HE'S BULLYING ME :(((("
    )


@client.command()
async def banger(ctx):
    await ctx.send(
        "That was a fuckin' BANGER tweet, DON'T BE FRIENDS WTIH ME OR ORBIT ME IF YOU ARE THIS FUCKING SENSITIVE, I don't play into the lefty snowflake sensitive playground shit, go back to whatever twitter shithole you came from, loser"
    )


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
async def pronounrole(ctx, emoji, role: discord.Role):
    emb = discord.Embed(title='Pronouns', colour=discord.Colour.red())
    emb.add_field(name='He/Him', value=":heart:", inline=False)
    emb.add_field(name='She/Her', value=':green_heart:', inline=False)
    emb.add_field(name='They/Them', value=':purple_heart:', inline=False)
    emb.add_field(name='Any/All', value=':blue_heart:', inline=False)
    emb.add_field(name='Ask', value=':yellow_heart:', inline=False)
    msg = await ctx.channel.send(embed=emb)
    await msg.add_reaction(emoji)

    with open('reactrole.json') as json_file:
        data = json.load(json_file)

        new_react_role = {
            'role_name': role.name,
            'role_id': role.id,
            'emoji': emoji,
            'message_id': msg.id
        }
        data.append(new_react_role)
    with open('reactrole.json', 'w') as j:
        json.dump(data, j, indent=4)

class ReactionRolesNotSetup(commands.CommandError):
  """reaction roles are not set up"""
  pass
def is_setup():
  async def wrap_function(ctx):
    data = await ctx.bot.config.find(ctx.guild.id)
    if data is None:
      raise ReactionRolesNotSetup
    if data.get("message_id") is None:
      raise ReactionRolesNotSetup
    return True
  return commands.check(wrap_function)

class Reactions(commands.Cog, name="ReactionRoles"):
  def __init__(self,bot):
    self.bot=bot
  @commands.group(
    aliases=["rr"], invoke_without_command=True
  )
  @commands.guild_only()
  async def reactionroles(self, ctx):
    await ctx.invoke(self.bot.get_command("help"), entity="reactionroles")
def setup(bot):
  bot.add_cog(Reactions(bot))
@client.event
async def on_raw_reaction_add(payload):
    if payload.member.bot:
        pass
    else:
        with open('reactrole.json') as react_file:
            data = json.load(react_file)
            for x in data:
                if x['emoji'] == payload.emoji.name and x['message_id'] == payload.message_id:
                    role = discord.utils.get(client.get_guild(payload.guild_id).roles,id=x['role_id'])
                    await payload.member.add_roles(role)
@client.event
async def on_raw_reaction_remove(payload):
  with open('reactrole.json') as react_file:
      data = json.load(react_file)
      for x in data:
          if x['emoji'] == payload.emoji.name and x['message_id'] == payload.message_id:
              role = discord.utils.get(client.get_guild(payload.guild_id).roles, id=x['role_id'])
              await client.get_guild(payload.guild_id).get_member(payload.user_id).remove_roles(role)

#pronoun embed role



@client.command()
async def pings(ctx):
    embed = discord


@client.command()
async def age(ctx):
    embed = discord.Embed(title='Age', colour=discord.Colour.red())
    embed.add_field(name='<18', value=':underage:', inline=False)
    embed.add_field(name='Boomer', value=':older_man:', inline=False)
    await ctx.send(embed=embed)


### magic 8 ball code
###
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


keep_alive()
client.run(os.getenv('TOKEN'))
