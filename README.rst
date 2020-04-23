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

Set your config
~~~~~~~~~~~~~~~

.. code:: python

    from git_nb import cfg

    cfg.username = "yourusername"
    cfg.email = "youremail"

Clone a repository
~~~~~~~~~~~~~~~~~~

If the repository is private, you will be invited to write your password.

.. code:: python

    import git_nb
    from git_nb import cfg

    cfg.repo_name = "yourrepo"
    git_nb.git_clone()

Pull
~~~~

.. code:: python

    import git_nb

    git_nb.git_pull()
