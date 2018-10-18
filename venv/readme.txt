Virtal python environment.
    assuming python3 and pip3 have been installed (sudo apt-get install python3-pip python3-venv):

one time setup of venv:
$ python3 -m venv ./venv
$ pip3 install -r ./venv/requirements.txt

each time before usage:
$ source ./venv/bin/activate

each time after usage:
$ deactivate



