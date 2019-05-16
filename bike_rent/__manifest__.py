# -*- coding: utf-8 -*-
{
    'name': "bike_rent",
    'summary': "Bike rent management module.",
    'description': "A practice module meant for Versada internship that manages bike rent operations.",
    'author': "Dangiras",
    'website': "https://www.versada.eu",
    'category': 'Uncategorized',
    'version': '12.0.1.0',
    'depends': [
        'base',
        'product',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/bike_rent_views.xml',
        'views/product_views.xml',
        'views/res_partner_views.xml'
    ],
    'demo': [
        'demo/bike_rent_demo.xml',
    ],
}