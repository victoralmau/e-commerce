# -*- coding: utf-8 -*-
# © 2017 Sergio Teruel <sergio.teruel@tecnativa.com>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    'name': 'Website Sale Skip Payment',
    'summary': 'Skip payment for logged users in checkout process',
    'version': '9.0.1.0.0',
    'category': 'E-commerce',
    'website': 'https://www.tecnativa.com',
    'author': 'Tecnativa, Odoo Community Association (OCA)',
    'license': 'LGPL-3',
    'application': False,
    'installable': True,
    'depends': [
        'website_sale',
    ],
    'data': [
        'views/website_sale_skip_payment.xml',
    ],
}
