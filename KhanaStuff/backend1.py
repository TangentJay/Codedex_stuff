# Codedex_stuff/KhanaStuff/backend1.py
'''
* Author: TanB
* Created: 7/3/2025
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff
'''



# Collect user profile data.
first_name = input("What's your first name? ")
email=input('Please enter your email: ')
page_title=input('please enter a title: ')

# Construct a personalized page header for the logged in user.
header_title = "<h1>" + first_name + "</h1>"
header_subtitle = "<h2>Hello, " + first_name + "!</h2>"
header_content = "<p>" + email + "@example.com</p>"
page_header = header_title + header_subtitle + header_content

# Construct the main profile page content.
section_title = "<h2>About " + page_title + "</h2>"
section_text = "<p>This is a cool bio.</p>"
button = "<button>Like</button>"
section_footer = "<p>Notifications: 4</p>"
page_content = section_title + section_text + button + section_footer

# The final HTML body combines all the elements, in order.
print("The HTML string for your profile page is:")
print(page_header + page_content)