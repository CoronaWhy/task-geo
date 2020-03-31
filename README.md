# CoronaWhy Geography Task Force

<p align="left">
<img width=15% src="https://uploads-ssl.webflow.com/5e729ef3ef0f906b804d4f27/5e77e9db1ede36135bbb1927_logo%203%402x.png" alt=“CoronaWhy” />

<i>A worldwide effort by volunteers to fight Coronavirus (COVID-19)</i>
</p>


![CI](https://github.com/CoronaWhy/task-geo/workflows/CI/badge.svg)


Help us understand how geography affects virality.

- Documentation: https://CoronaWhy.github.io/task-geo
- Task-Geo Homepage: https://github.com/CoronaWhy/task-geo
- Main Coronawhy Homepage: https://www.coronawhy.org/


## About CoronaWhy

CoronaWhy is a crowd-sourced team of over 350 engineers, researchers, project managers, and all sorts of other professionals with diverse backgrounds who joined forces to tackle the greatest global problem of today--understanding and conquering the COVID-19 pandemic. This team formed in response to the Kaggle CORD-19 competition to synthesize the flood of new knowledge being generated every day about COVID-19. The goal for the organization is to inform policy makers and care providers about how to combat this virus with knowledge from the latest research at their disposal.


## About CoronaWhy Geo Task 

The goal of our team is to understand how geography affects the spread of the virus. We are currently focusing on two streams:
* In close collaboration with #task-risk and #task-ties, we identify potential risk factors for the spread of COVID-19, extract data about such risk factors from various sources, and perform analyses to assess teir impact on the spread of the virus. Examples of such risk factors are population density in a region, temperature, humidity, social distancing policies in place, ... an many others!
* Using Natural Language Processing on a vast dataset of scientific papers, we try to support the expert's understanding on how location might impact the effects of the virus. For example, one of our goals is to map clinical studies to the region where they were performed and to present a simple interface to the wider comunity to visualize their distribution.

## About CoronaWhy Geo Task Force

We are an international team of 15 people with different backgrounds (and growing!), all united to understand how geography impacts the spread of COVID-19.

*List of collaborators (pending)*

## Datasets

*Pending*

# Install

Also, although it is not strictly required, the usage of a [virtualenv](https://virtualenv.pypa.io/en/latest/)
is highly recommended in order to avoid interfering with other software installed in the system.

These are the minimum commands needed to create a virtualenv using python3.6 for **task-geo**:

```bash
pip install virtualenv
virtualenv -p $(which python3.6) task-geo
```

Afterwards, you have to execute this command to activate the virtualenv:

```bash
source task-geo/bin/activate
```

Remember to execute it every time you start a new console to work on **task-geo**!


With your virtualenv activated, you can clone the repository and install it from
source by running `make install-deveop` on the `stable` branch:

```bash
git clone git@github.com:CoronaWhy/task-geo.git
cd task-geo
git checkout stable
make install-develop
```

Now you have the code installed on your local system, and you are ready to help us with your contribution, but first, please have a look at the [Contributing Guide](https://CoronaWhy.github.io/task-geo/contributing.html).
