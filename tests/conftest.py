import json
import pytest
import selenium.webdriver

@pytest.fixture
def config(scope="session"):

    # Read the file
    with open('config.json') as config_file:
        config = json.load(config_file)

    # Assert values are acceptable
    assert config['browser'] in ['Firefox', 'Chrome', 'Headless Chrome']
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0

    return config

@pytest.fixture
def browser(config):
    
    # initialize ChromeDriver
    if config['browser'] == 'Firefox':
        dr = selenium.webdriver.Firefox()
    elif config['browser'] == 'Chrome':
        dr = selenium.webdriver.Chrome()
    elif config['browser'] == 'Headless Chrome':
        opts = selenium.webdriver.ChromeOptions()
        opts.add_argument('headless')
        dr = selenium.webdriver.Chrome(options=opts)
    else:
        raise Exception('Browser not supported')

    # make its calls wait up to 10 seconds for elements to appear
    dr.implicitly_wait(config['implicit_wait'])

    # return the driver object
    yield dr

    # close the browser window
    dr.quit()