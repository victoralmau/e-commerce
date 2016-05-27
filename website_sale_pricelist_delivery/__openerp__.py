# -*- coding: utf-8 -*-
# © 2016 Carlos Dauden <carlos.dauden@tecnativa.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': "Website Sale Pricelist Delivery",
    'summary': """
        This module allows associate a pricelist with deliveries
    """,
    'category': 'e-commerce',
    'version': '8.0.1.0.0',
    'depends': [
        'website_sale_delivery',
    ],
    'data': [
        'views/pricelist_view.xml',
    ],
    'author': 'Tecnativa, '
              'Odoo Community Association (OCA)',
    'website': 'http://www.tecnativa.com',
    'license': 'AGPL-3',
    'installable': True,
}
