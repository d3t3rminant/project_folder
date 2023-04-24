blogs = {'Blog1':'Content1'} # blog_name:blog_object
def menu():
    choice = None
    while choice != 0:
        choice = int(input("Enter 1 to print the blogs. Enter 0 to end the program: "))
        if choice == 1:
            print_blogs()
    print("End of program")

def print_blogs():
    for key, item in blogs.items():
        print("Blog {} - {}".format(key, item))



if __name__ == "__main__":
    menu()