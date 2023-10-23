# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 10:08:39 2023

@author: tyson.harris
"""

def title():
    print ("\nCOMMAND MENU")
    
def options():
    option_name = ["list",
                   "add",
                   "del",
                   "exit"]
    
    option_desc = ["List all movies",
                   "Add a movie",
                   "Delete a movie",
                   "Exit program"]
    
    for n, d in zip(option_name, option_desc):
        print ("{} - {}".format(n, d))
      
def movies_list(movies):
    for i, item in enumerate(movies, start = 1):
        print ("{}. {} ({})".format(i, item[0], item[1]))

def list_cmnd(movies):
    movies_list(movies)
    
def add_cmnd(movies):
    name = input("Name:\t")
    year = int(input("Year:\t"))
    
    if (year < 0):
        print ("Error; invalid entry")
        add_cmnd(movies)
    else:
        movie = [name, year]
        print ("{} has been added".format(name))
        movies.append(movie)
        
    
def del_cmnd(movies):
    number = int(input("Number:\t")) - 1
    
    if (number < 0) or (number + 1 > len(movies)):
        print ("Error; invalid entry")
        
    else:
        print ("{} has been deleted".format(movies[number][0]))
        movies.pop(number)
        
        
def main():
    movies = [["Monty Python and the Holy Grail", 1975],
              ["On the Waterfront", 1954],
              ["Cat on a Hot Tin Roof", 1958]]
    
    title()
    options()
    
    loop = True
    
    while loop:
        
        movies.sort()
        command = input("\nCommand:\t").lower()
        
        if command == 'list':
            list_cmnd(movies)
            
        elif command == 'add':
            add_cmnd(movies)
            
        elif command == 'del':
            del_cmnd(movies)
            
        elif command == 'exit':
            loop = False
            
        else:
            print ("Error; unknown command")
          
    print ("\nBye!")   
    
if __name__ == '__main__':    
    main()
    
    

