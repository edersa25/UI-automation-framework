# UI Automation Framework

A professional UI automation testing framework built with **Python**, **Playwright**, and **Pytest** using the **Page Object Model (POM)** design pattern.

## Project Overview

This project automates common user workflows on the Sauce Demo e-commerce application and demonstrates industry-standard UI automation practices.

The framework was built to showcase:

* UI automation with Playwright
* Page Object Model
* Pytest fixtures
* Parameterized tests
* Smoke and regression test organization
* Cross-browser testing
* Parallel execution
* HTML reporting
* Automatic screenshots on failure
* Logging
* Environment variable management
* GitHub Actions CI

## Technologies

* Python 3.12
* Playwright
* Pytest
* Pipenv
* Pytest-HTML
* Pytest-xdist
* python-dotenv
* GitHub Actions

## Project Structure

```text
pages/
tests/
utils/
data/
logs/
reports/
screenshots/
```

## Features

* Login validation
* Successful login
* Invalid login scenarios
* Locked user validation
* Product page verification
* Add product to cart
* Cross-browser execution
* Parallel execution
* Automatic screenshots on failure
* HTML test reports
* Logging
* CI pipeline

## Running the Project

Install dependencies:

```bash
pipenv install
```

Install Playwright browsers:

```bash
pipenv run playwright install
```

Run all tests:

```bash
pipenv run pytest
```

Run in headed mode:

```bash
pipenv run pytest --headed
```

Run in Firefox:

```bash
pipenv run pytest --browser=firefox
```

Run in WebKit:

```bash
pipenv run pytest --browser=webkit
```

Run in parallel:

```bash
pipenv run pytest -n auto
```

Generate an HTML report:

```bash
pipenv run pytest --html=reports/report.html --self-contained-html
```

## Future Improvements

* Checkout workflow automation
* Visual regression testing
* API/UI integration testing
* Database validation
* Docker support
* Test data generation
* Allure reporting

## Author

Built as a portfolio project while transitioning into QA Automation Engineering.
