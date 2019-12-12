from sys import argv
from subprocess import call
import platform
import json
import os.path
import sys


def check_file_extension_and_open_file(file_to_open, text_editor='gedit'):
    """This function checks if the file-to-be-opened is actually a Google Docs (gdoc, gsheet, gslides) file or not.
    If not, then the file is passed to the the text editor and gdocopener exits. (This is necessary, because Linux
    makes file
    associations
    based on file types and not on file extensions.) If it is Google Docs file indeed, it returns its contents."""

    _, extension = os.path.splitext(file_to_open)
    if extension not in ['.gdoc', '.gsheet', '.gslides']:
        print('This was not a Google Docs file, so gdocopener passed it over to the text editor.')
        try:
            return call([text_editor, file_to_open])
        except FileNotFoundError:
            print('Could not run the text editor. Maybe not installed?')
        finally:
            sys.exit()

    try:
        with open(file_to_open, 'r') as file:
            return file.read()

    except FileNotFoundError:
        print('The Google Docs file you want to open does not exist!')
        sys.exit()



def extract_url_from_gdoc(gdoc_content):
    """This function parses the file contents. If it is not JSON, it notifies the user and exits. If it is JSON,
    extracts and returns the URL to the Docs file."""

    try:
        json_dict = json.loads(gdoc_content)
        return json_dict['url']

    except json.JSONDecodeError:
        print('The file you want to open is not a valid Google Docs file (aka JSON file)!')
        sys.exit()


def open_url_in_chrome(gdoc_url):
    """This function takes the url of the gdoc file and opens it in the Chrome browser. The function chooses the
    appropriate command to start Chrome based on the user's current OS."""

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
        file_to_open = argv[1]

        content = check_file_extension_and_open_file(file_to_open=file_to_open)
        gdoc_path = extract_url_from_gdoc(gdoc_content=content)
        open_url_in_chrome(gdoc_path)
    else:
        print('You should pass a file as an argument to gdocopener!/n Usage: python gdocopener.py [filename]')
