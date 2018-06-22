# Copyright 2017 Sergio Teruel <sergio.teruel@tecnativa.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    "name": "Website Sale Stock Control Global",
    "summary": "Block sale products without global stock in shop on line",
    "version": "11.0.1.0.0",
    "category": "Website",
    "website": "http://www.tecnativa.com",
    "author": "Tecnativa, "
              "Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "depends": [
        "website_sale_stock",
        "stock_available_global",
    ],
    "application": False,
    "installable": True,
    "auto_install": True,
}
