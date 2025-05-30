import urllib.request
import urllib.error
import sys
import json
from get_user_activity import get_user_activity

while True:

    user_found = False

    while not user_found:                               # Loop until a valid user is found
        user = input("Enter a GitHub username: ")
        if user == 'exit':
            print("Exiting the program.")
            sys.exit()

        url = f'https://api.github.com/users/{user}/events'
        try:
            response = urllib.request.urlopen(url)      # Make the API request
            data_json = json.loads(response.read())     # Parse the JSON response
            user_found = True

            if len(data_json) == 0:
                print("User has no recent activity.")
            else:
                print(f'User {user} found!')

        except urllib.error.HTTPError as e:
            print(f'User was not found! Error Code: {e.code} \n Please try again!' )


    with open('user_data.json','w+') as file:
        json.dump(data_json,file, indent=2)
    with open('user_data.json','r') as json_data:
        api_data = json.load(json_data)

    get_user_activity(api_data)


    






