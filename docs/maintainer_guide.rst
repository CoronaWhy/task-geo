Maintainer Guide
================

This document purpose is to define and concrete the tasks related to maintaining the github repository
to have a detailed description of each of the task to serve as both:

1. Reference for Mantainers of the repository
2. Guide for users who may be interested in improve it's contribution workflow.


Issues
------

Issues can be classified into three types:

- **Bug reports**

- **Feature requests**

- **Tasks**

Let's see them in more detail:

Bug reports
***********

Bug reports are communications that something is not working as intended. They should follow this guideline:

+ **Title**
  Short but concise, must refer to the component failing and the type of error and the context.
  Examples of good titles are::

    XXXX Exception on function path.to.function
    XXXX Exception on function path.to.function when calling with parameter param=value
    Error when doing $something on OS

  Examples of bad titles are::

    Error             # not descriptive
    xxx crash         # doesn't refer to a component
    wrong values      # doesn't refer to a component

The general idea is that reading the title of an issue can give a general idea of what the bug is.
This will make it easier for people searching the bug reports to filter what they can do, and also
for users trying to find a bug related to a problem they may have.

+ **General information:**

  * Commit SHA or version of package when available. ( This will help us locate the error, and
    make sure it hasn't been fixed yet).
  * OS version: This can help replicate OS specific issues.
  * Python version: This can help replicate python-version specific issues.

- **Description:** This is where the main explanation of what happened, here the user must explain
  not only what they did, but what they intended to do, in order to avoid to fix something that is
  working properly but is not being used properly.

- **Code snippet:** It should provide a `minimal, complete and reproducible example`_ of the issue
  being reported.

- **Traceback:** If the bug reported causes a crash, the traceback should be posted in the
  *Additional Content* section.

- **Dependencies:** If the bug reported caused a crash, or we have suspicions that the issue may be
  happening in some call to an external dependency, the actual dependency list the user has
  installed maybe required. ( It can be obtained with ``pip freeze``)


All the contents listed above should serve to an only purpose: Help duplicate and identify the issue.

Bug report workflow
...................

After a bug report is created, it passes through 4 stages:

1. **Verification:** This is the stage where we make sure we are able to duplicate the issue.
   We will ask for whatever information is needed in order to replicate the bug, when this step
   is completed, we create a branch using the naming convention 
   ``gh-$(ISSUE_NUMBER)-$(TITLE OF THE ISSUE)`` and add a test that replicate the bug being
   reported and push it to the main repository.
   
   The build shall fail, meaning that we have been able to reproduce the bug. At this point the tag 
   ``Ready to start`` can be added. If the issue is specially easy to solve, the tag ``good first issue``
   can be added too.

   In the case that the bug is not such, for example, bad usage from the user, or correct, 
   albeit unexpected behavior, the tag ``wontfix`` can be added and the issue closed.

2. **Assignement:** After we create the branch, we create a Trello card linking it to the github issue
   and explaining the problem, the project manager will find someone to fix the bug.

3. **Development:** After the project manager finds somebody to fix the bug, this is the stage where the
   bug is actually fixed.
4. **Resolution:**. After the bug has been fixed, the changes are submited with a Pull Request.


Feature requests
****************

Feature requests are request for improvements in our package.

They should include two parts:

- **Motivation:** Either something that is not correct and can be improved, or a new feature they
  consider the package should provide.

- **Proposal of solution:** How they propose the issue to be solved, or how, in general terms, they
  whish the behavior was after everything is solved.

Feature request workflow
........................

After a feature request is created, it passes through 4 steps:

1. **Verification and design:** After receiving the feature request, we must make sure that the proposal:
   
   a) Makes sense in the scope of this project and his motivations.
   b) It's doable with the resources available.
   c) It's consistent with the behavior of the rest of the package.

   If any of this requisites is not filled, we will add the `wontfix` tag and close the issue.
   If all three requisites are fulfilled, then we will start studying the proposal of solution if 
   exist, or to design it according the reported desired behavior. To do so we should take in
   consideration:
   
   a) What structures will be required to be created?
   b) Which inputs, outputs and functionality will have each part?
   c) How will it be used by the final user?
   d) Are components in our codebase with similar functionality to any of the components that
      can be used, or modified to fulfill the requirements?
   e) In which part of the repository should be added this components?
   f) There will be any potential conflicts with other components?

   We will add the design proposal in a comment.

2. **Assignement:** After we create the branch, we create a Trello card linking it to the github
   issue and a brief summary of the design proposal, the project manager will find someone to
   implement it.

3. **Development:** After the project manager finds somebody to implement the feature, this is
   the stage where coding happens.

4. **Resolution:**. After the feature has been, the changes are submited with a Pull Request.


Support
*******

Support issues came from users who tried to use our package but the the documentation ( or the
lack of thereof) wasn't helpful enough to get the results they wanted.

Usually this issues don't require developing code, just explaining the user how to use our package.
In the case that documentation is missing or incomplete, a Pull Request can be open to improve the
documentation.

Tasks
*****

Tasks are related to issues created from Trello and contain improvements to be done discussed
in the trello card or for which general documentation already exists, so no further work for the
maintainer is required.


Pull requests
-------------

Pull Requests are open by collaborators who whish their work to be included in the repository.

The review process has the following steps:

1. **Review of General format:** This is the first and preliminary stage, where we simply review 
   that the general format of the PR is correct, this include answering the following questions:

   - There is an issue related to the Pull Request?
   - Are the items on the checklist checked? The ones that are not, do they have a reason for? Could
     the review process continue without these?
   - Is there a description of the changes included?

   If any of this questions is answered with a NO, we must go to the collaborator and ask him to made
   the corresponding changes.

2. **Continous Integration / Build**: Github will automatically launch a build job for every new
   Pull Request that is open, that will run the tests and linters. If the build fails, we will add
   the ``ci-fail`` label and ask the submitter to fix it. If the build passes, we add the ``ci-ok``
   label and move to the next step.

3. **Output / notebooks / examples / documentation format:** Now we will review that the outputs 
   and the components behavior is as expected, usually this can be done with:

   - Cloning the fork/ checking out the branch
   - Create a new virtualenv and install from scratch the module
   - Run the notebooks provided, if any, seeing if the outputs change with the ones submitted.
   - Generate the docs and review the docs added for the submission.
   - Use the public API and see that the output is compliant with the specifications.

   If we found any issues, we will add the ``output-fail`` label and ask for the changes. If 
   everything is ok, we add the ``output-ok`` label and continue to the next step.

4. **Peer review / Code review:** This is the final step, where we read the code and analyze it 
looking for flaws, things that should be looked include:

   - Good naming practices
   - Code redundancy
   - Readability
   - Coherent APIs (arguments, defaults, types)
   - Structured code
   - Good use of external libraries.

   All issues that are found should be explained and with a proposed change. After the changes are
   made, the PR can be merged.









.. _minimal, complete and reproducible example: https://stackoverflow.com/help/minimal-reproducible-example