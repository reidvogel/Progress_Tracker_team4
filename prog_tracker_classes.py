list_of_users = []
list_of_shows = []

class User():
    def __init__(self, username, password, role):
        self.name = username
        self.password = password
        self.shows = []
        self.shows_prog = []
        self.role = role #user or admin
    def addUser(self): #This is used by sign up or admin
        list_of_users.append(self)
    def delUser(self): 
        list_of_users.remove(self)
    def addShow(self, show):
        self.shows.append(show)
    def delShow(self, show):
        self.shows.remove(show)

    def editUser(self, var):
        '''var is what they want to update'''
        if var == 1: #Username
            print("Please enter a new username: ")
            self.name = input()
        elif var == 2: #Password
            print(f"Please enter a new password for {self.name}: ")
            self.password = input()
    def showList(self):
        print(f"These are the shows currently on {self.name}'s list: ")
        for i in self.shows:
            print(f"{i+1}: {self.shows[i]}") #Gotta account for index starting at 0
    def showListandProg(self):
        print("These are the shows you are currently watching and your progress: ")
        for i in self.shows:
            print(f"{i+1}: {self.shows[i]}, Progress: {self.shows_prog[i+1]}") #Gotta account for index starting at 0
    def updateShowProg(self):
        self.showListandProg()
        print("Please enter the number corresponding to the show you would like to update progress: ")
        index = input() - 1 #Gotta account for index starting at 0
        print(f"Enter the number of episodes you have watched for {self.shows[index]}")
        self.shows_prog[index] = input() #maybe check it's not more than episodes available
        
    
  
            
class Show():
    def __init__(self, name, episodes):
        self.name = name
        self.ep = episodes
    def addShow(self):
        list_of_shows.append(self)
        print(f"{self.name} added to List of Available Shows")
    def delShow(self):
        list_of_shows.remove(self)
        print(f"{self.name} removed from List of Available Shows")
    def ListShows(self):
        print("Here are all the available shows")
        for i in list_of_shows:
            print(f"{i}: {list_of_shows[i]}")
    def UpdateShow(self): #used to change number of episodes
        self.ListShows()
        print("Please enter the number corresponding to the show you would like to update: ")
        index = input()
        list_of_shows[index].ep = input()
        print(f"The number of episodes for {list_of_shows[index]} is now {list_of_shows[index].ep}")
        



