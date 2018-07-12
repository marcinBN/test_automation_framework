
usage: run_test.py [-h] -f {test_search.py} [-e {dev,stage,prod}]

optional arguments:
  -h, --help            show this help message and exit
  -f {test_search.py}, --file {test_search.py}
                        Test filename
  -e {dev,stage,prod}, --env {dev,stage,prod}
                        Environment


python run_test.py -e prod -f test_search.py
