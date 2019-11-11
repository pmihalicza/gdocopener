from sys import argv
from subprocess import call
import platform

def extract_url_from_gdoc(gdoc_file):
    pass

def open_url_in_chrome(gdoc_url):
    '''This function takes the url to the gdoc file and opens it in the Chrome browser.
    The function chooses the appropriate command to start Chrome based on the user's current OS'''

    if platform.system() == 'Linux':
        command = 'google-chrome'
    elif platform.system() == 'Windows':
        command = 'Chrome.exe'

    call([command, gdoc_url])

if __name__ == '__main__':
    gdoc_file = argv[1]
    gdoc_path = extract_url_from_gdoc(gdoc_file=gdoc_file)

    open_url_in_chrome(gdoc_path)
