import sys
from os import system


dictionary = {}

def add(value):
    if value.split(" ")[1] not in dictionary.get(value.split(" ")[0],[]):
        dictionary.setdefault(value.split(" ")[0], []).append(value.split(" ")[1])
        print("Added")
    else:
        print("ERROR, String already exists for the key")

def keys():
    if not dictionary:
        print("ERROR, No keys exist")
    for key in dictionary:
        print(key)

def members(value):
    if value.split(" ")[0] not in dictionary:
        print("ERROR, key does not exist.")
    for member in dictionary.get(value.split(" ")[0],[]):
        print(member)

def remove(value):
    if value.split(" ")[1] not in dictionary.get(value.split(" ")[0],[]):
        print("ERROR, Member does not exist")
    else:
        dictionary[value.split(" ")[0]].remove(value.split(" ")[1])
        if not dictionary[value.split(" ")[0]]:
            del dictionary[value.split(" ")[0]]
        print("Removed")


def removeAll(value):
    if value in dictionary: 
        del dictionary[value]
        print("Removed")
    else:
        print("ERROR, Key does not exist")

def clear():
    global dictionary 
    dictionary= {}
    print("Cleared")

def keyExists(value):
    if value in dictionary:
        print("True")
    else:
        print("False")

def memberExists(value):
    if value.split(" ")[1] in dictionary.get(value.split(" ")[0],[]):
        print("True")
    else:
        print("False")

def allMembers():
    if not dictionary:
        print("(empty set)")
        return
    for value in dictionary.values():
        for member in value:
            print(member)

def items():
    if not dictionary:
        print("(empty set)")
        return
    for key,value in dictionary.items():
        for member in value:
            print(key+":"+member)

def main():
    run = True

    while run:
        command = input("Enter a command:")

        if "ADD" in command:
            add(command.split("ADD ")[1])
        elif "KEYEXISTS" in command:
            keyExists(command.split("KEYEXISTS ")[1])
        elif "KEYS" in command:
            keys()
        elif "MEMBEREXISTS" in command:
            memberExists(command.split("MEMBEREXISTS ")[1])
        elif "ALLMEMBERS" in command:
            allMembers()
        elif "MEMBERS" in command:
            members(command.split("MEMBERS ")[1])
        elif "REMOVEALL" in command:
            removeAll(command.split("REMOVEALL ")[1])
        elif "REMOVE" in command:
            remove(command.split("REMOVE ")[1])
        elif "CLEAR" in command:
            clear()
        elif "ITEMS" in command:
            items()
        elif "EXIT" in command:
            run = False
        else:
            print("Command not recognized")


if __name__ == "__main__":
    main()