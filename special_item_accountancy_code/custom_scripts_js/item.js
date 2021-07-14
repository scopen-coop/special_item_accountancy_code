// Copyright (c) 2017, Britlog and contributors
// For license information, please see license.txt

frappe.ui.form.on('Item', {
    setup: function(frm) {
        frm.set_query('categorie_comptable_tiers', 'special_item_accountancy_code_details', function (doc, cdt, cdn) {
            var filters = {
                'is_actif': 1
            };
            return {
                filters: filters
            }
        });
    }
});