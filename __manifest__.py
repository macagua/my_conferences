# -*- coding: utf-8 -*-
{
    'name': "My conferences",

    'summary': """
        My Conferences is an application to ease the management of conferences
        you can manage registration of guests as well as resources...""",

    'description': """
       If you have the time to write a long description, please do!
    """,

    'author': "ERPish.com",
    'maintainer': "Leonardo J. Caballero G.",
    'website': "http://www.erpish.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Extra Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/mymenu.xml',
        'views/mainpage.xml',
    ],
    'application': True,
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'images': ['static/description/icon.png'],
}

