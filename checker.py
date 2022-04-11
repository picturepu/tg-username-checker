from bs4 import BeautifulSoup
import requests
import threading
import time
import os

#opening files

usernames_file = open('username.txt', 'r')
available_file = open('available.txt', 'w')
wrong_file = open('wrong.txt', 'w')

def check(username):
    url = f'https://t.me/{username}'
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')
    
    square_1 = soup.find('div', class_ = 'tgme_body_wrap')
    square = square_1.find('div', class_ = 'tgme_page_extra')   #find @nickname or any subscribers

    if square == None:
        print(f'{username} is available')
        print(username, file = available_file)  #writing to available.txt
    else:
        print(f'{username} is not available')
        print(username, file = wrong_file)      #writing to wrong.txt

usernames = usernames_file.readlines()

for username in usernames:
    if len(threading.enumerate()) < 8:     #number of CPU threads
        th = threading.Thread(target=check, args=(username.strip(), ))
        time.sleep(0.5)
        th.start()
    elif len(threading.enumerate()) < 1:   #stopping program
        usernames_file.close()
        available_file.close()
        wrong_file.close()
    else:
        time.sleep(1)
    

