# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 09:47:48 2023

@author: tyson.harris
"""

def sep_line():
    
    print ('=' * 50)
    
    
def title():
    
    print ("BASEBALL TEAM MANAGER\n")
    
    
def menu_options():
    
    print ("MENU OPTIONS")
    
    option_list = ["Display lineup", 
                   "Add Player", 
                   "Remove PLayer", 
                   "Move Player", 
                   "Edit Player Postion", 
                   "Edit Player Stats", 
                   "Exit Program"]
    
    for i, item in enumerate(option_list, start = 1):
        print ("{} - {}". format(i, item))
        
        
def positions(positions_list):
    
    print ("POSITIONS")
    for i in positions_list:
        print ("{},".format(i), end=" ")
    print ()
    
    
    
def get_at_bats():
    
    at_bats = int(input("At bats:\t"))
    if (at_bats <= 1) or (at_bats >= 600):
        print ("Error; At bats must be between 1 and 600")
        get_at_bats()
    
    else:
        return at_bats
    
    
def get_hits(at_bats):
    
    hits = int(input("Hits:\t"))
    if (hits < 0) or (hits > at_bats):
        print ("Error; hits exceeds at bats")
        get_hits(at_bats)
        
    else:
        return hits
    
    
def linup_list(team_lineup):
    
    print ("\n\t\t Player\t\t POS\t AB\t H\t AVG")
    print ('-' * 45)
    for i, item in enumerate(team_lineup, start = 1):
        print ("{}.\t\t {}\t\t {}\t\t {}\t {}\t {}".format(i, item[0], item[1], item[2], item[3], item[4]))



def add_cmnd(team_linup, positions_list):
    
    name = input("Name:\t")
    
    p_loop = True
    
    while p_loop:
        
        position = input("Position:\t").upper()
        
        if position in positions_list:
            p_loop = False
            
        else:
            print ("Invalid poition. Try again.")
            positions(positions_list)
            
    at_bats = get_at_bats()
    num_hits = get_hits(at_bats)
    average = num_hits / at_bats
    
    player = [name, position, at_bats, num_hits, average]
    
    team_linup.append(player)
    print ("{} was added.".format(name))
    

def del_cmnd(team_lineup):
    number = int(input("Number:\t")) - 1
    
    if (number < 0) or (number + 1 > len(team_lineup)):
        print ("Error; invalid entry")
        del_cmnd(team_lineup)
        print ()
        
    else:
        print ("{} has been deleted".format(team_lineup[number][0]))
        team_lineup.pop(number)
    
    
def move_cmnd(team_lineup):
      number = int(input("Current lineup number:\t")) - 1
          
      if (number < 0) or (number + 1 > len(team_lineup)):
          print ("Error; invalid entry")
          move_cmnd(team_lineup)
          print ()
          
      else:
          print ("You selected {}".format(team_lineup[number][0]))

          new_lineup = int(input("New lineup number:\t"))
          
          delete = team_lineup.pop(number)
          team_lineup.insert(new_lineup - 1, delete)
          
                 
def edit_player_position(team_lineup, positions_list):
    number = int(input("Lineup number:\t")) - 1
        
    if (number < 0) or (number + 1 > len(team_lineup)):
        print ("Error; invalid entry")
        edit_player_position(team_lineup, positions_list)
        print ()
        
    else:
        print ("You selected {}".format(team_lineup[number][0]))
        
        p_loop = True
        
        while p_loop:
            
            position = input("Position:\t").upper()
            
            if position in positions_list:
                p_loop = False
                
            else:
                print ("Invalid poition. Try again.")
                positions(positions_list)
                
        team_lineup[number][1] = position
    
        print ("{} was updated".format(team_lineup[number][0]))
    
    
def edit_player_stats(team_lineup):
    number = int(input("Lineup number:\t")) - 1
        
    if (number < 0) or (number + 1 > len(team_lineup)):
        print ("Error; invalid entry")
        edit_player_stats(team_lineup)
        print ()
        
    else:
        print ("You selected {}".format(team_lineup[number][0]))
        
        at_bats = get_at_bats()
        num_hits = get_hits(at_bats)
        average = num_hits / at_bats
    
    team_lineup[number][2] = at_bats
    team_lineup[number][3] = num_hits
    team_lineup[number][4] = average
    
    print ("{} was updated".format(team_lineup[number][0]))
    
    
def main():
    
    positions_list = ['C', '1B','2B', '3B', 'SS', 
                      'LF', 'CF', 'RF', 'P' ]
    
    team_lineup = [['Joe', 'P', 10, 2, 0.2],
                  ['Tom', 'SS', 11, 4, 0.364],
                  ['Ben', '3B', 9, 3, 0.333],
                  ['Mike', 'C', 4, 1, 0.25]]
    
    loop = True
    
    sep_line()
    title()
    menu_options()
    print ()
    positions(positions_list)
    sep_line()
    
    while loop:
    
        cmnd = int(input("Menu Option:\t"))
            
        if cmnd == 1:
            linup_list(team_lineup)
        
        elif cmnd == 2:
            add_cmnd(team_lineup, positions_list)
            
        elif cmnd == 3:
            del_cmnd(team_lineup)
            
        elif cmnd == 4:
            move_cmnd(team_lineup)
            
        elif cmnd == 5:
            edit_player_position(team_lineup, positions_list)
            
        elif cmnd == 6:
            edit_player_stats(team_lineup)
         
        elif cmnd == 7:
            loop = False
    
        print()


if __name__ == '__main__':
    main()
    
    print ("Bye!")
    
