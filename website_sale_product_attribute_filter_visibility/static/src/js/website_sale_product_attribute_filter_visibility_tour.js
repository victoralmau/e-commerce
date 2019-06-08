/* Copyright 2019 Sergio Teruel
 * License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl). */

odoo.define("website_sale_product_attribute_filter_visibility.tour", function (require) {
    "use strict";

    var tour = require("web_tour.tour");
    var base = require("web_editor.base");

    var steps = [  
       {
            content: "open customize menu",
            trigger: '#customize-menu > a',
        },
        {
            content: "click on 'Product Attribute's Filter'",
            trigger: "#customize-menu a:contains(Product Attribute's Filter)",
            
        },
        {
            content: "Check that Test color is showed as attibute",
            trigger: "a:contains('Customizable Desk')",
            extra_trigger: ".js_attributes:has(strong:contains('Test Color'))",

        },
        {
            content: "Check that Test Size is showed as attibute",
            trigger: "a:contains('Customizable Desk')",
            extra_trigger: ".js_attributes:not(:has(strong:contains('Test Size')))",

        },
        
       {
            content: "open customize menu",
            trigger: '#customize-menu > a',
        },
        
        {
            content: "click on 'Product Attribute's Filter'",
            trigger: "#customize-menu a:contains(Product Attribute's Filter)",
        },        

    ];
    tour.register("website_sale_product_attribute_filter_visibility",
        {
            url: "/shop",
            test: true,
            wait_for: base.ready(),
        },
        steps
    );
    return {
        steps: steps,
    };
});
