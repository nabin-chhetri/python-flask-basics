# Python & Flask
## Install Python3
```bash 
$ sudo apt install python-is-python3
```

## Install venv package to create virtual environment
```bash 
$ sudo apt install python3-venv
```

## Create virtual environment using venv
```bash
$ python3 -m venv <virtual_env_name>

# Example: create virtual environment named my_virt_env

$ python3 -m venv my_virt_env
```

## Activate virtual environment
- For Linux
```bash
$ source <virtual_env_name>/bin/activate

# Example:

$ source my_virt_env/bin/activate
```

## Install Pip3 to install pip3 packages
```bash 
$ sudo apt install python3-pip
```


## Install Python Pip3 packages
```bash 
$ pip3 install <package_name>

# Example: Install sqlalchemy 

$ pip3 install sqlalchemy 
```

## Run a webserver.py using python http.server
```bash
$ python3 webserver.py
```

## Run server.py that communicates with SQLite database using SQLAlchemy
Note : Required Files
- server.py
- database_setup.py
- restarantmenu.db
```bash
$ python3 server.py
```

## Run listofmenus.py to populate data to the restaurantsmenu.db 
```bash
python3 listofmenus.py
```
