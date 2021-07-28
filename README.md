# cookie_analyzer

### Python setup
    Install Python 3 from - 
        https://realpython.com/installing-python/
        https://www.python.org/downloads/

### Setup the Project
```
pip install . 
```

#### Let's say you want to install a package named foo. Then you do,
```
$ git clone https://github.com/AdityaMisra/super-duper-carnival.git  
$ cd super-duper-carnival
$ python setup.py install
```

#### Instead, if you don't want to actually install it but still would like to use it. Then do,
```
$ python setup.py develop
```

### Run from command line
```
$ python cookie_analyzer.py  -h
usage: cookie_analyzer.py [-h] [-f F] [-d D]

This program returns a list of most active cookies for a given date

optional arguments:
  -h, --help  show this help message and exit
  -f F        Path of the cookie log file
  -d D        Date for which we've to fetch the most active cookie
                        
$ python cookie_analyzer.py -f resources/cookie_log.csv -d 2018-12-09
```

### Sample output
```
$ python cookie_analyzer.py -f resources/cookie_log.csv -d 2018-12-09
Printing most freq cookie(s) for the date ->  2018-12-09
AtY0laUfhglK3lC7

```

### How to run the tests
* This command runs the unit test in verbose mode
    ```
    pytest . -v

    ```