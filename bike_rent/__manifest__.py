# -*- coding: utf-8 -*-
{
    'name': "bike_rent",
    'summary': "Bike rent management module.",
    'description': "A practice module meant for Versada internship that manages bike rent operations.",
    'author': "Dangiras",
    'website': "https://github.com/dangirasv/bike_rent",
    'category': 'Uncategorized',
    'version': '12.0.1.0.0',
    'depends': [
        'website_sale',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/bike_rent_views.xml',
        'views/product_views.xml',
        'views/res_partner_views.xml',
        'views/sale_views.xml',
        'views/website_sale_templates.xml',
        'report/sale_order_report_templates.xml',
    ],
    'demo': [
        'demo/product_product_demo.xml',
        'demo/res_partner_demo.xml',
        'demo/sale_order_demo.xml',
    ],
}