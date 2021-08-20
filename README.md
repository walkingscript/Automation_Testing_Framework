# TEST FRAMEWORK DEVELOPMENT

For fast run on Windows you just need to install Python 3.9 and run "start.bat".
At the first time, this file automaticaly creates virtual environment and downloads required packages.
After, that is runs the tests.

For manual run of this project needs Python 3.9 interpreter and virtual environment.

Download Python you can here: https://www.python.org/ Don't forget to add python to your environment variable in process of install.

After that, you should to create virtual environment in the project folder and install requirements. For that in console type next commands.

For Linux:

    pip install -m venv ./venv
    source venv\bin\activate
    pip install -r requirements.txt

For Windows:

    pip install -m venv ./venv
    venv\scripts\activate
    pip install -r requirements.txt

To run project type:

    cd project
    pytest -v -p no:cacheprovider --html=artifacts/index.html --self-contained-html

Good Luck!
