import pytest
from selenium import webdriver
from base.webdriver_factory import WebDriverFactory


@pytest.fixture()
def setUp():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")


@pytest.fixture(scope="class")
def oneTimeSetUp(request, browser):
    print("Running one time setUp")
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()
    # if browser == 'chrome':
    #     baseURL = "http://northstar-stage.us-east-1.elasticbeanstalk.com"
    #     # driver = webdriver.Chrome(ChromeDriverManager().install())
    #     driver = webdriver.Chrome("C:\\Users\\hjasani\\PycharmProjects\\Personal_Projects\\Python_Selenium\\SeleniumSessions\\chromedriver_win32_106\\chromedriver.exe")
    #     driver.maximize_window()
    #     driver.implicitly_wait(5)
    #     driver.get(baseURL)
    #     print("Running tests on Chrome")
    # else:
    #     baseURL = "http://northstar-stage.us-east-1.elasticbeanstalk.com"
    #     driver = webdriver.Firefox(executable_path="C:\\Users\\hjasani\\PycharmProjects\\Personal_Projects\\Python_Selenium\\SeleniumSessions\\chromedriver_win32_106\\chromedriver.exe")
    #     driver.get(baseURL)
    #     print("Running tests on Firefox")

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print("Running one time tearDown")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")