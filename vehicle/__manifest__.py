# -*- coding: utf-8 -*-
{
    'name': "vehicle",

    'summary': """
        Module created for educational purposes.""",

    'description': """
        a very long description """,

    'author': "Mustafa Asım Altınışık",
    'website': "https://www.mustafa.altinisik.net",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    #modülümüzün çalışması için gerekli olan modüller
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
