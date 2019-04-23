# Copyright 2019 Tecnativa
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Website Snippet Shop Product',
    'summary': 'This module allows the user '
               'to display some products into any website page.',
    'category': 'Website',
    'version': '11.0.1.0.0',
    'author': 'Onestein, Odoo Community Association (OCA)',
    'license': 'AGPL-3',
    'website': 'https://github.com/OCA/e-commerce',
    'depends': [
        'website_sale'
    ],
    'data': [
        'templates/assets.xml',
        'templates/snippets.xml',
    ],
    'installable': True,
}
