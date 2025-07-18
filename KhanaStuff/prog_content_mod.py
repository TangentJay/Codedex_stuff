# KhanaStuff/prog_content_mod.py
'''
* Author: TanB
* Created: 7/17/2025
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff
'''

#content modaration bot

# porsitive , nutural, negative post
wrd_coint = 13
sentiment = 'netural'
account_age_in_days = 60

is_suspicious = wrd_coint <= 3 or wrd_coint > 200 
is_usefulpost = not is_suspicious and sentiment != 'negative'
is_trusted = account_age_in_days >=30

#promote useful post by trusted users.
if  is_usefulpost and is_trusted:
    print("This post has been featured on the hot list")

#spmmers tend to use brand new accounts
if sentiment == 'negative' and account_age_in_days < 7:
    print('This post has been flagged as potential spam')

