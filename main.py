import discord, random, os, sys
# from discord.ext import commands
from private.vars import *

client = discord.Client(intents=discord.Intents.default())

# client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

# @bot.start("MTAzMzU0ODQwMzc5NzQxMzkyOA.Gk4bZv.6dFlHzq4nvZsgEFOQqrS7_ZpL55u7vnjSBbJqw")

arr = []
global y, add, test, x, ans
y = random.randint(1,5)
add = random.randint(1, 5)
x = random.randint(1,5)

def betterProblemGenerator():
    eq = []
    op = ["+", "-", "*", "/"]
    numOfValues = random.randint(1,4)
    numOfOperations = numOfValues-1



def problemGenerator():
    opp = ["+", "-", "*", "/"]
    ran1 = random.randint(0,99)
    ran2 = random.randint(0, 99)
    ran0 = random.randint(0,3)
    if ran0 == 0:
        ans = ran1 + ran2
    elif ran0 == 1:
        ans = ran1 - ran2
    elif ran0 == 2:
        ans = ran1 * ran2
    else:
        ans = ran1 / ran2
    return str(ran1) + " " + opp[ran0] + " " + str(ran2)
    # eq = []
    # for i in range(numOfValues + numOfOperations):
    #     if not i % 2:
    #         eq.append(values[i/2])
    #         ranX = random.randint(0,1)
    #         if not i and ranX:
    #             eq[0] += 'x'
    #     elif difficulty < 2:
    #         if i == 1:
    #             eq.append(operations[0])
    #         else:
    #             randOp = random.randint(1, difficulty + 3)
    #             eq.append(operations[randOp])
    # e = ''.join(eq)
    # return e


@client.event
async def on_ready():
    print("We are online")

@client.event
async def on_message(message):
    global y, add, test, x
    values = []
    if test:
        x = random.randint(1,5)
        test = False
    if message.author == client.user:
        return
    if y == x:
        await message.channel.send(problemGenerator())
        test = True
        await message.reply("GOD DID")
        if str(ans) == message.author:
            await message.channel.send("Correct")
        else:
            await message.channel.send("Wrong")
    else:
        y = random.randint(1,5)




def rand(start: int):
    return random.randint(start + 5, 10)

client.run(DISCORD_TOKEN)
