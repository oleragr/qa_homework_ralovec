# Web UI Testing framework
Simple custom testing framework with python and py.test

## Setup Steps

1. Install python 3+ version
2. Install and create virtualenv
3. Activate virtualenv
4. Install required dependency's: `pip install -r requirements.txt`
5. This step is only for Windows users:
    Install pywin32 (How to do that you can find in section "**Install pywin32**")
   
###  Task 1 
Test sketches for Task 1 can be found in tests/api_tests/toggle_user_status_api_test.py

### Run tests for Task 2
``py.test tests/web_tests/homework_web_test.py::TestHomeworkWeb::test_herokuapp``

### Run tests for Task 3
``py.test tests/web_tests/homework_web_test.py::TestHomeworkWeb::test_globalsqa``

### Requirements

`pip install -r {Requirement_file}` - With this command you can install all required packages from file

`requirements.txt` Only for testing

### Install pywin32
This is needed for screenshot testing

1. Download the exe yourself (https://github.com/mhammond/pywin32/releases)
2. Activate your virtualenv
3. Run easy_install DOWNLOADED_FILE.exe
