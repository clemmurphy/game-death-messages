import random
import json

TIMES_TO_RUN = 10

# import external files to lists

with open('decoration.txt') as f:
    decoration = f.read().splitlines()
with open('prefix.txt') as f:
    prefix = f.read().splitlines()
with open('suffix.txt') as f:
    suffix = f.read().splitlines()
with open('pre_prefix.txt') as f:
    pre_prefix = f.read().splitlines()
with open('deco_spaces.txt') as f:
    deco_spaces = f.read().splitlines()
with open('names.txt') as f:
    names = f.read().splitlines()

# chance that the gamertag will have this element

DEC_CHANCE = 0.3
DEC_SPC_CHANCE = 0.7
PREF_CHANCE = 0.4
SUFF_CHANCE = 0.4
PREPRE_CHANCE = 0.1
LEET_CHANCE = 0.4
UPPER_CHANCE = 0.3
ALT_CHANCE = 0.1

def chance(rate):
    if random.random() < rate:
        return True
    else:
        return False


def name_process(name):
    if (name.find("i") != -1):
        if chance(LEET_CHANCE):
            name = name.replace("i", "ii")
    if (name.find("o") != -1):
        if chance(LEET_CHANCE):
            name = name.replace("o", "0")
    if (name.find("s") != -1):
        if chance(LEET_CHANCE):
            name = name.replace("s", "Z")
    if (name.find("e") != -1):
        if chance(LEET_CHANCE):
            name = name.replace("e", "3")
    if (name.find("a") != -1):
        if chance(LEET_CHANCE):
            name = name.replace("a", "4")
    if (name.find("u") != -1):
        if chance(LEET_CHANCE):
            name = name.replace("u", "UwU")
    if chance(UPPER_CHANCE):
        name = name.upper()
    if (name.find(" ") != -1):
        name = name.replace(" ", "_")
    return name

def construct(name):
    d = ""
    ds = ""
    pp = ""
    p = ""
    s = ""

    if chance(DEC_CHANCE):
        d = random.choice(decoration).strip("\n")
        if chance(DEC_SPC_CHANCE):
            ds = random.choice(deco_spaces).strip("\n")
        else:
            ds = " "
    
    if chance(PREPRE_CHANCE):
        pp = random.choice(pre_prefix).strip("\n")
    
    if chance(PREF_CHANCE):
        p = random.choice(prefix).strip("\n")
    
    if chance(SUFF_CHANCE):
        s = random.choice(suffix).strip("\n")
    
    name = pp + d + ds + p + name + s + ds + d

    return name

def death_message(name):
    with open('deathmethods.txt') as f:
        methods = f.read().splitlines()
    with open('weapons.txt') as f:
        weapons = f.read().splitlines()

    method = random.choice(methods)
    weapon = random.choice(weapons)

    message = "You " + method + " " + name + " with a " + weapon

    return message

def chat(name):
    with open('chat.txt') as f:
        chat_stubs = f.read().splitlines()
    chat_stub = random.choice(chat_stubs)
    
    chat = name + chat_stub
    return chat

def main(r):
    while r > 0:
        name = random.choice(names)
        name = name_process(name)
        name = construct(name)
        message = death_message(name)
        chat_message = chat(name)
        print(message)
        print(chat_message)
        print("")
        r -= 1

main(TIMES_TO_RUN)