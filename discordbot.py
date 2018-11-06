import random
from discord import Game
from discord.ext.commands import Bot

BOT_PREFIX = ("!")
TOKEN = 'token'

client = Bot(command_prefix=BOT_PREFIX)

# Get the square of a number
@client.command(name='square',
                brief="Squares an integer.\n",
                description="Squares an integer.",
                pass_context = True)
async def square(context, number):
    try:
        squared_value = int(number) * int(number)
    except ValueError as error:
        await client.say("Input must be an integer.")
    else:
        await client.say(context.message.author.mention + ", " + str(number) + " squared is " + str(squared_value))

# Generate a random number between two numbers
@client.command(name = 'rand',
                description="Generates a random integer between 2 integers.",
                brief="Generates a random integer between 2 integers.\n",
                aliases=['random'],
                pass_context = True)
async def rand(context, lowerBound, upperBound):
    try:
        lowerBound = int(lowerBound)
        upperBound = int(upperBound)

        randomNumber = random.randint(lowerBound, upperBound)
    except ValueError as error:
        await client.say("Input must be an integer, lowerbound can not be higher than upperbound.")
    else:
        await client.say(context.message.author.mention + ", here is a random integer between %i and %i:\n%i"%(lowerBound, upperBound$

# Rolls a dice, user specifies the size of the dice
@client.command(name = "diceroll",
                description="Rolls a dice of user specified size.",
                brief="Rolls a dice.\n",
                aliases=['dice','roll'],
                pass_context = True)
async def diceroll(context, diceSize):
    try:
        diceSize = int(diceSize)
        rollResult = random.randint(1, diceSize)
    except ValueError as error:
        await client.say("Input must be an integer.")
    else:
        await client.say(context.message.author.mention + ", you rolled a %i."%(rollResult))

# Prints when the bot successfully logs in in the console
@client.event
async def on_ready():
    await client.change_presence(game=Game(name="with humans"))
    print("Logged in as " + client.user.name)

client.run(TOKEN)
