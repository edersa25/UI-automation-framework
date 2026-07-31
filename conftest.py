import os

import pytest

from utils.config import BASE_URL


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        page = item.funcargs.get("page")

        if page:

            os.makedirs("screenshots", exist_ok=True)

            filename = f"screenshots/{item.name}.png"

            page.screenshot(path=filename)


@pytest.fixture
def website_url():
    return BASE_URL
