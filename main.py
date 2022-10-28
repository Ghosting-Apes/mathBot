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
    options = ["+", "-"]
    numOfValues = random.randint(2,4)
    numOfOperations = numOfValues-1
    values = [str(random.randint(1,100)) for i in range(numOfValues)]
    operations = [random.randint(0,1) for i in range(numOfOperations)]
    # Array of "x" and 0 to randomly determine if a variable should be added
    variables = [("x", random.randint(0,2)) if random.randint(0,1) == 1 else ("0",0) for i in range(numOfValues-1)]
    variables.sort(key = lambda x: x[1], reverse=True)

    for i in range(numOfValues):
        # Adds the value + variable to array
        if i == numOfValues-1:
            eq.append(values[i])
        else:
            # Checks if it should add a variable (and with what power)
            if(variables[i][0] == "x"):
                if(variables[i][1] == 0 or variables[i][1] == 1):
                    eq.append(values[i] + variables[i][0])
                    eq.append(options[operations[i]])
                else:
                    eq.append(values[i] + variables[i][0] + "^" + str(variables[i][1]))
                    eq.append(options[operations[i]])
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
