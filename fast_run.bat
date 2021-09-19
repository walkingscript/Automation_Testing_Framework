@echo off

if not exist ".\venv" (
    python -m venv venv
)

venv\scripts\python -m pip install --upgrade pip
venv\scripts\python -m pip install -r requirements.txt

SET ALLURE_CHROME_DIR=artifacts/allure_data/chrome/
SET ALLURE_FIREFOX_DIR=artifacts/allure_data/firefox/

venv\scripts\python -m pytest --alluredir=%ALLURE_CHROME_DIR% --clean-alluredir -m demo_test
START allure serve %ALLURE_CHROME_DIR%

SET WEB_BROWSER=firefox
venv\scripts\python -m pytest --alluredir=%ALLURE_FIREFOX_DIR% --clean-alluredir -m demo_test
START allure serve %ALLURE_FIREFOX_DIR%

@pause
