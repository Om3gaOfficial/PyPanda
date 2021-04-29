
# PyPanda 0.0.1
![](https://img.shields.io/badge/python-3.6-blue.svg) ![](https://img.shields.io/badge/python-3.7-blue.svg) ![](https://img.shields.io/badge/python-3.8-blue.svg) ![](https://img.shields.io/badge/python-3.9-blue.svg)


`PyPanda` is an easy to use [Python 3](https://www.python.org/) based library providing simple and easy access to the API of [Bitpanda](https://www.bitpanda.com/) and [Bitpanda Pro](https://www.bitpanda.com/pro).

`PyPanda` will be updated regularly and will someday have all features implemented as an trouble-free to use function.

---
### Liberies used
The `pypanda.py` file uses only two liberies at the moment.

 - [requests](https://pypi.org/project/requests/)
 - json (implemented in Python)
---
### How to use
#### Installation
I am currently working to publish this libery on [PyPi](https://pypi.org/) then you should be able to use `pip install pypanda`. Until then please just clone the Github Repo or use `pypanda.py` file.
Please be sure that you have installed the liberies listed above

#### Using the libery
The libery currently just supports the Bitpanda API completly. The implementation of the Bitpanda Pro API will come in future versions. But please see the `CHANGELOG.md` file for further information about alle changes.

##### Examples

###### Bitpanda
```python
import PyPanda

PyPandaClient = PyPanda.BitPandaClass
print(PyPandaClient.getWallets("APIKey", True))
```

##### Bitpanda Pro
```python
import PyPanda
  
PyPandaClient = PyPanda.BitPandaProClass
print(PyPandaClient.getCurrentPrices())
```
---
### Latest changes
Nothing here yet

---
### Contact
To report issues, bugs, docu corrections or to propose new features use preferably [Github Issues](https://github.com/Om3gaOfficial/PyPanda/issues).
