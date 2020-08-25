"""
Name:UKHUREBOR OSAGIE NATHANIEL
StudentID:MSE0103

---------------------------
Question 1:

Write a program in the python programming language:
- Enter a person's name to search
- Read Contact list form URL: https://api.androidhive.info/contacts/
- print the search results yes or no and the person's position in the list in case of yes.

"""

# import pandas for data preprocessing
import pandas as pd

# import requests to load the contact list from the web
import requests

# the url to the contact list
contact_list_url = "https://api.androidhive.info/contacts/"

def get_contact_data(url=contact_list_url):
    """
    get_contact_data loads the data from https://api.androidhive.info/contacts/
    using the request lib.

    Then processes the data in a tabular structure with the help of pandas

    Parameters
    ----------
    url : url, optional
        The url to where the data is stored, by default contact_list_url

    Returns
    Pandas DataFrame :
        Return a pandas object
    """    ""
    contact_data = requests.get(url).json()

    return pd.json_normalize(contact_data["contacts"])


def name_query_search():
    """
    name_query_search gets the person's name.
    Looks up the data to search the data that the name exist.
    If the name exist, it prints yes and the position.
    Otherwise, it prints No, the name was not found.

    PS: It was deduced that there were no duplicate names therefore it was safe to say that if
    the number of names found was 1, then the name exist and if it was 0, the it does not exist.
    """    ""

    # load the data
    df = get_contact_data()

    # get the person's name
    person_name = input("Please enter your name: \n")

    # query the data
    query = df[df["name"] == person_name]

    if len(query)==1:
        print(f"Yes, Your name: {person_name} was found on the list and your position on the list is {query.index.tolist()} \n ")

    elif len(query)==0:
        print(f"Unfortunately {person_name} was not found on the list")



# Test the function to see if the functions answers our question
name_query_search()
