#imports
from prog_tracker_classes import *


# Administration User Menu options:
def admin_tv_menu():
    option = input("""Select option:
    1: View All TV Show
    2: Add New TV Show
    3: Edit Specific TV Show
    4: Remove Specific TV Show""")
    match option:

        # See all tv shows
        case "1":
            Show.ListShows()
        # Add user information
        case "2":
            Show.addShow()
        #delete show
        case "3":
            Show.delShow()
        case "4":
        #edit tv show
            Show.UpdateShow()
        case _:
            print("Not a valid input.")


def add_tv_show():
    # input new tv show title:
    title = input("Enter name of tv show: ")
    Show.addshow(title)
    
    


def edit_tv_show():
    # Locate user by entering their username
    showtitle = input("Enter existing show: ")
    for show in shows:
        if show.shows == showtitle:
            shows == show
            break
        else:
            print("Show not found")
            return
    while True:
        # Edit existing show title
        new_title = input("Enter new title: ")
        # update progress:
        updated_progress = input("Enter 'not completed', 'in-progress', or 'completed': ")
    shows.showtitle = newtitle
    show_prog.progress = updated_progress

def remove_tvshow():
    # Locate show by entering its title
    title = input("Enter existing user's username: ")
    for u in shows:
        if u.username == username:
            list_of_users == u
            break
        else:
            print("Show not found")
            return
    show = [tvshow for tvshow in shows if shows.title != title]
