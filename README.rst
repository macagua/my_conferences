==============
My conferences
==============

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |tech-docs| |odoo13-docs| |help|
    * - tests
      - | |python37| |odoo13| |travis| |coverall|
    * - license
      - |github-license|
    * - contribute
      - |github-issues| |github-forks| |github-contributors|
    * - share
      - |share-twitter| |github-stars|

.. |tech-docs| image:: http://img.shields.io/badge/tutorial-docs-875A7B.svg?style=flat&colorA=8F8F8F
    :target: http://www.erpish.com/odoo/step-by-step-tutorial-for-how-to-create-a-hello-world-application-for-odoo/
    :alt: Documentation Source

.. |odoo13-docs| image:: http://img.shields.io/badge/13.0-docs-875A7B.svg?style=flat&colorA=8F8F8F
    :target: https://www.odoo.com/documentation/13.0/index.html
    :alt: Odoo 13 Documentation

.. |help| image:: http://img.shields.io/badge/master-help-875A7B.svg?style=flat&colorA=8F8F8F
    :target: https://www.odoo.com/forum/help-1
    :alt: Odoo Help

.. |share-twitter| image:: https://img.shields.io/twitter/url?url=https%3A%2F%2Fgithub.com%2Fmacagua%2Fmy_conferences
    :target: https://twitter.com/intent/tweet?text=Download%20and%20use%20%27my_conferences%27%20package%20for%20doing%20Python%20trainings%20in%20Venezuela%20%F0%9F%87%BB%F0%9F%87%AA%20https://github.com/macagua/my_conferences
    :alt: Share at Twitter

.. |github-contributors| image:: https://img.shields.io/github/contributors/macagua/my_conferences.svg
    :target: https://github.com/macagua/my_conferences/graphs/contributors
    :alt: Github Contributors

.. |github-license| image:: https://img.shields.io/github/license/macagua/my_conferences.svg
    :target: https://github.com/macagua/my_conferences/blob/master/LICENSE
    :alt: Github License

.. |github-issues| image:: https://img.shields.io/github/issues/macagua/my_conferences
    :target: https://github.com/macagua/my_conferences/issues
    :alt: Github Issues

.. |github-forks| image:: https://img.shields.io/github/forks/macagua/my_conferences
    :target: https://github.com/macagua/my_conferences/network/members
    :alt: Github Forks

.. |github-stars| image:: https://img.shields.io/github/stars/macagua/my_conferences
    :target: https://github.com/macagua/my_conferences/stargazers
    :alt: Github Favorites

.. |python37| image:: https://img.shields.io/badge/Python-3.7-blue
    :target: https://www.python.org/downloads/release/python-375/
    :alt: Python 3.7.5 version

.. |odoo13| image:: https://img.shields.io/badge/Odoo-13-blue
    :target: https://github.com/odoo/odoo/tree/13.0
    :alt: Odoo 13 version

.. |travis| image:: https://travis-ci.org/macagua/my_conferences.svg?branch=master
    :target: https://travis-ci.org/macagua/my_conferences
    :alt: Travis-CI Build Status

.. |coverall| image:: https://coveralls.io/repos/github/macagua/my_conferences/badge.svg?branch=master
    :target: https://coveralls.io/github/macagua/my_conferences?branch=master
    :alt: Coveralls Checkout Status

.. end-badges

About
=====

My conferences, is an Odoo 13 module to ease the management of conferences,
you can manage registration of guests as well as resources.

This Odoo module let you manage:

- manage conferences.

Dependencies
============

This module requires the following dependencies:

- odoo 13 > https://github.com/odoo/odoo


Install
=======

Download the source code:

::

    $ git clone https://github.com/macagua/my_conferences.git


Move ``my_conferences`` folder into ``extra-addons`` Odoo directory:

::

    $ mv my_conferences /full/path/to/extra-addons/


Restart the Odoo instance server, login and got to **Apps** > **My conferences** > **Install**

.. figure:: https://raw.githubusercontent.com/macagua/my_conferences/master/static/description/install_module.png
    :align: center
    :width: 70%
    :alt: Install 'My conferences' Module

    Install 'My conferences' Module

Then go to Main menu at left top corner and click to **Manage Conferences** and click to **Edit** button for edit it or click to **Create** or create a new conference.

.. figure:: https://raw.githubusercontent.com/macagua/my_conferences/master/static/description/manage_conferences.png
    :align: center
    :width: 70%
    :alt: Access to 'Manage Conferences' Menu

    Access to 'Manage Conferences' Menu


Testing
=======

For run the module tests, with the following command:

::

    $ /full/path/to/odoo-bin --addons-path=/full/path/to/addons,/full/path/to/extra-addons \
      -d t -i my_conferences --test-enable --stop-after-init --log-level=test


Contribute
==========

- Issue Tracker: https://github.com/macagua/my_conferences/issues

- Source Code: https://github.com/macagua/my_conferences


License
=======

- The project is licensed under the AGPL-3.


References
==========

- `Step by Step Tutorial for How to create a Hello World Application for Odoo! <http://www.erpish.com/odoo/step-by-step-tutorial-for-how-to-create-a-hello-world-application-for-odoo/>`_.

- `Automated testing in Odoo <https://www.surekhatech.com/blog/automated-testing-in-odoo>`_.

- `Odoo Experience 2018 - Improve the Quality of Your Modules with Automated Tests <https://www.youtube.com/watch?v=jZddEWFdUcM>`_.

