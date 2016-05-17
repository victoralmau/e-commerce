# -*- coding: utf-8 -*-
# © 2016 Sergio Teruel <sergio.teruel@tecnativa.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Website Sale By Category",
    "summary": "Show categories in shop",
    "version": "8.0.1.0.0",
    "category": "e-commerce",
    'website': 'http://www.tecnativa.com',
    'author': 'Tecnativa, '
              'Odoo Community Association (OCA)',
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "website_sale",
    ],
    "data": [
        "views/assets.xml",
        "views/website_sale_by_category_view.xml",
        "views/template.xml",
        "security/website_sale_by_category.xml",
    ],
}
