import gdocopen as gd

def test_open_url_in_chrome():
    gdoc_url = 'https://imdb.com'
    returncode = gd.open_url_in_chrome(gdoc_url)
    assert returncode == 0, 'Something went wrong with opening the URL in Chrome'

def test_extract_url_from_gdoc():
    gdoc_file = '/home/peti/Dropbox/test_gdoc_file.gdoc'
    assert gd.extract_url_from_gdoc(gdoc_file) == 'https://www.dropbox.com/cloud_docs/view/#############', \
        'THe URL extracted is not right'