# Imports
import random
import string
import time
import webbrowser

rawPause = input("How many seconds do you want between each site? ")
pause = int(rawPause)
sites = []

# Generate sites and add them to list
def gen():    
    result = ""

    # Generate the end of the URL
    let1 = random.choice(string.ascii_letters)
    let2 = random.choice(string.ascii_letters)
    end = random.randint(1000, 9999)

    rawResult = "https://prnt.sc/" + str(let1) + str(let2) + str(end)
    result = rawResult.lower()

    sites.append(result)

# Algorithm to remove sites that are the improper length
def check():
    for i in sites:
        n = 0
        if len(sites[n]) != 22:
            sites.remove(sites[n])
            n += 1
        else:
            n += 1

# Open the tab
def run():
    webbrowser.open_new_tab(sites[0])
    sites.remove(sites[0]) # Remove the already viewed tab

while True:
    gen()
    check()
    run()
    time.sleep(pause)