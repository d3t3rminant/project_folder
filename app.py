def vypoctove_menu(a,b,c):
    return vypocet(1,2,3)

def vypocet(a,b, c):
    return soucet(a, b) - c

def soucet(a,b):
    return a+b



blogs = {'Blog1':'Content1'} # blog_name:blog_object
def menu():
    print_blogs()

def print_blogs():
    for key, item in blogs.items():
        print("Blog {} - {}".format(key, item))
