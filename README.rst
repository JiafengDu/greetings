greetings
#############################

.. note::

  This README was auto-generated. Maintainer: please review its contents and
  update all relevant sections. Instructions to you are marked with
  "PLACEHOLDER" or "TODO". Update or remove those sections, and remove this
  note when you are done.

|pypi-badge| |ci-badge| |codecov-badge| |doc-badge| |pyversions-badge|
|license-badge| |status-badge|

Purpose
*******

An extension to open edx instance that exposes a REST API endpoint and saves a greeting from the user. 
If the greeting is "hello", then the view of this API endpoint calls the original greeting endpoint again with "goodbye" as the parameter.

Getting Started
***************

Developing
==========

One Time Setup
--------------
.. code-block::

  # Clone the repository
  git clone git@github.com:openedx/greetings.git
  cd greetings

  # Set up a virtualenv using virtualenvwrapper with the same name as the repo and activate it
  mkvirtualenv -p python3.8 greetings


Every time you develop something in this repo
---------------------------------------------
.. code-block::

  # Activate the virtualenv
  workon greetings

  # Grab the latest code
  git checkout main
  git pull

  # Install/update the dev requirements
  make requirements

  # Run the tests and quality checks (to verify the status before you make any changes)
  make validate

  # Make a new branch for your changes
  git checkout -b <your_github_username>/<short_description>

  # Using your favorite editor, edit the code to make your change.
  vim ...

  # Run your new tests
  pytest ./path/to/new/tests

  # Run all the tests and quality checks
  make validate

  # Commit all your changes
  git commit ...
  git push

  # Open a PR and ask for review.

Deploying
=========

Add the app to the Open Edx platform that is running in tutor development mode (tutor dev)
------------------------------------------------------------------------------------------
.. code-block::
  # Create (or open existing) docker-compose.override.yml file
  nano "$(tutor config printroot)/env/dev/docker-compose.override.yml"

  # Add there the volume mapping so the project will be available inside the container without the need to rebuild it
  version: "3.7"
  services:
    lms:
      volumes:
        - <PATH-To-APP-DIRECTORY>:/mnt/greetings

  # Run tutor dev start -d to restart container with the new volume

  # Install the app
  docker exec -it tutor_dev-lms-1 bash
  cd /mnt/greetings
  python setup.py develop

  # While in the session, also migrate the new model
  python manage.py makemigrations greetings
  python manage.py migrate

  # Restart the container
  docker restart tutor_dev-lms-1

Add the app to the production mode (tutor local)
------------------------------------------------
.. code-block::
  # Install the project as a pip package by:
  # add it to the "$(tutor config printroot)"/config.yml
  OPENEDX_EXTRA_PIP_REQUIREMENTS:
  - git+https://github.com/jiafengdu/greetings.git

More Help
=========

For questions specific to this plugin, please contact Jiafeng

License
*******

The code in this repository is licensed under the AGPL 3.0 unless
otherwise noted.

Please see `LICENSE.txt <LICENSE.txt>`_ for details.

Contributing
************

Contributions are very welcome.
Please read `How To Contribute <https://openedx.org/r/how-to-contribute>`_ for details.

This project is currently accepting all types of contributions, bug fixes,
security fixes, maintenance work, or new features.  However, please make sure
to have a discussion about your new feature idea with the maintainers prior to
beginning development to maximize the chances of your change being accepted.
You can start a conversation by creating a new issue on this repo summarizing
your idea.

The Open edX Code of Conduct
****************************

All community members are expected to follow the `Open edX Code of Conduct`_.

.. _Open edX Code of Conduct: https://openedx.org/code-of-conduct/

People
******

The assigned maintainers for this component and other project details may be
found in `Backstage`_. Backstage pulls this data from the ``catalog-info.yaml``
file in this repo.

.. _Backstage: https://open-edx-backstage.herokuapp.com/catalog/default/component/greetings

Reporting Security Issues
*************************

Please do not report security issues in public. Please email dujiafengdave@gmail.com


.. |status-badge| image:: https://img.shields.io/badge/Status-Experimental-yellow
