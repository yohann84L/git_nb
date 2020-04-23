echo "Deleting old version"
rm -rf dist/
rm -rf build/

echo "Build package"
python setup.py sdist bdist_wheel

echo "Push package to pypi"
twine check dist/*
twine upload --verbose --repository-url https://upload.pypi.org/legacy/ dist/*