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

