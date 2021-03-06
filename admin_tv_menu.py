#imports
from prog_tracker_classes import *


# Administration User Menu options:
def admin_tv_menu():
    print("""Select option:
    1: View All TV Show
    2: Add New TV Show
    3: Edit Specific TV Show
    4: Remove Specific TV Show""")
    option = check_int()
    match option:

        # See all tv shows
        case 1:
            Show.ListShows()
        # Add user information
        case 2:
            title = input("Please enter the title of the new show:")
            print(f"Enter the total number of episodes in {title}")
            ep = check_int()
            new_show = Show(title,ep)
            Show.addShow(new_show)
        #delete show
        case 3:
            Show.delShow()
        case 4:
        #edit tv show
            Show.UpdateShow()
        case _:
            print("Not a valid input.")

