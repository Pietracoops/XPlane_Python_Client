# XPlaneApi Packaging instructions


* First create the software distribution:
```
python setup.py sdist
```

* Install Twine:
```
pip install twine
```

* Upload to PyPi using twin
```
twine upload dist/*
```