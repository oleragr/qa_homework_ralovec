import pytest

from configfiles.config import ConfigLoader
from base.webdriverfactory import WebDriverFactory


@pytest.yield_fixture(autouse=True)
def setUp(request, browser):
    if request.node.get_closest_marker('api') is not None:
        print("Running class setUp without browser")
        yield None
    else:
        print(f"Running class setUp for {browser}")
        wdf = WebDriverFactory(browser)
        driver = wdf.getWebDriverInstance()
        if request.cls is not None:
            request.cls.driver = driver
        yield driver
        driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser", default='chrome')
    parser.addoption("--env", action='store', default='test')


@pytest.fixture(scope="session")
def conf():
    return ConfigLoader().get_configuration()


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def env_cli(request):
    return request.config.getoption("--env")
