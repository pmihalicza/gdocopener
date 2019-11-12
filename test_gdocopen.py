import gdocopen as gd
import unittest

class MyTestCLass(unittest.TestCase):
    def test_open_url_in_chrome(self):
        gdoc_url = 'https://imdb.com'
        gd.open_url_in_chrome(gdoc_url)

        self.assertEqual()

if __name__ == '__main__':


    gdoc_file = '/home/peti/Dropbox/test_gdoc_file.gdoc'
    print(gd.extract_url_from_gdoc(gdoc_file) == 'httnps://www.dropbox.com/cloud_docs/view/#############')