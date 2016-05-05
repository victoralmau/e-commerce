/* © 2016 Tecnativa, S.L.
 * License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
 */

(function () {
    'use strict';
    var website = openerp.website;

    $(document).ready(function () {
        $( ".chk_line" ).change(function () {
            var amount = 0.0;
            $( ".chk_line:checked" ).each(function() {
                amount += parseFloat($(this).data('lst_price'));
            });
            $("#total_selected").text(amount.toFixed(2).toString() +' €');
          }).change();
        $('#add_to_cart').click(add_to_cart_group);
    });

    function add_to_cart_group(ev){
        ev.preventDefault();
        $( ".chk_line:checked" ).each(function() {
            debugger
            var $check = $(this);
            var line_id;
            var value = 1;
            openerp.jsonRpc("/shop/cart/update_json", 'call', {
            'line_id': null,
            'product_id': parseInt($check.data('product_id')),
            'set_qty': value})
            .then(function (data) {
                debugger
                if (!data.quantity) {
                    location.reload(true);
                    return;
                }
                var $q = $(".my_cart_quantity");
                $q.parent().parent().removeClass("hidden", !data.quantity);
                $q.html(data.cart_quantity).hide().fadeIn(600);

//                $("#cart_total").replaceWith(data['website_sale.total']);
            });


        });


    }

})();