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
        'views/sale_service_view.xml',
        'views/sale_service_project_view.xml',
        'views/sale_view.xml',
        'views/account_invoice_view.xml',
        'views/project_view.xml',
        'views/report_saleorder.xml',
        'views/report_invoice.xml',
        'wizard/product_price_service_view.xml',
        'security/ir.model.access.csv',
    ],
    'author': 'Tecnativa, '
              'Odoo Community Association (OCA)',
    'website': 'http://www.tecnativa.com',
    'license': 'AGPL-3',
    'installable': True,
    'images': [],
}
