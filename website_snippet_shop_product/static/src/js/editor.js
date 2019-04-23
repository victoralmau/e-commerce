/* Copyright 2019 Tecnativa
 * License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl). */

odoo.define('website_snippet_shop_product.best_seller_editor', function (require) {
    'use strict';

    var s_options = require('web_editor.snippets.options');
    var rpc = require('web.rpc');

    // js_get_best_seller select category
    s_options.registry.js_get_best_seller_selectCategory = s_options.Class.extend({
        start: function () {
            this._super();
            var self      = this;
            var categoriesList = [];

            rpc.query({
                model: 'product.public.category',
                method: 'search_read',
                args: [[], ['name', 'id']],
            })
            .then(function (categories) {
                self.createCategoryList(categories) // start printing products...
            })
            .fail(function (e) {
                // No data
                var title = _t("Oops, Houston we have a problem"),
                    msg   = $("<div contenteditable='false' class='message error text-center'><h3>"+ title +"</h3><code>"+ e.data.message + "</code></div>" );
                self.$target.append(msg)
                return;
            });
        },
        createCategoryList: function (categories) {
            var self = this;
            var ul = null;
            ul = self.$overlay.find(".snippet-option-js_get_best_seller_selectCategory > ul");
            $(categories).each(function () {
                var category = $(this);
                var li = $('<li data-filter_by_category_id="' + category[0].id + '" data-no-preview="true"><a>' + category[0].name + '</a></li>');
                ul.append(li);
            });
            if (self.$target.attr("data-filter_by_category_id")) {
                var id = self.$target.attr("data-filter_by_category_id");
                ul.find("li[data-filter_by_category_id=" + id  + "]").addClass("active");
            }
        },
        filter_by_category_id: function (previewMode, value, $li) {
            $li.parent().find("li").removeClass("active");
            $li.addClass("active");
            value = parseInt(value);
            this.$target.attr("data-filter_by_category_id",value)
                                    .data("filter_by_category_id",value)
                                    .data('snippet-view').redrow(true);
        },
    });

    // js_get_best_seller limit product display
    s_options.registry.js_get_best_seller_limit = s_options.Class.extend({
        start: function () {
            var self = this;
            setTimeout(function () {
                var ul = self.$overlay.find(".snippet-option-js_get_best_seller_limit > ul");
                if (self.$target.attr("data-products_limit")) {
                    var limit = self.$target.attr("data-products_limit");
                    ul.find('li[data-products_limit="' + limit + '"]').addClass("active");
                } else {
                    ul.find('li[data-products_limit="3"]').addClass("active");
                }
            }, 100);
        },
        products_limit: function (previewMode, value, $li) {
            var self = this;
            value = parseInt(value);
            this.$target.attr("data-products_limit", value).data("products_limit", value);
            $li.parent().find("li").removeClass("active");
            $li.addClass("active");
        },
    });

});
