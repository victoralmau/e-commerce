/* © 2016 Tecnativa, S.L.
 * License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
 */
(function () {
    'use strict';
    var website = openerp.website;
    var qweb = openerp.qweb;
    website.add_template_file('/website_sale_product_group/static/src/xml/product_group.xml');

    openerp.website.productpack = {};
    openerp.website.productpack.Pack = openerp.Widget.extend({
        init: function (dom) {
            var self = this;
            this.$el = this.$target = $(dom);
            this.start();
        },
        start: function () {
            var self = this;
            this.$el.find('.js_add_to_cart').on('click', function (event) {
                    event.preventDefault();
                    self.on_click();
                });
            this.$el.find('form input:checkbox').on('change', function (event) {
                    self.on_change(event);
                });
        },
        stop: function () {
        },
        on_click: function(){
            this.add_to_cart_group();
        },
        on_change: function(event){
            this.render_total();
        },
        calculate_total: function(){
            var self = this;
            var total_dic = {};
            var total_price = 0.0;
            var total_lst_price = 0.0;
            $( ".chk_line:checked" ).each(function() {
                total_price += parseFloat($(this).data('price')) * parseFloat($(this).data('unit'));
                total_lst_price += parseFloat($(this).data('lst_price')) * parseFloat($(this).data('unit'));
            });
            total_dic = {
                'total_price': total_price,
                'total_lst_price': total_lst_price,
            }
            return total_dic;
        },
        render_total: function (){
            var total_dic = this.calculate_total();
            $(".js_total_selected_price").text(total_dic['total_price'].toFixed(2).toString() +' €');
            $(".js_total_selected_lst_price").text(total_dic['total_lst_price'].toFixed(2).toString() +' €');
        },
        add_to_cart_group: function (){
            var self = this;
            var product_ids = [];
            product_ids = this.selected_lines();
            if (product_ids.length > 0) {
                this.show_popup();
                openerp.jsonRpc("/shop/cart/products_update_json", 'call', {
                    'line_id': null,
                    'product_ids': product_ids,
                    'set_qty': 1})
                    .then(function (data) {
                        if (!data.quantity) {
                            location.reload(true);
                            return;
                        }
                        var $q = $(".my_cart_quantity");
                        $q.parent().parent().removeClass("hidden", !data.quantity);
                        $q.html(data.cart_quantity).hide().fadeIn(600);
                        $("#cart_total").replaceWith(data['website_sale.total']);
                        self.hide_popup();
                    });
            };
        },
        show_popup: function(){
            $(".oe_product_cart").prepend(qweb.render('popupcart',{}));
            $('#popup').fadeIn('slow');
            $('.popup-overlay').fadeIn('slow');
            $('.popup-overlay').height($(window).height());
        },
        hide_popup: function(){
            $('#popup').fadeOut('slow');
            $('.popup-overlay').fadeOut('slow');
            $("#popup").remove();
        },
        selected_lines: function (){
            var self = this;
            var product_ids = new Array();
            $( ".chk_line:checked" ).each(function() {
                var $check = $(this);
                product_ids.push({
                    'product_id': $check.data('product_id'),
                    'qty': $check.data('unit'),
                    'pack_item_id': $check.data('pack_item_id'),
                    'public_categ_id': $check.data('public_categ_id'),
                    });
            });
            return product_ids;
        }
    });

    $(document).ready(function () {
        var content = new openerp.website.productpack.Pack(this);
        content.render_total();
    });
})();