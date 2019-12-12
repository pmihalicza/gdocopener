from sys import argv
from subprocess import call
import platform
import json

def extract_url_from_gdoc(gdoc_file):
    """This function opens the gdoc_file, reads its JSON contents and parses it. It then extracts and returns the URL to
    the Docs file."""
    try:
        with open(gdoc_file, 'r') as file:
            content = file.read()

            json_dict = json.loads(content)
            return json_dict['url']

    except FileNotFoundError:
        error = 'The file you want to open does not exist!'
        print(error)
        return error

    except json.JSONDecodeError:
        error = 'The file you want to open is not a valid gdoc file (aka JSON file)!'
        print(error)
        return error


def open_url_in_chrome(gdoc_url):
    """This function takes the url of the gdoc file and opens it in the Chrome browser.
    The function chooses the appropriate command to start Chrome based on the user's current OS."""

    if platform.system() == 'Linux':
        command = 'google-chrome'
    elif platform.system() == 'Windows':
        command = 'Chrome.exe'

    try:
        return call([command, gdoc_url])
    except FileNotFoundError:
        print('Could not run Chrome. Maybe it is not installed?')
        return 1

if __name__ == '__main__':
    if len(argv) > 1:
        gdoc_file = argv[1]
        gdoc_path = extract_url_from_gdoc(gdoc_file=gdoc_file)

        open_url_in_chrome(gdoc_path)
    else:
        print('You should pass a file as an argument to gdocopen!')
