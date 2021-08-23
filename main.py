import os
import sys
import json
clear = lambda: os.system('cls')

def mainMenu(): 
    clear()
    print('''
Simple Shoe Inventory Tracking System
--------------------------------------
1. View Entire Inventory
2. View Specific Model Inventory
3. Add Item to Inventory
4. Remove Item from Inventory
5. Edit Items
6. Exit
    ''')

    while True:
        option = int(input('Please select one of the following options: '))
        if option == 1:
            viewInventory()
            break

        elif option == 2:
            viewSpecificInventory()
            break
        
        elif option == 3:
            addItems()
            break

        elif option == 4:
            removeItems()
            break

        elif option == 5:
            editItems()
            break

def viewInventory():
    clear()
    with open('inventory.txt', 'r') as inv:
        currInventory = json.loads(inv.read())
        for name,value in enumerate(currInventory):
            print(f"{value}: {currInventory[value]}")
    returnToMainMenu()

def viewSpecificInventory():
    clear()
    optionSku = input('Select the sku you wish to look at: ').upper()

    with open('inventory.txt', 'r') as inv:
        currInventory = json.loads(inv.read())

        if currInventory.get(optionSku) is not None:
            for i,value in enumerate(currInventory):
                if(value == optionSku):
                    currShoe = currInventory[value]
                    if (len(currShoe) > 1):
                        for x in range(len(currShoe)):
                            print(f"Model: {currShoe[x]['model']}\nSize: {currShoe[x]['size']}\nPrice: {currShoe[x]['price']}\n")
                    elif (len(currShoe) == 1):
                        print(f"Model: {currShoe[0]['model']}\nSize: {currShoe[0]['size']}\nPrice: {currShoe[0]['price']}")
        else:
            print('You currently do not own that SKU')
            
    returnToMainMenu()

def addItems():
    clear()
    addSku = input('Enter the SKU you wish to add: ').upper()
    addModel = input('Enter the model name: ').capitalize()
    addSize = float(input('Enter the product size: '))
    addPrice = float(input('Enter the product price: '))

    newItem = {'model': addModel, 'size:': addSize, 'price:': addPrice}
    newList = [newItem]

    with open('inventory.txt', 'r') as inv:
        currInventory = json.loads(inv.read())

    if currInventory.get(addSku) is not None:
        for i,value in enumerate(currInventory):
            if(value == addSku):
                currShoe = currInventory[value]
                currShoe.append(newItem)
    else:
        currInventory[addSku] = newList

    with open('inventory.txt', "w") as invFile:
        json.dump(currInventory, invFile, sort_keys = True, indent = 1)

    removeMore = input ('Would you like to add more items? (y/n): ').lower().strip()
    if removeMore == 'y':
        removeItems()
    elif removeMore == 'n':
        returnToMainMenu()

def removeItems():
    clear()
    sku = input('Enter the SKU you wish to remove: ')

    #Check if item exists

    removeMore = input ('Would you like to remove more items? (y/n): ').lower().strip()
    if removeMore == 'y':
        removeItems()
    elif removeMore == 'n':
        returnToMainMenu()

def editItems():
    clear()
    sku = input('Enter the SKU you wish to edit: ')
    

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
