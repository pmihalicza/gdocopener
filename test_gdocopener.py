import gdocopen as gd
import pytest

def test_open_url_in_chrome():
    gdoc_url = 'https://imdb.com'
    returncode = gd.open_url_in_chrome(gdoc_url)
    assert returncode == 0, 'Something went wrong with opening the URL in Chrome'

def test_extract_url_from_gdoc():
    gdoc_file = '/home/peti/Dropbox/test_gdoc_file.gdoc'
    extracted_url = gd.extract_url_from_gdoc(gdoc_file)
    assert extracted_url == 'https://www.dropbox.com/cloud_docs/view/#############', \
        'THe extracted URL  is not correct'

def test_extract_url_from_gdoc_with_nonJSON_file():
    gdoc_file = '/home/peti/Dropbox/randomfile.txt'
    extracted_url = gd.extract_url_from_gdoc(gdoc_file)

    assert extracted_url == 'The file you want to open is not a valid gdoc file (aka JSON file)!', 'NonJSON files are not handled correctly'

def test_extract_url_from_doc_with_nonexisting_file():
    gdoc_file = '/home/peti/Dropbox/thisdoesnotexists.txt'
    extracted_url = gd.extract_url_from_gdoc(gdoc_file)

    assert extracted_url == 'The file you want to open does not exist!', 'Not existing files are not handled correctly'