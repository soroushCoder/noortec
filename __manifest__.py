# -*- coding: utf-8 -*-
{
    'name': "artarad_website_noortec",

    'summary': """
        """,

    'description': """
        Customize theme for noortec website
    """,

    'author': "Mohammad Hassanzadeh & Soroush Ebadi",
    'website': "http://www.artarad.ir",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['website'],

    # always loaded
    'data': [



        'views/templates.xml',
    ],
    'qweb': [
         # 'views/templates.xml',

    ],

    'css':['static/src/css/noortec_style.css'],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}