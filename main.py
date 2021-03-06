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
5. Exit
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

    newItem = {'model': addModel, 'size': addSize, 'price': addPrice}
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
    removeSku = input('Enter the SKU you wish to remove: ').upper().strip()

    with open('inventory.txt', 'r') as inv:
        currInventory = json.loads(inv.read())

    if currInventory.get(removeSku) is not None:
        for key, value in list(currInventory.items()):
            if key == removeSku:
                skuList = currInventory[key]
                if (len(skuList) > 1):
                    tooManySku = input("You currently own more than one of this sku, please select the model you wish to remove: ").capitalize()
                    for skuKey, skuValue in enumerate(skuList):
                       if(skuList[skuKey]['model'] == tooManySku):
                        skuList.pop(skuKey)
                else:
                    del(currInventory[key])

    else:
        print('You currently do not own that SKU')

    with open('inventory.txt', "w") as invFile:
        json.dump(currInventory, invFile, sort_keys = True, indent = 1)

    removeMore = input ('Would you like to remove more items? (y/n): ').lower().strip()
    if removeMore == 'y':
        removeItems()
    elif removeMore == 'n':
        returnToMainMenu()

def doesSkuExist(invTest, object):
    for key, value in list(invTest.items()):
            if key == object:
                skuList = invTest[key]
                if (len(skuList) > 1):
                    return('You currently own more than one model of this sku.')
                else:
                    del(invTest[key])
                    return invTest

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
