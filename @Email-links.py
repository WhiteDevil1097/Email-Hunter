import requests
from bs4 import BeautifulSoup
import re
import colorama
from colorama import Fore,Style

# some decorations for giving it a good look and feel.
colorama.init()
print(Fore.RED + Style.BRIGHT)
print()
print(r"           .AMMMMMMMMMMA.            ")
print(r"         .AV. :::.:.:.::MA.          ")
print(r"        A' :..        : .:`A         ")
print(r"       A'..              . `A.        ")
print(r"      A' :.    :::::::::  : :`A       ")    
print(r"      M  .    :::.:.:.:::  . .M        ")
print(r"      M  :   ::.:.....::.:   .M         ")   
print(r"      V : :.::.:........:.:  :V         ")
print(r"      AA:    ..:...:...:.   A A           _   _   _   _   _     ")
print(r"    .V  MA:.....:M.::.::. .:AM.M.        / \ / \ / \ / \ / \   ")
print(r"   A'  .VMMMMMMMMM:.:AMMMMMMMV: A       ( E | m | a | i | l )    ")
print(r"  :M .  .`VMMMMMMV.:A `VMMMMV .:M:       \_/ \_/ \_/ \_/ \_/    ")
print(r"   V.:.  ..`VMMMV.:AM..`VMV' .: V   >>>Devoloper_By_White_Devil<<<  ")
print(r"    V.  .:. .....:AMMA. . .:. .V     ")
print(r"     VMM...: ...:.MMMM.: .: MMV       ")
print(r"        `VM: . ..M.:M..:::M'         ")
print(r"         `M::. .:.... .::M           ")
print(r"          M:.  :. .... ..M           ")
print(r"          V:  M:. M. :M .V           ")
print(r"          `V.:M.. M. :M.V'           ")
print()

def extract_links_from_email(email_id):
    """
    Extracts links associated with a given email ID from various online sources.

    Args:
        email_id (str): The email ID to extract links for.

    Returns:
        A dictionary with links categorized by source.
    """
    links = {                                                                                                                           'linkedin': [],
        'github': [],
        'twitter': [],
        'facebook': [],
        'other': []
    }

    # LinkedIn
    linkedin_url = f"https://www.linkedin.com/search/results/content/?keywords={email_id}"
    response = requests.get(linkedin_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    for a in soup.find_all('a', href=True):
        link = a['href']
        if link.startswith('https://www.linkedin.com/in/'):
            links['linkedin'].append(link)                                                                                                   
    # GitHub
    github_url = f"https://github.com/search?q={email_id}"
    response = requests.get(github_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    for a in soup.find_all('a', href=True):
        link = a['href']
        if link.startswith('https://github.com/'):
            links['github'].append(link)

    # Twitter
    twitter_url = f"https://twitter.com/search?q={email_id}"
    response = requests.get(twitter_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    for a in soup.find_all('a', href=True):
        link = a['href']
        if link.startswith('https://twitter.com/'):
            links['twitter'].append(link)

    # Facebook
    facebook_url = f"https://www.facebook.com/search/top/?q={email_id}"
    response = requests.get(facebook_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    for a in soup.find_all('a', href=True):
        link = a['href']
        if link.startswith('https://www.facebook.com/'):
            links['facebook'].append(link)

    # Other links
    google_url = f"https://www.google.com/search?q={email_id}"
    response = requests.get(google_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    for a in soup.find_all('a', href=True):
        link = a['href']
        if not link.startswith('https://www.google.com/') and not link in links.values():
            links['other'].append(link)

    return links
# Example usage:
email_id = input("Enter an email ID: ")
links = extract_links_from_email(email_id)
print("Extracted links:")
for source, link_list in links.items():
    print(f"{source.capitalize()}:")
    for link in link_list:
        print(link)

