# Copyright 2020 Tecnativa
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    'name': 'Tecnativa Access Test',
    'category': 'e-commerce',
    'author': "Tecnativa, ",
    'website': 'https://github.com/OCA/e-commerce',
    'version': '12.0.1.0.0',
    'license': 'AGPL-3',
    'depends': [
        'account',
        'web_responsive',
        'website_sale',
    ],
    'data': [
        "security/ir.model.access.csv",
        "data/menus.xml",
        "views/tecnativa_access_test.xml",
        "views/test_page.xml",
        "views/report_invoice_customer_totals.xml",
    ],
    'demo': [
        "demo/demo.xml",
    ],
    'installable': False,
}
