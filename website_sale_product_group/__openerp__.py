# -*- coding: utf-8 -*-
# © 2016 Carlos Dauden <carlos.dauden@tecnativa.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': "Website Sale Product Group",
    'summary': """
        This module allows group products in website sale
    """,
    'category': 'e-commerce',
    'version': '8.0.1.0.0',
    'depends': [
        'website_sale',
    ],
    'demo': [
    ],
    'data': [
        'views/website_sale_product_group.xml',
        'views/product_view.xml',
        'views/templates.xml',
        'views/assets.xml',
        'security/ir.model.access.csv',
    ],
    'author': 'Tecnativa, '
              'Odoo Community Association (OCA)',
    'website': 'http://www.tecnativa.com',
    'license': 'AGPL-3',
    'installable': True,
    'images': [],
}
