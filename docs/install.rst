Installation
============

The quickest way to get started using **task-geo** is to launch a
`Binder <https://mybinder.org/>`__ environment.

Please click on the |Binder| button and follow the example notebooks!

However, you if you have to contribute changes to the code or run it in
a different environment you will want to install it on your own.

Native Python
-------------

On UNIX-line systems such as MacOS and GNU/Linux, **Task Geo** can be
installed natively using Python.

For this, you will need to first clone the repository and the execute
``make install`` inside it.

.. code:: bash

    git clone https://github.com/CoronaWhy/task-geo.git
    cd task-geo
    make install

If you plan to contribute to the code, please check our `Contributing
Guide <https://CoronaWhy.github.io/task-geo/contributing.html>`__ for
more details about how to properly setup your environment.

.. note:: Installing the library in Windows natively is not recommended,
          so if you are running a Windows system we recommend you to either switch
          to a UNIX-Like environment, or use the Docker installation method
          explained below.

Docker
------

**Task Geo** is also prepared to be run inside a docker environment
using ``docker-compose``.

This is not the ideal setup for development, but can be used to run the
software on a Windows environment.

For this, make sure to have both
`docker <https://docs.docker.com/install/>`__ and
`docker-compose <https://docs.docker.com/compose/install/>`__ installed
on your system and then follow these steps:

1. Clone this repository and go into the ``task-geo`` folder:

.. code:: bash

    git clone https://github.com/CoronaWhy/task-geo.git
    cd task-geo

2. Start a Jupyter Notebook inside a docker container.

.. code:: bash

    docker-compose up --build

3. Point your browser at http://127.0.0.1:8888

.. |Binder| image:: https://mybinder.org/badge_logo.svg
   :target: https://mybinder.org/v2/gh/CoronaWhy/task-geo/master?filepath=notebooks
