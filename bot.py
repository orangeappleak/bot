import discord
import asyncio
import random
import json
import os

from discord.ext.commands import command
from discord import Game
from itertools import cycle
from discord import colour
from discord import Channel

bot_prefix=['++']
client=discord.ext.commands.Bot(command_prefix=bot_prefix)
client.remove_command('help')
TOKEN="NDYyODc1NjA4MDkxODUyODAw.DkIFAQ.nEFG9E6Wcp7BI0GmzneJH8t2_Cs"

@client.event#just for fun
async def on_message(msg):
    if msg.content.lower().startswith('you have to'):
        possibilities=['hey,i have my free will in this server and i cant be doing as you say okay','i have my freedom over here so........']
        await client.send_typing(msg.message.channel)
        await client.send_message(msg.channel,random.choice(possibilities))
    chat_filter=['fuck','fuck off','dick','bitch']
    msd=msg.content.split(" ")
    for word in msd:
        if word.lower() in chat_filter:
            await client.delete_message(msg)
            await client.send_typing(msg.message.channel)
            await client.send_message(msg.author,'hey you cant be using such type of words in this server punk')
    if msg.content.lower().startswith('?discord.py_documentation'):
        embed=discord.Embed(description='API Reference--->\nhttp://discordpy.readthedocs.io/en/latest/api.html',colour=discord.Colour.blue())
        await client.send_typing(msg.channel)
        await client.send_message(msg.channel,embed=embed)
    if msg.content.lower().startswith('?clash_royale_api'):
        await client.send_message(msg.channel,'https://docs.royaleapi.com/#/')
    await client.process_commands(msg)

@client.command(pass_context=True)
async def coinflip(ctx):
    await client.send_typing(ctx.message.channel)
    await client.say('whats youre call?')
    reply=await client.wait_for_message(channel=ctx.message.channel,author=ctx.message.author)
    poss=['tails','heads']
    await client.send_typing(ctx.message.channel)
    await client.say('okay flipping the coin')
    gif=discord.Embed(title='coinflip')
    url=['https://cdn.discordapp.com/attachments/455323478267133962/459233673510780938/Flipping-coin-animated.gif',
    'https://vignette.wikia.nocookie.net/glee/images/d/d5/281735_1342370254-coin-flip.gif.gif']
    gif.set_image(url=random.choice(url))
    await client.say(embed=gif)
    await asyncio.sleep(2.0)
    await client.send_typing(ctx.message.channel)
    final=await client.say('\n\n{}'.format(random.choice(poss)))
    if reply.content==final.content:
        await client.send_typing(ctx.message.channel)
        await client.say('looks like you won MR.{}'.format(ctx.message.author.mention))
    else:
        await client.send_typing(ctx.message.channel)
        await client.say('you lost it\ni am actually addicted towards winning{}'.format(ctx.message.author.mention))

@client.command(pass_context=True)
async def kiss(ctx,member:discord.Member):
    k=discord.Embed(description='hey {},{} gave you kiss'.format(member.mention,ctx.message.author.mention))
    kisses=['https://media.giphy.com/media/v4JbTGe4KJjKo/giphy.gif'
    ,'https://cdn.discordapp.com/attachments/455323478267133962/459237164916670464/tenor.gif']
    k.set_image(url=random.choice(kisses))
    await client.send_typing(ctx.message.channel)
    await client.say(embed=k)

@client.command(pass_context=True)#admin
async def admin(ctx):
    if 'admin' in (role.name for role in ctx.message.author.roles):
        await client.send_typing(ctx.message.channel)
        await client.say('yes you are an admin <@%s>' % ctx.message.author.id)
    else:
        await client.send_typing(ctx.message.channel)
        await client.say('sorry,but you are not an admin')

@client.command(aliases=['hi','hello','wassup','hey'],
pass_context=True)#greest a member back
async def greets(ctx):
    greetings=['hey','wassup','hello there','salutations','greetings','well my creator has socialized me,\n so hello there','i love to greet people,wassup']
    await client.send_typing(ctx.message.channel)
    await client.send_message(ctx.message.channel,random.choice(greetings) + "<@%s>" % ctx.message.author.id)

@client.command(pass_context=True)#tells info of the member
async def info(ctx,user:discord.Member):
    embed=discord.Embed(title='{}\'s info'.format(user.name),description='here\'s the information i can gather',colour=discord.Colour.orange())
    embed.add_field(name='name:',value=user.name,inline=False)
    embed.add_field(name='id:',value=user.id,inline=False)
    embed.add_field(name='status:',value=user.status,inline=False)
    embed.add_field(name='member of the server from:',value=user.joined_at,inline=False)
    embed.set_thumbnail(url=user.avatar_url)
    embed.set_footer(text='\nTHAT\'S ALL I CAN GATHER')
    await client.send_typing(ctx.message.channel)
    await client.send_message(ctx.message.author,embed=embed)

@client.command(pass_context=True)#deletes the messages
async def delete_messages(ctx):
    try:
        if 'admin' in (role.name for role in ctx.message.author.roles):
            await client.send_typing(ctx.message.channel)
            await client.say('gimme a sec')
            await client.purge_from(channel=ctx.message.channel,limit=1000)
            await client.send_typing(ctx.message.channel)
            await client.say('there you go <@%s>' % ctx.message.author.id)
        elif "admin" not in (role.name for role in ctx.message.author.roles):
            await client.send_typing(ctx.message.channel)
            await client.say('you have to be an admin in order to that')
    except:
        await client.say("`discord.ext.commands.errors.CommandInvokeError: Command raised an exception: HTTPException: BAD REQUEST (status code: 400): You can only bulk delete messages that are under 14 days old.`")

@client.command(pass_context=True)#kicks a member
async def kick(ctx,user:discord.Member):
    if 'admin' in (role.name for role in ctx.message.author.roles):
        await client.send_typing(ctx.message.channel)
        await client.say('as you say')
        try:
            await client.kick(user)
            await client.send_typing(ctx.message.channel)
            await client.say('done')
        except:
            await client.send_typing(ctx.message.channel)
            await client.say('sorry but its forbidden :sweat_smile:')
    else:
        await client.send_typing(ctx.message.channel)
        await client.say('sorry,but are you an admin :sweat_smile:')

@client.command(pass_context=True)#repeats the typed message
async def say(ctx):
    await client.send_typing(ctx.message.channel)
    await client.say('what do you want me to repeat(indicate me using a # and a space):smile:')
    def c(msg):
        return msg.content.startswith('#')
    msgs=await client.wait_for_message(check=c,channel=ctx.message.channel)
    slice=msgs.content.split(" ")
    await client.send_typing(ctx.message.channel)
    await client.say('i am saying:```%s```' % (' '.join(slice[1:])))

@client.command(pass_context=True)#creates a new channel
async def create_channel(context):
    if 'admin' in (role.name for role in context.message.author.roles):
        try:
            await client.send_typing(context.message.channel)
            await client.send_message(context.message.channel,'what do you want to name it??')
            name=await client.wait_for_message(channel=context.message.channel,author=context.message.author,timeout=30.0)
            await client.send_typing(context.message.channel)
            await client.send_message(context.message.channel,'is it a voice channel or a text channel')
            confirmmsg=await client.wait_for_message(channel=context.message.channel,author=context.message.author,timeout=30.0)
            if (confirmmsg.content=='voice'):
                await client.create_channel(context.message.server,name.content,type=discord.ChannelType.voice)
                await client.send_typing(context.message.channel)
                await client.say('the voice channel named {} has been created'.format(name.content))
            elif(confirmmsg.content=='text'):
                await client.create_channel(context.message.server,name.content,type=discord.ChannelType.text)
                await client.send_typing(context.message.channel)
                await client.say('the text channel named {} has been created'.format(name.content))
            else:
                await client.send_typing(context.message.channel)
                await client.say('wrong')
        except:
            await client.send_typing(context.message.channel)
            await client.say('you took too long try again')
    else:
        await client.send_typing(context.message.channel)
        await client.say('sorry but you must be an admin in order to do that')

@client.command(pass_context=True)#deltes a channel
async def delete_channel(ctx,channel:discord.Channel):
    if 'admin' in (role.name for role in ctx.message.author.roles):
        await client.send_typing(ctx.message.channel)
        await client.say('wait a sec')
        await client.delete_channel(channel)
        await client.send_typing(ctx.message.channel)
        await client.say('the channel named #{} has been deleted'.format(channel.name))
    else:
        await client.send_typing(ctx.message.channel)
        await client.say('you must be an admin in order to that')

@client.command(pass_context=True)#edits an existing channel
async def edit_channel(ctx,channel:discord.Channel):
    if 'admin' in (role.name for role in ctx.message.author.roles):
        embed=discord.Embed(tilte='choose',description='what do you want to do??',colour=discord.Colour.red())
        embed.add_field(name='1.',value='name',inline=False)
        embed.add_field(name='2.',value='topic',inline=False)
        await client.say(embed=embed)
        msg=await client.wait_for_message(channel=ctx.message.channel,author=ctx.message.author,timeout=40.0)
        try:
            if msg.content.startswith('1'):
                await client.say('so its the name you want to change\nplease enter a new name:')
                name=await client.wait_for_message(channel=ctx.message.channel,author=ctx.message.author,timeout=30.0)
                edit=await client.edit_channel(channel,name=name.content)
                await client.say('the channel name has changed from {} to {}'.format(name.content,channel.name))
            else:
                await client.say('what is the new topic of this channel?')
                topic=await client.wait_for_message(channel=ctx.message.channel,author=ctx.message.author,timeout=30.0)
                await client.edit_channel(channel,topic=topic.content)
                await client.say('the topic has been changed for the channel {}'.format(channel.name))
        except:
            await client.say('you took to long')
    else:
        await client.say('sorry but you are not an admin')

@client.command(pass_context=True)#custom help command
async def help(ctx):
    embed=discord.Embed(tilte='LIST OF COMMANDS',description='the operations that the bot can perform',colour=discord.Colour.purple())
    embed.add_field(name='NOTE->',value='each command must be called using a bot prefix like ++command_name',inline=False)
    embed.add_field(name='say->',value='it makes the bot repeat what you have typed',inline=False)
    embed.add_field(name='admin->',value='the bot tells you whether you are an admin or not',inline=False)
    embed.add_field(name='kick [member_name]->',value='it makes the bot kick out a member from the server',inline=False)
    embed.add_field(name='delete_messages->',value='deletes the current messages of the channel or a server',inline=False)
    embed.add_field(name='greets->',value='it just greets back when you greet the bot',inline=False)
    embed.add_field(name='create_channel->',value='it creates a new channel',inline=False)
    embed.add_field(name='delete_channel [channel_name]->',value='it deletes an existing channel',inline=False)
    embed.add_field(name='edit_channel [channel_name]->',value='it edits an existing channel',inline=False)
    embed.add_field(name='rules->',value='rules of the server',inline=False)
    embed.add_field(name='JUST FOR FUN COMMANDS',value='some fun commands that the bot can perform')
    embed.add_field(name='coinflip->',value='flips a coin',inline=False)
    embed.add_field(name='kiss [user_name]->',value='kisses a member in the server',inline=False)
    await client.send_typing(ctx.message.channel)
    await client.send_message(ctx.message.author,embed=embed)

@client.command(pass_context=True)#rules
async def rules(ctx):
    embed=discord.Embed(name='RULES',description='these are the rules for the server,which must be followed')
    embed.set_image(url='https://cdn.discordapp.com/attachments/292781967706030082/359898598219055104/rules-banner.png')
    embed.add_field(name='1.',value='choose an approriate channel for youre messages',inline=False)
    embed.add_field(name='2.',value='dont expect others to write the whole code for you',inline=False)
    embed.add_field(name='3.',value='dont get kicked out for simple and silly reasons',inline=False)
    embed.add_field(name='4.',value='if the bot dosent work properly just text in the general channel regarding the issue of the bot and the bot name also',inline=False)
    embed.add_field(name='5.',value='do not use any kind of language or abusive words that can harm others',inline=False)
    embed.add_field(name='NOTE',value='any violations of the above mentioned rule can lead to kicking or banning you from the server')
    await client.send_typing(ctx.message.channel)
    await client.send_message(ctx.message.channel,embed=embed)

@client.event#greets a new member on join
async def on_member_join(member:discord.Member):
    await client.send_message(member,'welcome to the server {}'.format(member))
    await client.send_message(member,'befor you start texting type in ++rules and check them first')
    await client.send_message(member,'if you need any help then type in ++help command for assistance')

@client.event
async def on_member_join(member):
    with open("users.json","r") as f:
        users=json.load(f)
    await update_data(users ,member)
    with open("usrs.json","w") as f:
        json.dump(users,f)

@client.event
async def on_message(ctx):
    if ctx.author.bot:
        return
    with open("users.json","r") as f:
        users=json.load(f)

    await update_data(users, ctx.author)
    await expierience(users, ctx.author, 5)
    await level_up(users, ctx.author, ctx.channel)

    with open("users.json","w") as f:
        json.dump(users, f)
    await client.process_commands(ctx)

async def update_data(users,user):
    if user.id not in users:
        users[user.id]={}
        users[user.id]['expierience'] = 0
        users[user.id]['level'] = 1
async def expierience(users,user,exp):
    users[user.id]['expierience'] += exp
async def level_up(users,user,channel):
    xp=users[user.id]['expierience']
    level_start=users[user.id]['level']
    level_end=int(xp ** (1/4))

    if level_start<level_end:
        await client.send_message(channel,"{} has grown to level {}".format(user.mention,level_end))
        users[user.id]['level']=level_end

@client.event
async def on_ready():
    print('logged in as: %s' % client.user.name)
    print('ID is:' + client.user.id)
    await client.change_presence(game=discord.Game(name="just helping")


client.run(os.environ.get('TOKEN'))
