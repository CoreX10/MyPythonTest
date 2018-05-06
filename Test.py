# This is a test program

def addToInventory(inventory, addedItems):

    for i in range(len(addedItems)):
        inventory.setdefault(addedItems[i],0)
        inventory[addedItems[i]] += 1

    return inventory
  

def displayInventory(inventory):
    print('Inventory:')
    item_total = 0
    for k,v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print('\nTotal number of items: ' + str(item_total))

dragonLoot = ['gold coin','dagger','gold coin','gold coin','ruby']
inv = {'gold coin':42, 'rope':1}
inv = addToInventory(inv,dragonLoot)
displayInventory(inv)
