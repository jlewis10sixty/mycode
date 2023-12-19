#!/usr/bin/python3
"""tracking the iss using
   api.open-notify.org/astros.json | Alta3 Research"""

# notice we no longer need to import urllib.request or json
import requests

## Define URL
MAJORTOM = 'http://api.open-notify.org/astros.json'

def main():
    """runtime code"""

    ## Call the webservice
    groundctrl = requests.get(MAJORTOM)
    # send a post with requests.post()
    # send a put with requests.put()
    # send a delete with requests.delete()
    # send a head with requests.head()

    ## strip the json off the 200 that was returned by our API
    ## translate the json into python lists and dictionaries
    helmetson = ({'message': 'success', 'people': [{'name': 'Eddie Kopra', 'craft': 'ISS'}, {'name': 'James Peake', 'craft': 'ISS'}, {'name': 'Yuri Kopra', 'craft': 'ISS'}, {'name': 'Buzz Aldrin', 'craft': 'ISS'}], 'number': 4})

    ## display our Pythonic data
    print("\n\nConverted Python data")
    print(helmetson)

    print('\n\nPeople in Space: ', helmetson['number'])
    for h in helmetson:
        print (h[0] + h[1] + "\n")
    people = helmetson['people']
    print(people)

if __name__ == "__main__":
    main()
