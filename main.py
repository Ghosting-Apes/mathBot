import discord, random, os, sys
from env import DISCORD_TOKEN

client = discord.Client(intents=discord.Intents.default())

TOKEN = os.getenv(DISCORD_TOKEN)

arr = []
global y, add, test, x, ans
y = random.randint(1,5)
add = random.randint(1, 5)
test = False
x = random.randint(1,5)


def problemGenerator():
    eq = []
    options = ["+", "-", "*", "/"]
    numOfValues = random.randint(2,4)
    numOfOperations = numOfValues-1
    values = [str(random.randint(1,100)) for i in range(numOfValues)]
    operations = [random.randint(0,3) for i in range(numOfOperations)]
    for i in range(numOfValues):
        if i == numOfValues-1:
            eq.append(values[i])
        else:
            eq.append(values[i])
            eq.append(options[operations[i]])
    return " ".join(eq) + " = "

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
    else:
        y = random.randint(1,5)


def rand(start: int):
    return random.randint(start + 5, 10)

client.run(DISCORD_TOKEN)
