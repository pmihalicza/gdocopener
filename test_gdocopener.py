import gdocopener as gd
import pytest

def test_open_url_in_chrome():
    gdoc_url = 'https://imdb.com'
    returncode = gd.open_url_in_chrome(gdoc_url)
    assert returncode == 0, 'Something went wrong with opening the URL in Chrome'

def test_extract_url_from_gdoc():
    gdoc_content = '{' \
                   '"url": "https://www.hengerurtartalom.com"' \
                   '}'
    extracted_url = gd.extract_url_from_gdoc(gdoc_content)
    assert extracted_url == 'https://www.hengerurtartalom.com', \
        'The extracted URL  is not correct'

def test_opening_no_gdoc_file(capsys):
    gdoc_file = 'not_a_gdoc_file.txt'
    with pytest.raises(SystemExit):
        gd.check_file_extension_and_open_file(gdoc_file)
    captured = capsys.readouterr()

    assert captured.out == 'This was not a Google Docs file, so gdocopener passed it over to the text editor.\n'

def test_nonJSON_content(capsys):
    gdoc_content = 'This is not JSON'
    with pytest.raises(SystemExit):
        gd.extract_url_from_gdoc(gdoc_content)
    captured = capsys.readouterr()

    assert captured.out == 'The file you want to open is not a valid Google Docs file (aka JSON file)!\n', \
        'NonJSON files ' \
                                                                                                    'are not handled correctly'

def test_opening_nonexisting_text_file(capsys):
    gdoc_file = 'thisdoesnotexists.txt'
    with pytest.raises(SystemExit):
        gd.check_file_extension_and_open_file(gdoc_file)
    captured = capsys.readouterr()

    assert captured.out == 'This was not a Google Docs file, so gdocopener passed it over to the text editor.\n', \
        'Not existing text files are not handled correctly'

def test_opening_nonexisting_gdoc_file(capsys):
    gdoc_file = 'thisdoesnotexists.gdoc'
    with pytest.raises(SystemExit):
        gd.check_file_extension_and_open_file(gdoc_file)
    captured = capsys.readouterr()

    assert captured.out == 'The Google Docs file you want to open does not exist!\n', 'Not existing gdoc iles are not ' \
                                                                               'handled ' \
                                                                        'correctly'

def test_opening_gdoc_extension():
    assert False

def test_opening_gsheet_extension():
    assert False

def test_opening_gslides_extension():
    assert False

def test_bad_text_editor():
    assert False