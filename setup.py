from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(
    name='git_nb',
    version='0.1.2',
    description='Python package to execute git command in notebook',
    long_description=readme(),
    long_description_content_type="text/x-rst",
    url='http://github.com/yohann84L/git_nb',
    keywords="git python repo repository pull clone notebook nb",
    author='Yohann Lereclus',
    author_email='lereclus84L@gmail.com',
    license='MIT',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=['git_nb'],
    zip_safe=False
)
