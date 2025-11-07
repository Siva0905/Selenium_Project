# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

# Example: make the webdriver fixture configurable via pytest -k/parametrize
# Usage: @pytest.mark.parametrize("browser", ["chrome","firefox"])
@pytest.fixture(scope="function")
def driver(request):
    browser = getattr(request, "param", "chrome")
    if browser == "chrome":
        svc = ChromeService(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new")  # remove if you want visible browser
        drv = webdriver.Chrome(service=svc, options=options)
    elif browser == "firefox":
        svc = FirefoxService(GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")
        drv = webdriver.Firefox(service=svc, options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    drv.implicitly_wait(5)
    yield drv
    drv.quit()
