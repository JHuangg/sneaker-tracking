import os
import sys
import json

def mainMenu(): 
    print('''
        Simple Shoe Inventory Tracking System
        --------------------------------------
        1. View Entire Inventory
        2. View Specific Model Inventory
        2. Add Item to Inventory
        3. Remove Item from Inventory
        4. Edit Items
        5. Exit
        ''')

    while True:
        option = int(input('Please select one of the following options: '))
        if option == 1:
            viewInventory()
            break

        if option == 2:
            viewSpecificInventory()
            break

def viewInventory():
    with open('inventory.txt', 'r') as inv:
        currInventory = json.loads(inv.read())
    returnToMainMenu()

def viewSpecificInventory():
    optionShoe = input('Select the shoe model you wish to look at: ').lower()

    with open('inventory.txt', 'r') as inv:
        currInventory = json.loads(inv.read())
        currShoe = currInventory[optionShoe]

        for i in currShoe:
            print(f"Colourway: {i['Colourway']}\nSize: {i['Size']}\nPrice: {i['Price']}\n")

    returnToMainMenu()

def AddItems():
    removeItem = input('Name of item you wish to remove: ')

    #Check if item exists

    addMore = input ('Would you like to add more items? (y/n): ').lower().strip()
    if addMore == 'y':
        AddItems()
    elif addMore == 'n':
        returnToMainMenu()
    

def returnToMainMenu():
    returnMenu = input('Return to main menu? (y/n): ').lower().strip()
    if returnMenu == 'y':
        mainMenu()
    elif returnMenu == 'n':
        sys.exit()
    else: 
        print('Please select either y or n')
        returnToMainMenu()

def exit():
    sys.exit()

mainMenu()










# def mainMenu():
#     while True:
#         #insert return to main menu
