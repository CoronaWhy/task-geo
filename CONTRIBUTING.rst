.. highlight:: shell

============
Contributing
============

Welcome
-------

Welcome to the team! The CoronaWhy Geo Task Force is excited to have you be part of this incredible
crowd-sourced effort to better understand and synthesize COVID-19-related literature.
The main focus of our task force is centered around three goals:

- Provide high-quality data to complement the literature provided by #task-risk on geographical
  risk factors for the spread of COVID-19.
- Extract information to enable compelling visualizations of what is currently happening by #data-viz .
- Extract important geographic location data from the corpus of scientific papers to help domain experts
  select the most relevant literature for various topics.

Everyone is welcome to contribute code via pull requests, file issues on GitHub,
add to our documentation, or to help out in any other way, and their work will be greatly
appreciated! Every little bit helps, and credit will always be given.

If you are interested in getting involved ping @Daniel Robert-Nicoud or @Manuel Alvarez in the
`CoronaWhy slack team`_.

We will be communicating primarily through the Slack #task-geo channel. Project management/task
delegation will be visible on the team's Trello board (ping @Marie Bjerede to get access to that).

Your hard work is invaluable in making quick, actionable progress on understanding the state of
the world with regard to the combatting this terrible pandemic. THANK YOU.

You can contribute in many ways:

Types of Contributions
----------------------

Report Bugs
~~~~~~~~~~~

Report bugs at the `GitHub Issues page`_.

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

Fix Bugs
~~~~~~~~

Look through the GitHub issues for bugs. Anything tagged with "bug" and "help
wanted" is open to whoever wants to implement it.

Implement Features
~~~~~~~~~~~~~~~~~~

Look through the GitHub issues for features. Anything tagged with "enhancement"
and "help wanted" is open to whoever wants to implement it.

Write Documentation
~~~~~~~~~~~~~~~~~~~

task-geo could always use more documentation, whether as part of the
official task-geo docs, in docstrings, or even on the web in blog posts,
articles, and such.

Submit Feedback
~~~~~~~~~~~~~~~

The best way to send feedback is to file an issue at the `GitHub Issues page`_.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions are welcome :)

Get Started!
------------

Ready to contribute? Here's how to set up `task-geo` for local development.

1. Fork the `task-geo` repo on GitHub.
2. Clone your fork locally::

    $ git clone git@github.com:your_name_here/task-geo.git

3. Install your local copy into a virtualenv. Assuming you have virtualenvwrapper installed,
   this is how you set up your fork for local development::

    $ mkvirtualenv task-geo
    $ cd task-geo/
    $ make install-develop

4. Create a branch for local development::

    $ git checkout -b name-of-your-bugfix-or-feature

   Try to use the naming scheme of prefixing your branch with ``gh-X`` where X is
   the associated issue, such as ``gh-3-fix-foo-bug``. And if you are not
   developing on your own fork, further prefix the branch with your GitHub
   username, like ``githubusername/gh-3-fix-foo-bug``.

   Now you can make your changes locally.

5. While hacking your changes, make sure to cover all your developments with the required
   unit tests, and that none of the old tests fail as a consequence of your changes.
   For this, make sure to run the tests suite and check the code coverage::

    $ make lint       # Check code styling
    $ make test       # Run the tests
    $ make coverage   # Get the coverage report

6. When you're done making changes, check that your changes pass all the styling checks and
   tests, including other Python supported versions, using::

    $ make test-all

7. Make also sure to include the necessary documentation in the code as docstrings following
   the `Google docstrings style`_.
   If you want to view how your documentation will look like when it is published, you can
   generate and view the docs with this command::

    $ make view-docs

8. Commit your changes and push your branch to GitHub::

    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature

9. Submit a pull request through the GitHub website.

Pull Request Guidelines
-----------------------

Before you submit a pull request, check that it meets these guidelines:

1. It resolves an open GitHub Issue and contains its reference in the title or
   the comment. If there is no associated issue, feel free to create one.
2. Whenever possible, it resolves only **one** issue. If your PR resolves more than
   one issue, try to split it in more than one pull request.
3. The pull request should include unit tests that cover all the changed code
4. If the pull request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring, and add the
   feature to the documentation in an appropriate place.
5. The pull request should work for all the supported Python versions. Check the `Github Build
   Status page`_ and make sure that all the checks pass.
6. If you are working on the task-geo team, please make one of your team mates review your code before
   submitting the PR.
7. Have a look at older PR for the same kind of submission, and check that your code is compliant
   of the comments made to them, and the rationale behind them.

Unit Testing Guidelines
-----------------------

All the Unit Tests should comply with the following requirements:

1. Unit Tests should be based only in unittest and pytest modules.

2. The tests that cover a module called ``task_geo/path/to/a_module.py``
   should be implemented in a separated module called
   ``tests/task_geo/path/to/test_a_module.py``.
   Note that the module name has the ``test_`` prefix and is located in a path similar
   to the one of the tested module, just inside the ``tests`` folder.

3. Each method of the tested module should have at least one associated test method, and
   each test method should cover only **one** use case or scenario.

4. Test case methods should start with the ``test_`` prefix and have descriptive names
   that indicate which scenario they cover.
   Names such as ``test_some_methed_input_none``, ``test_some_method_value_error`` or
   ``test_some_method_timeout`` are right, but names like ``test_some_method_1``,
   ``some_method`` or ``test_error`` are not.

5. Each test should validate only what the code of the method being tested does, and not
   cover the behavior of any third party package or tool being used, which is assumed to
   work properly as far as it is being passed the right values.

6. Any third party tool that may have any kind of random behavior, such as some Machine
   Learning models, databases or Web APIs, will be mocked using the ``mock`` library, and
   the only thing that will be tested is that our code passes the right values to them.

7. Unit tests should not use anything from outside the test and the code being tested. This
   includes not reading or writing to any file system or database, which will be properly
   mocked.

Tips
----

To run a subset of tests::

    $ python -m pytest tests.test_task_geo
    $ python -m pytest -k 'foo'


.. _GitHub issues page: https://github.com/CoronaWhy/task-geo/issues
.. _Github Build Status page: https://github.com/CoronaWhy/task-geo/actions
.. _Google docstrings style: https://google.github.io/styleguide/pyguide.html?showone=Comments#Comments
.. _CoronaWhy slack team: https://join.slack.com/t/coronawhy/shared_invite/zt-cw83m6ds-p4AwsMV65tha2joKhn~s5Q
