Data Sources
------------


What is a data source?
======================

A data source is a function that is able to retrieve data available anywhere (may it be a website, webservice, FTP, file,..)  and return in a format compatible with the Data Model specification.

Usually a data source is composed of two parts:

1. A **connector**: Handles the retrieval of the raw data.
2. A **formatter**: Transform the raw data to follow the data model specification.


We get into the details for each component in the following sections

Connector specification
=======================

A connector is a function that handles the retrieval of data, it follows the prototype:

.. code-block :: python

    def xxx_connector(*args, **kwargs):
        """Retrieves data from xxxx.

        Arguments:
            argument_1(type): Explanation of what it does
            ...

        Returns:
            pandas.DataFrame
        """
        ...
        return pandas.DataFrame(...)

It must follow these rules:

- It doesn't have a fixed set of arguments, as it depends from the data we are trying to retrieve.
  It's not the same a function that downloads a file, and has no need for arguments, that a function
  that connects to an API accepting for 5 diferent parameters.

- It allows, however, use with the least possible amount of parameters, that is,
  accepting as many default arguments as possible.

- It must return a ``pandas.DataFrame``.

- It have a docstring explaining its arguments and type.

- All access to external data, as mapping of reference values is done at this step.

- It's named ``xxxx_connector`` where ``xxxx`` is the name of the source.


Formatter specification
=======================

A formatter is a function that recieves as only argument the ``pandas.DataFrame`` returned by the
connector, and returns a ``pandas.DataFrame`` following the Data Model specification.
It has a prototype:


.. code-block :: python

    def xxx_formatter(raw, *args, **kwargs):
        """Formats data retrieved from xxx.

        Arguments:
            raw(pandas.DataFrame):

        Returns:
            pandas.DataFrame
        """
        ... # pandas magic happens here

        return formatted_dataset


It must follow these rules:

- Its first argument is a ``pandas.DataFrame`` and return a ``pandas.DataFrame`` too.
  In case that the connector allows to multiple formats and/or metrics in the data, additional parameters
  can be passed to the formatter too.

- The returned ``pandas.DataFrame`` must follow the Data Model.

- It'snamed ``xxx_formatter`` where ``xxx`` is the name of the source.

- It should not access to any external data.


Data source specification
=========================

Data sources are functions that retrieve data and format them to follow the Data Model, internally, shouldn't be more complex than:

.. code-block :: python

    def xxx(*args, **kwargs):
        """Data Source for xxx.

        Arguments:
            argument_1(type):
            ...

        Returns:
            pandas.DataFrame
        """
        data = xxx_connector(*args, **kwargs)
        return xxx_formatter(data)


It have to follow the rules:

- It will have the same exact arguments that it's connector and will return a ``pandas.DataFrame``.
- It will be importable from top-module level, that is:

.. code-block :: python

    from task_geo.data_sources.xxx import xxx


Examples and documentation
==========================

To help other members of CoronaWhy getting started using task_geo data sources, we will include
along our submission a notebook in the `notebooks/examples` folder containing the following:

1. An explanation of the diffent argument the data source requires, it's type, expected format
   and values.
2. A minimal basic usage of the data source provided, that is, leaving all optional arguments
   with their default values.

This notebook will be rendered along the documentation in the section `Examples`_ of the
documentation. Try to be as clear and concise as you can with the explanation of the usage and
parameters of your data source, as some of the potential users may not a high technical level.

To help other members of our team who may need to use, modify or improve our work, we should
include complete docstrings in the high-level API we provide, the docstring should contain:

- Brief description of what the object does.
- List of arguments, its type and a brief description.
- An simple, minimal and complete example of usage.

For a complete reference of how to format the docstrings, please check the
`Google docstrings style`_.


Tests
=====

As per the Contributing Guide you are required to add unit tests to your submissions, beyond that, a
compliance test for your formatter is also required, the test should be done in the following way.

1. Retrieve some data using your `connector`, and store 50 rows in a csv file.
2. Create a fixture in ``tests/folders``.
3. Create a unit test that loads your fixture, passes it to your formatter and then passes the
   result to ``task_geo.testing.check_dataset_format``, more or less like this:

.. code-block :: python

    from task_geo.data_sources.my_datasource.my_datasource_formatter import my_formatter
    from task_geo.testing import check_dataset_format

    class TestMyDataSourceFormatter(TestCase):
        ...
        def test_formatter(self):
            """Validate formatter output for datasource xxx."""
            # Setup
            fixture = pd.read_csv('tests/fixtures/myfixture.csv')

            # Run
            data = my_datasource_formatter(fixture)

            # Check
            check_dataset_format(data)


Data audit and metadata
=======================

To make the results of our work usable not only to other members of the Coronawhy team, but also
by academics who may be interested, we need to follow the `DataPackage`_ specification.

In order to do so, we need to implement two documents along the code of our data source.


datapackage.json
****************

Below have a minimal example of what your datapackage.json must contain.

.. code-block :: none

    {
        "title": "",
        "subtitle": "",
        "description": "",
        "resources": [{
            "description": "",
            "schema": {
                "fields": [
                    {
                        "name": "",
                        "description": "",
                        "type": ""
                    },
                    ...
                ]
            }
        }],
        "keywords": [
            "coronawhy",
        ]
    }

audit.md
********

Here we should describe the origin of the data, the transformations that our code has done in order
to match our Data Model, it should follow this template:

.. code-block :: none

    # {DATASET_NAME}

    ## General information

    - **Description**: Explain briefly what kind of data the dataset provides.
    - **Credits**: Authors of the original data.
    - **Source**: Link to the raw source.

    ## Description

    For each column add a node with with the following:
    **Column Name**
    - Description:
    - Type:
    - Units: (Where make sense)

    ## Transformations applied

    (List all the transformation done to your data from the moment you retrieve it, to the
    moment your data source returns it, this includes, but is not limited to:
    - Filtering
    - Aggregation
    - Merging
    - Enriching
    - Decoding / Encoding
    - Change of Units
    - Adding/removing columns
    - ...
    )


Data Source module structure
============================

A valid data source submission, is composed of a module, a notebook with examples and tests
should look like this:

.. code-block :: none

    task_geo/
        data_sources/
            my_data_source/
                __init__.py
                __main__.py
                my_data_source_connector.py
                my_data_source_formatter.py
                datapackage.json
                audit.md

    notebooks/
        examples/
            my_dataset_example.ipynb

    tests/
        data_sources/
            my_data_source/
                test_formatter.py


.. _Examples: https://github.com/CoronaWhy/task-geo/issues
.. _Google docstrings style: https://google.github.io/styleguide/pyguide.html?showone=Comments#Comments
.. _DataPackage: https://specs.frictionlessdata.io/data-package/#introduction
