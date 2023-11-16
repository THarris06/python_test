# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 08:45:12 2023

@author: tyson.harris
"""

def title():
    
    print ("\nThe Wizard Inventory Program")
    
    
def command_menu():
    
    print ("\nCOMMAND MENU")
    
    command_list = ("Show", "Grab", "Edit", "Drop", "Exit")
    
    command_desc = ("Show all items", "Grab an item", 
                    "Edit an item", "Drop an item", 
                    "Exit program")
    
    for a, b in zip(command_list, command_desc):
        print ("{} - {}".format(a, b))
        
    
def show_command(inventory_list):
    
    for i, item in enumerate(inventory_list, start = 1):
        print ("{} - {}". format(i, item))
        
    
def grab_command(inventory_list):
    
    if len(inventory_list) < 4:
        
        item_grab = input("Name:\t")
        inventory_list.append(item_grab)
        print ("{} was added".format(item_grab))
        
    else:
        print ("You can't carry anymore items. Drop something first.")
        

def edit_command(inventory_list):
    
    edit_input = input("Number:\t")
    
    if edit_input.isnumeric():
        
        edit_input = int(edit_input) - 1
        
        if (edit_input < 0) or (edit_input + 1 > len(inventory_list)):
            
            print ("Error. Selection out of range")
            edit_command(inventory_list)
            
        else:
            
            new_name = input("Updated name:\t")
            
            inventory_list[edit_input] = new_name
            
            print ("Item number {} was updated.".format(edit_input + 1))
    
    else:
        print ("Error")
        edit_command(inventory_list)
        
        
def drop_command(inventory_list):
    
    drop_input = input("Number:\t")
    
    if drop_input.isnumeric():
        
        drop_input = int(drop_input) - 1
        
        if (drop_input < 0) or (drop_input + 1 > len(inventory_list)):
            
            print ("Error. Selection out of range")
            drop_command(inventory_list)
            
        else:
            
            print ("{} was dropped.".format(inventory_list[drop_input]))
            inventory_list.pop(drop_input)
        
        
def main():
    
    loop = True
    inventory = ["wooden staff", "wizard hat", "cloth shoes"]
    
    title()
    command_menu()
    
    while loop:
        
        print ()
        
        command_input = input("Command:\t")
        
        if command_input.lower() == 'show':
            show_command(inventory)
            
        elif command_input.lower() == 'grab':
            grab_command(inventory)
            
        elif command_input.lower() == 'edit':
            edit_command(inventory)
        
        elif command_input.lower() == 'drop':
            drop_command(inventory)
        
        elif command_input.lower() == 'exit':
            loop = False
            
        else:
            print ("Error. Invaild Command")
            loop = False
            

if __name__ == '__main__':
    
    main()
    
    print("\nBye!")