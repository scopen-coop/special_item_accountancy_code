// Copyright (c) 2021, scopen.fr and contributors
// For license information, please see license.txt

frappe.ui.form.on('Categorie comptable Tiers et code comptable Produit', "categorie_comptable", function(frm,cdt,cdn) {
        frappe.msgprint("qsdqdqsd");
        frappe.call({
            method: "special_item_accountancy_code.custom_scripts_py.item_account_gl.get_available_accountancy_code_type",
            args: {
                    doctype:frm.doc,
                    txt:'',
                    searchfield:'',
                    start:'',
                    page_len:'',
                    filters:''
                },
            callback: function (r) {
                frm.set_df_property('categorie_comptable', 'options', r.message)
                frm.refresh_field('categorie_comptable');
            }
        });
    });
