Installing Instructions
========

## Required Packages

* Python
* Git
* pip
* virtualenv

eg, on Ubuntu:

    sudo apt-get install git python python-pip
    sudo pip install virtualenv


eg, on Mac

    sudo easy_install pip
    sudo pip install virtualenv

Installation
------------

* Get the code from github:

  ```git clone https://github.com/HIVis-Tools/serverH.git```

* Create the temp folder:
 
  ```mkdir serverH/server/hivis/static/temp```
* Build the virtualenv:
 
 ```virtualenv --python=python2.7 serverH/venv```

* Install the python dependencies:
 
 ```serverH/venv/bin/pip install -r serverH/requirements.txt```

* You may need to run the following to apply migrations:

 ```serverH/venv/bin/python manage.py migrate```

Running Django
-------
Once all of that is done you can run the app thorugh Djago like this:

```
cd serverH/server/
../venv/bin/python manage.py runserver
```

Then you can just chck it running at [http://localhost:8000/hivis/input_page](http://localhost:8000/hivis/input_page)
