/* © 2016 Tecnativa, S.L.
 * License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
 */

(function () {
    'use strict';
    var website = openerp.website;

    $(document).ready(function () {
        $( ".chk_line" ).change(calculate_total).change();
        $('#add_to_cart').click(add_to_cart_group);
    });

    function calculate_total(){
        debugger
        var amount = 0.0;
        $( ".chk_line:checked" ).each(function() {
            amount += parseFloat($(this).data('lst_price')) * parseFloat($(this).data('unit'));
        });

        $("#total_selected").text(amount.toFixed(2).toString() +' €');
    };

    function add_to_cart_group(ev){
        ev.preventDefault();
        var product_ids = [];
        var $check = $(this);
        $( ".chk_line:checked" ).each(function() {
            var $check = $(this);
            product_ids.push($check.data('product_id'));
        });
        openerp.jsonRpc("/shop/cart/products_update_json", 'call', {
            'line_id': null,
            'product_ids': product_ids,
            'set_qty': 1})
            .then(function (data) {
                debugger
                if (!data.quantity) {
                    location.reload(true);
                    return;
                }
                var $q = $(".my_cart_quantity");
                $q.parent().parent().removeClass("hidden", !data.quantity);
                $q.html(data.cart_quantity).hide().fadeIn(600);
                $("#cart_total").replaceWith(data['website_sale.total']);
            });
    };
})();