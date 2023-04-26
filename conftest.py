import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    """add option for change language"""
    parser.addoption('--language', action='store', default='en',
                     help="Choose language if uphold")


@pytest.fixture(scope="function")
def browser(request):
    try:
        user_language = request.config.getoption("language")
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        # options.add_argument("--no-sandbox")  # if you want open a browser
        # options.add_argument("--headless")    # commented
        # options.add_argument("--disable-gpu") # this strings
        browser = webdriver.Chrome(options=options)
        browser.implicitly_wait(5)
        yield browser
    except pytest.UsageError:
        raise pytest.UsageError("--language = [en | fr | ru ...][default=en] --browser_name=[should be chrome | firefox][default=chrome]")
    finally:
        print("\nquit browser..")
        browser.quit()

