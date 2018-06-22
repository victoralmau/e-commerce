# Copyright 2017-2018 Sergio Teruel <sergio.teruel@tecnativa.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from lxml import html
import json
from odoo.tests.common import HttpCase


class WebsiteSaleStockControlGlobal(HttpCase):
    def setUp(cls):
        super(WebsiteSaleStockControlGlobal, cls).setUp()
        cls.public_user = cls.env.ref('base.public_user')
        with cls.cursor() as cr:
            env = cls.env(cr)
            Quant = env['stock.quant']
            SaleOrder = env['sale.order']
            SaleOrderLine = env['sale.order.line']
            cls.company1 = env['res.company'].create({
                'name': 'company1',
            })
            cls.warehouse_company1 = env['stock.warehouse'].create({
                'name': 'Wharehouse Company1',
                'company_id': cls.company1.id,
                'code': 'WH1',
            })

            cls.company2 = env['res.company'].create({
                'name': 'company2',
            })
            cls.warehouse_company2 = env['stock.warehouse'].create({
                'name': 'Wharehouse Company2',
                'company_id': cls.company2.id,
                'code': 'WH2',
            })

            cls.product_tmpl = env['product.template'].create({
                'name': 'Test template',
                'type': 'product',
                'inventory_availability': 'always',
                'website_published': True,
                'list_price': 150.0,
            })
            cls.quant_company_1 = Quant.create({
                'location_id': cls.warehouse_company1.lot_stock_id.id,
                'product_id': cls.product_tmpl.product_variant_id.id,
                'quantity': 10,
            })
            cls.quant_company_2 = Quant.create({
                'location_id': cls.warehouse_company2.lot_stock_id.id,
                'product_id': cls.product_tmpl.product_variant_id.id,
                'quantity': 10,
            })
            so = SaleOrder.new({
                'partner_id': cls.public_user.partner_id.id,
            })
            so.onchange_partner_id()
            cls.sale_order = SaleOrder.create(so._convert_to_write(so._cache))
            sol = SaleOrderLine.new({
                'order_id': cls.sale_order.id,
                'product_id': cls.product_tmpl.product_variant_id.id,
                'product_uom_qty': 5.0,
            })
            sol.product_id_change()
            SaleOrderLine.create(sol._convert_to_write(sol._cache))

    def test_product_page(self):
        response = self.url_open(
            '/shop/product/%s' % self.product_tmpl.id, timeout=20)
        result = html.document_fromstring(response.content)
        attribute_values = result.xpath(
            "//ul[@class='list-unstyled js_add_cart_variants nav-stacked']"
        )
        values = json.loads(
            attribute_values[0].attrib['data-attribute_value_ids']
        )
        available_global = values[0][4]['virtual_available']
        self.assertEquals(available_global, 20.0)

    def test_sale_order(self):
        with self.cursor() as cr:
            res = self.sale_order._cart_update(
                self.product_tmpl.product_variant_id.id,
                set_qty=10.0,
                kawrds={}
            )
            self.assertFalse('warning' in res)

    def test_sale_order_wo_global_stock(self):
        # with self.cursor() as cr:
        res = self.sale_order._cart_update(
            self.product_tmpl.product_variant_id.id,
            add_qty=50.0,
            kawrds={}
        )
        self.assertTrue('warning' in res)
