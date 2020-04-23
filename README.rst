git_nb
============

Python package to execute basic git command in notebook.

Installation
------------
Using pip :

.. code:: sh

    pip install git_nb


Example
-------

Clone a repository
~~~~~~~~~~~~~~~~~~

.. code:: python

    from git_nb import Repo

    repo = Repo(username="yohann84L", repo_name="git_nb")
    repo.git_clone()

Pull
~~~~

.. code:: python

    repo.git_pull()
