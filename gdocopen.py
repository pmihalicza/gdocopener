from sys import argv

def extract_url_from_gdoc(gdoc_file):
    pass

def open_url_in_chrome(gdoc_path):
    command = "google-chrome".join(gdoc_path)
    run(command)

if __name__ == '__main__':
    gdoc_file = argv[1]
    gdoc_path = extract_url_from_gdoc(gdoc_file=gdoc_file)
    open_url_in_chrome(gdoc_path)