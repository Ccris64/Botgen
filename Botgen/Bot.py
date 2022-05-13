import os.path
import random
import json
print("Welcome to the bot!")
names = ["John","Luke","Josh","King","Isabelle","Isabella","Charlotte"]    
botName = names[random.randrange(0,6)]
if os.path.exists("dictionary.bot"):
    print("Loading dictionary.bot...")
    dictFile = open("dictionary.bot", "r")
    dictData = dictFile.read()
    botDictionary = json.loads(dictData)
    dictFile.close()
else:
    print("Could not find dictionary.bot file. Please create one yourself or grab the base one at this project's website.")
    exit()

print("Bot initialized. ")
print("You are now talking to a generated bot called \""+botName+"\".")
while True:
    msg = input(">").lower()
    print("You:",msg)
    if msg in botDictionary:
        print(dict(botDictionary)[msg].format(botName,msg)) ### {1}, {2}, {3}... can be added to the dictionary.bot file. 
    else:
        print("Sorry, I didn't understand. If you want to customize my commands, modify the dictionary.bot file in my folder.")
