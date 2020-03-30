Data sources
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
   
It has to follow the following rules:

- It doesn't have a fixed set of arguments, as it depends from the data we are trying to retrieve. It's not the same a function that downloads a file, and has no need for arguments, that a function that connects to an API allowing for 5 diferent parameters.

- It will, however, allow to be used with the least possible amount of parameters, that is, accept as many defaults as make sense.

- It will, imperativemet, return a `pandas.DataFrame`

- It will have a docstring explaining its arguments and type.

- All access to external data, as mapping of reference values should be done at this step.

- It will be named xxxx_connector where xxxx is the name of the source.


Formatter specification
=======================

A formatter is a function that recieves as only argument, the `pandas.DataFrame` returned by the connector, and returns a `pandas.DataFrame` following the Data Model specification. It has a prototype:


.. code-block :: python

    def xxx_formatter(raw):
    """Formats data retrieved from xxx.
    
    Arguments:
        raw(pandas.DataFrame): 
        
    Returns:
        pandas.DataFrame    
    """
    ... # pandas magic happens here
    
    return formatted_dataset


It has to follow the following rules:

- It will have as a single argument a `pandas.DataFrame` and return a `pandas.DataFrame` too.

- The returned `pandas.DataFrame` must follow the Data Model.

- It will named `xxx_formatter` where `xxx` is the name of the source.

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

- It will have the same exact arguments that it's connector and will return a `pandas.DataFrame`.
- It will be importable from top-module level, that is:

    .. code-block :: python
    
        from task_geo.data_sources.xxx import xxx

- As a bonus point, it's nice to include a notebook or a little script working as both 'usage documentation' and 'end-to-end' test.