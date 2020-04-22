from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='gitnb',
      version='0.1',
      description='Python package to execute git command in notebook',
      long_description=readme(),
      url='http://github.com/yohann84L/gitnb',
      keywords="git python repo repository pull clone notebook nb",
      author='Yohann Lereclus',
      author_email='lereclus84L@gmail.com',
      license='MIT',
      packages=['gitnb'],
      zip_safe=False)
