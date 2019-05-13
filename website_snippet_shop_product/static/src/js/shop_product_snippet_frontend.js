/* Copyright 2019 Tecnativa
 * License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl). */

odoo.define('website_snippet_shop_product.best_seller_frontend', function (require) {
    'use strict';

    var sAnimation = require('website.content.snippets.animation');
    var core = require('web.core');
    var rpc = require('web.rpc');

    var QWeb = core.qweb;
    var _t = core._t;

    sAnimation.registry.js_get_best_seller = sAnimation.Class.extend({
        selector : ".js_get_best_seller",
        xmlDependencies: ['/website_snippet_shop_product/static/src/xml/website_snippet_shop_product.xml'],

        start: function () {
            this.redrow();
            return this._super.apply(this, arguments);
        },
        destroy: function () {
            this._super.apply(this, arguments);
            this.clean();
        },
        redrow: function (debug) {
            this.clean(debug);
            this.build(debug);
        },
        clean: function (debug) {
            this.$target.empty();
        },
        build: function (debug) {
            var self     = this,
                limit    = self.$target.data("products_limit"),
                category_id  = self.$target.data("filter_by_category_id"),
                template = self.$target.data("template"),
                loading  = self.$target.data("loading");
            // prevent user's editing
            self.$target.attr("contenteditable","False");
            // if no data, then use defaults values
            if (!limit) limit = 3;
            if (!template) template = 'website_snippet_shop_product.best_seller_list_template';
            // create the domain
            var domain = [['website_published', '=', true]];
            if (category_id) {domain.push(['public_categ_ids', 'in', [parseInt(category_id)]]); }
            // call products
            rpc.query({
                model: 'product.template',
                method: 'search_read',
                args: [domain, ['name', 'id']],
            })
            .then(function (products) {
                var $template = $(QWeb.render("website_snippet_shop_product.products", {'products': products}));
                $template.appendTo(self.$target);
            })
            .fail(function (e) {
                // No data
                var title = _t("Oops, Houston we have a problem"),
                    msg   = $("<div contenteditable='false' class='message error text-center'><h3>"+ title +"</h3><code>"+ e.data.message + "</code></div>" );
                self.$target.append(msg)
                return;
            });
        },
    });
});
