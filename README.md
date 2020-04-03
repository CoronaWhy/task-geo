# CoronaWhy Geography Task Force

<p align="left">
<img width=15% src="https://uploads-ssl.webflow.com/5e729ef3ef0f906b804d4f27/5e77e9db1ede36135bbb1927_logo%203%402x.png" alt=“CoronaWhy” />

<i>A worldwide effort by volunteers to fight Coronavirus (COVID-19)</i>
</p>


![CI](https://github.com/CoronaWhy/task-geo/workflows/CI/badge.svg)
![docs](https://github.com/CoronaWhy/task-geo/workflows/Docs/badge.svg)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/CoronaWhy/task-geo/master?filepath=notebooks)


Help us understand how geography affects virality.

- Documentation: https://CoronaWhy.github.io/task-geo
- Task-Geo Homepage: https://github.com/CoronaWhy/task-geo
- Main Coronawhy Homepage: https://www.coronawhy.org/


## About CoronaWhy

CoronaWhy is a crowd-sourced team of over 550 engineers, researchers, project managers, and all sorts of other professionals with diverse backgrounds who joined forces to tackle the greatest global problem of today--understanding and conquering the COVID-19 pandemic. This team formed in response to the Kaggle CORD-19 competition to synthesize the flood of new knowledge being generated every day about COVID-19. The goal for the organization is to inform policy makers and care providers about how to combat this virus with knowledge from the latest research at their disposal.


## About CoronaWhy Task Geo Tea,

The Geo Task Team is a subgroup of the CoronaWhy team, it is formed by an interdisciplinary group of volunteers from across the world focused on understand how the many different geography-related factors may affect the spread of the virus.

The team is currently being led by Daniel (@DanielRobertNicoud) and Manuel (@ManuelAlvarezC), please direct any inquiries or issues with permissions to either of these two.

We are currently focusing on two streams:

* In collaboration with #task-risk and #task-ties, we identify potential geography-related risk factors for the spread of COVID-19, extract data about such risk factors from various sources and perform analyses to assess their impact on the spread of the virus.

* Using Natural Language Processing on the CORD-19 dataset, we try to support the expert's understanding on how geography-related factors (meterology, demographics, ...) might impact the effects on the the virus. For example, one of our goals is to map clinical studies to the region where they were performed and to present a simple interface to the wider comunity to visualize their distribution.


# Usage Example

In this short example we show you how to use the NOAA Data Source to download data from all the
France Stations over a period of time as a `pandas.DataFrame`.

```python3
from datetime import datetime
from task_geo.data_sources.noaa import noaa_api

start_date = datetime(2020, 1, 1)
end_date = datetime(2020, 1, 15)
countries = ['FR']

data = noaa_api(countries, start_date, end_date)
```

The returned `data` variable will be a `pandas.DataFrame` containing a table such as:

| atitude | longitude | elevation | country | name              | date       | station     |  tmax |  tmin |
|---------|-----------|-----------|---------|-------------------|------------|-------------|-------|-------|
| 48.0689 |   -1.7339 |        36 | France  | RENNES-ST JACQUES | 2020-01-01 | FR000007130 |  10.4 |   4.8 |
| 48.0689 |   -1.7339 |        36 | France  | RENNES-ST JACQUES | 2020-01-02 | FR000007130 |  11   |   7.8 |
| 48.0689 |   -1.7339 |        36 | France  | RENNES-ST JACQUES | 2020-01-03 | FR000007130 |  13.1 | nan   |
| 48.0689 |   -1.7339 |        36 | France  | RENNES-ST JACQUES | 2020-01-04 | FR000007130 |  10.4 |   1.4 |
| 48.0689 |   -1.7339 |        36 | France  | RENNES-ST JACQUES | 2020-01-05 | FR000007130 |   9.5 |   3   |
| 48.0689 |   -1.7339 |        36 | France  | RENNES-ST JACQUES | 2020-01-06 | FR000007130 | nan   |  -1.5 |
|     ... |       ... |       ... | ...     | ...               | ...        | ...         |    ...|   ... |

# Try it out!

The quickest way to get started using **task-geo** is to launch a [Binder](https://mybinder.org/) environment:

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/CoronaWhy/task-geo/master?filepath=notebooks) 

Please click at the button above and follow the example notebooks!

# What's next?

Please check our [documentation](https://CoronaWhy.github.io/task-geo) site to learn more about
the different data sources and about how to get startet contributing to the project.

