#!/usr/bin/python3
# lists all gists of a given user

import json
import requests

def get_all_gists(username):
    gists = []
    page = 1
    per_page = 100  # Maximum number of results per page

    while True:
        if username:
            url = f'https://api.github.com/users/{username}/gists'
        else:
            url = 'https://api.github.com/gists/public'

        # Make the request with pagination parameters
        response = requests.get(url, params={'per_page': per_page, 'page': page})
        
        # Check if the response is successful
        if response.status_code != 200:
            print(f"Error: {response.status_code} - {response.json()}")
            break

        # Get the gists from the response
        gists_on_page = response.json()
        
        # If there are no more gists, break the loop
        if not gists_on_page:
            break
        
        # Add the gists to the list
        gists.extend(gists_on_page)
        
        # Move to the next page
        page += 1

    return gists


def analyze_gists(gists):
    # for each file in the gist if it is not a markdown or a text file print the file name
    for gist in gists:
        # print(gist)
        for file in gist['files']:
            #if not file.endswith('.md') and not file.endswith('.txt')  and not file.endswith('.java')  and not file.endswith('.log')    and not file.endswith('.json')   and "." in file:
            if file.endswith('.py') or file.endswith('.sh') or file.endswith('.js'):
                print("* ["+file+": "+gist['description']+"]("+gist['html_url']+")")
def dl_write_gists(username):
    user_gists = get_all_gists(username)
    # write user gists to file
    with open(f"{username}_gists.json", "w") as file:
        json.dump(user_gists, file, indent=2)
    return user_gists

if __name__ == "__main__":
    
    # Optionally, get gists for a specific user
    username = 'monperrus'  # Replace with the actual username

    # dl_write_gists(username)
    with open(f"{username}_gists.json", "r") as file:
        user_gists = json.load(file)
    analyze_gists(user_gists)   
    #print(f"Total gists for {username}: {len(user_gists)}")
