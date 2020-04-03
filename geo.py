import argparse
import json
import os
import requests

GEO_URL = "https://api.scratchstats.com/scratch/users/${0}"

def get_arguments():
    parser = argparse.ArgumentParser(description="Find out user's location")
    inputs = parser.add_mutually_exclusive_group(required=True)
    inputs.add_argument("-s", dest="username", nargs="*", help="Username. Will return the country code of the user.")

    return parser.parse_args()

def get_location(arguments):
    if arguments.username is not None:
        username = arguments.username
    url = GEO_URL.format(username[0])
    r = requests.get(url)
    if r.status_code != 200:
        raise RuntimeError("GET {0} failed with status code {1}".format(r.status_code, url))
    
    user_formatted = r.json()

    print(user_formatted)
    return user_formatted


def main():
    arguments = get_arguments()
    location = get_location(arguments)


if __name__ == "__main__":
    main()