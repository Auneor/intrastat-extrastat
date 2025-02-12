==========================================
Product Harmonized System Codes - Delivery
==========================================

.. !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! This file is generated by oca-gen-addon-readme !!
   !! changes will be overwritten.                   !!
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

.. |badge1| image:: https://img.shields.io/badge/maturity-Beta-yellow.png
    :target: https://odoo-community.org/page/development-status
    :alt: Beta
.. |badge2| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |badge3| image:: https://img.shields.io/badge/github-OCA%2Fintrastat--extrastat-lightgray.png?logo=github
    :target: https://github.com/OCA/intrastat-extrastat/tree/16.0/product_harmonized_system_delivery
    :alt: OCA/intrastat-extrastat
.. |badge4| image:: https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :target: https://translation.odoo-community.org/projects/intrastat-extrastat-16-0/intrastat-extrastat-16-0-product_harmonized_system_delivery
    :alt: Translate me on Weblate
.. |badge5| image:: https://img.shields.io/badge/runbot-Try%20me-875A7B.png
    :target: https://runbot.odoo-community.org/runbot/227/16.0
    :alt: Try me on Runbot

|badge1| |badge2| |badge3| |badge4| |badge5| 

The OCA module *product_harmonized_system* adds a many2one field *hs_code_id* on product templates that points to an *H.S. Code* object. But the *delivery* module from the official addons adds a char field *hs_code* on product templates, which has the same purpose, but we can't use it because we need structured data for H.S. codes. This module hides the *hs_code* field added by the *delivery* module, to avoid confusion.

Since Odoo v16, the *delivery* module also adds a many2one field *country_of_origin*, which is similar to the many2one field *origin_country_id* of the OCA module *product_harmonized_system*. This module also hides the *country_of_origin* field added by the *delivery* module.

**Table of contents**

.. contents::
   :local:

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/OCA/intrastat-extrastat/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us smashing it by providing a detailed and welcomed
`feedback <https://github.com/OCA/intrastat-extrastat/issues/new?body=module:%20product_harmonized_system_delivery%0Aversion:%2016.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Do not contact contributors directly about support or help with technical issues.

Credits
=======

Authors
~~~~~~~

* Akretion

Contributors
~~~~~~~~~~~~

* Alexis de Lattre <alexis.delattre@akretion.com>
* Guewen Baconnier <guewen.baconnier@camptocamp.com>

Maintainers
~~~~~~~~~~~

This module is maintained by the OCA.

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

.. |maintainer-alexis-via| image:: https://github.com/alexis-via.png?size=40px
    :target: https://github.com/alexis-via
    :alt: alexis-via
.. |maintainer-luc-demeyer| image:: https://github.com/luc-demeyer.png?size=40px
    :target: https://github.com/luc-demeyer
    :alt: luc-demeyer

Current `maintainers <https://odoo-community.org/page/maintainer-role>`__:

|maintainer-alexis-via| |maintainer-luc-demeyer| 

This module is part of the `OCA/intrastat-extrastat <https://github.com/OCA/intrastat-extrastat/tree/16.0/product_harmonized_system_delivery>`_ project on GitHub.

You are welcome to contribute. To learn how please visit https://odoo-community.org/page/Contribute.
