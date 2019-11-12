import gdocopen as gd

if __name__ == '__main__':

    gdoc_url = 'https://imdb.com'
    gd.open_url_in_chrome(gdoc_url)

    gdoc_file = '/home/peti/Dropbox/test_gdoc_file.gdoc'
    print(gd.extract_url_from_gdoc(gdoc_file) == 'https://www.dropbox.com/cloud_docs/view/#############')