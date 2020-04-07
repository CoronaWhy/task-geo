Style Guide
===========

Overview
--------
This document describes a few principles of style for work related to the Geo Task Force.

The primary goal of these style guidelines is to improve code readability so that everyone,
whether reading the code for the first time or maintaining it for the future,
can quickly determine what the code does. Secondary goals are to design systems that are simple,
to increase the likelihood of catching bugs quickly, and avoiding arguments when there are
disagreements over subjective matters.

Philosophy
----------

Lazy programming
****************
Write what you need and no more, but when you write it, do it right.

Avoid implementing features you don’t need. You can’t design a feature without knowing what
the constraints are. Implementing features "for completeness" results in unused code that is
expensive to maintain, learn about, document, test, etc.

When you do implement a feature, implement it the right way. Avoid workarounds.
Workarounds merely kick the problem further down the road, but at a higher cost:
someone will have to relearn the problem, figure out the workaround and how to dismantle it
(and all the places that now use it), and implement the feature.
It’s much better to take longer to fix a problem properly, than to be the one who fixes everything
quickly but in a way that will require cleaning up later.

You may hear team members say "embrace the yak shave!". This is an encouragement to take on the
larger effort necessary to perform a proper fix for a problem rather than just applying a band-aid.

Write Test, Find Bug
********************

When you fix a bug, first write a test that fails, then fix the bug and verify the test passes.

When you implement a new feature, write tests for it.

If something isn’t tested, it is very likely to regress or to get "optimized away".
If you want your code to remain in the codebase, you should make sure to test it.

Don’t submit code with the promise to "write tests later". Just take the time to write the tests
properly and completely in the first place.

Coding format
*************
We will be adhering to `PEP-8`_ standards as closely as possible. These are widely accepted standards
for how good, clean code should look. Let's keep things tidy!

At any moment you can check your code is compliant of PEP8 by running::

    make lint

Beyond the PEP-8, all coding should follow the `Zen of Python`_.

Naming and module conventions
*****************************

Beyond the naming conventions included in the PEP-8, some other conventions will be followed by
the Geo Task Force:

- Avoid using the type in the name of variables, names should say WHAT it is, not HOW::

   .. code-block :: python

   country_list = [...]  # NO!
   countries = [...]     # YES!

   my_source_df = ...    # NO!
   my_source = ...       # YES!


- Avoid using abbreviations in variables::

   .. code-block :: python

    flt_cntry_cs = ...              # NO!
    filtered_country_cases = ...    # YES!

Always remember that names not only for interfaces as functions and their arguments, but also
for internal variables should be:

- **Descriptive**: One should have a general idea of whats inside of the variable just by reading
  it's name.

- **Concise**: That means short, but also clear. We need to be descriptive with the minimum possible
  amount of words.

- **Meaningful**: The names should make sense in the context in which they belong.



Other resources
***************

- `Best practices for data science code`_
- `Minimum sufficient pandas`_
- `The codeless code`_


.. _PEP-8: https://www.python.org/dev/peps/pep-0008/
.. _Zen of Python: https://www.python.org/dev/peps/pep-0020/#id2
.. _Best practices for data science code: https://www.kaggle.com/rtatman/six-steps-to-more-professional-data-science-code
.. _Minimum sufficient pandas: https://medium.com/dunder-data/minimally-sufficient-pandas-a8e67f2a2428
.. _The codeless code: http://thecodelesscode.com/