# CoronaWhy Geography Task Force

<p align="left">
<img width=15% src="https://uploads-ssl.webflow.com/5e729ef3ef0f906b804d4f27/5e77e9db1ede36135bbb1927_logo%203%402x.png" alt=“CoronaWhy” />

<i>A worldwide effort by volunteers to fight Coronavirus (COVID-19)</i>
</p>


![CI](https://github.com/CoronaWhy/task-geo/workflows/CI/badge.svg)
![docs](https://github.com/CoronaWhy/task-geo/workflows/Docs/badge.svg)


Help us understand how geography affects virality.

- Documentation: https://CoronaWhy.github.io/task-geo
- Task-Geo Homepage: https://github.com/CoronaWhy/task-geo
- Main Coronawhy Homepage: https://www.coronawhy.org/


## About CoronaWhy

CoronaWhy is a crowd-sourced team of over 350 engineers, researchers, project managers, and all sorts of other professionals with diverse backgrounds who joined forces to tackle the greatest global problem of today--understanding and conquering the COVID-19 pandemic. This team formed in response to the Kaggle CORD-19 competition to synthesize the flood of new knowledge being generated every day about COVID-19. The goal for the organization is to inform policy makers and care providers about how to combat this virus with knowledge from the latest research at their disposal.


## About CoronaWhy Task Geo Tea,

The Geo Task Team is a subgroup of the CoronaWhy team, it's formed by a group of multidisciplinar people from across the world focused on understand how the many different geography-related factors may affect the spread of the virus.

The team is currently being led by Daniel (@DanielRobertNicoud) and Manuel (@ManuelAlvarezC), please direct any inquiries or issues with permissions to either of these two.

We are currently focusing on two streams:

* In collaboration with #task-risk and #task-ties, we identify potential geography-related risk factors for the spread of COVID-19, extract data about such risk factors from various sources and perform analyses to assess their impact on the spread of the virus.

* Using Natural Language Processing on the CORD-19 dataset, we try to support the expert's understanding on how geography-related factors (meterology, demographics, ...) might impact the effects on the the virus. For example, one of our goals is to map clinical studies to the region where they were performed and to present a simple interface to the wider comunity to visualize their distribution.


# Install

## General recomendations

Also, although it is not strictly required, the usage of a [virtualenv](https://virtualenv.pypa.io/en/latest/)
is highly recommended in order to avoid interfering with other software installed in the system.

These are the minimum commands needed to create a virtualenv using python3.7 for **task-geo**:

```bash
pip install virtualenv
virtualenv -p $(which python3.7) task-geo
```

Afterwards, you have to execute this command to activate the virtualenv:

```bash
source task-geo/bin/activate
```

Remember to execute it every time you start a new console to work on **task-geo**!

## Installation for users

You should use this instructions if you plan to **USE** this repository.

With your virtualenv activated, you can clone the repository and install it from
source by running `make install`:

```bash
git clone https://github.com/CoronaWhy/task-geo.git
cd task-geo
make install
```

Now you are ready to go!

## Installation for developers

If you plan to **CONTRIBUTE**, here's how to set up `task-geo` for local development.
With your virtualenv activated, you can fork the repository, clone your fork locally and install by running `make install-develop`:

1. Fork the `task-geo` repo on GitHub.
2. Clone your fork locally and install it using `make install-develop`:

```
git clone git@github.com:your_name_here/task-geo.git
cd task-geo/
make install-develop
```

Now you have the code installed on your local system, and you are ready to help us with your contribution, but first, please have a look at the [Contributing Guide](https://CoronaWhy.github.io/task-geo/contributing.html).

