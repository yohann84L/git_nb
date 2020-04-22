```
python setup.py sdist bdist_wheel
twine check dist/*
twine upload --verbose --repository-url https://upload.pypi.org/legacy/ dist/*
```