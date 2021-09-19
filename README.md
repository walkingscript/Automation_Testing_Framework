# AUTOMATION TESTING FRAMEWORK

Requirements:
    
`Python 3.9`
`Allure`
`Chrome`
`FireFox`

For fast run on Windows you just need to install Python 3.9 and run "fast_run.bat".
Thus, python will automatically set up virtual environment and download required packages.
After, it'll run demo test.

For Linux:

    pip install -m venv venv
    source venv/bin/activate
    pip install --upgrade pip
    pip install -r requirements.txt

For Windows:

    pip install -m venv venv
    venv\scripts\activate
    pip install --upgrade pip 
    pip install -r requirements.txt

Test runs from root directory under your virtual environment:

    pytest --alluredir=artifacts/allure_data/chrome/ --clean-alluredir -m demo_test

Some key params are present in pytest addopts (pytest.ini).

Good Luck!
