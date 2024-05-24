# Exam 'gcore.com/hosting' Page

## Description

This project is an examination work for the module Selenium + pytest.

## Installation

1. Clone the repository:
```
git clone https://github.com/RustamMust/gcore.com-hosting-page.git
```

2. Install the virtual environment:
```
python3 -m venv venv
```

3. Establish dependencies:
```
pip install -r requirements.txt
```


## How to use the project

1. Main file for running tests:
```
test_hosting_page.py
```
2. Generate an Allure report:
```
pytest -s -v --aluredir=allureresults
```
3. View the Allure report:
```
allure serve allureresults
```
