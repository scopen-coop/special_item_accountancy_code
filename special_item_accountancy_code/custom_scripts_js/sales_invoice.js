// Copyright (c) 2017, Britlog and contributors
// For license information, please see license.txt

frappe.ui.form.on('Sales Invoice Item', {
    // cdt is Child DocType name i.e Quotation Item
    // cdn is the row name for e.g bbfcb8da6a
    item_code(frm, cdt, cdn) {
        let row = frappe.get_doc(cdt, cdn);
        console.log(frm.doc.customer);
        console.log(row.item_code);
        if (row.item_code) {
            frappe.call({
                method: "special_item_accountancy_code.custom_scripts_py.item_account_gl.get_correct_default_account",
                args: {
                    "customer": frm.doc.customer,
                    "item_code": row.item_code
                },
                callback: function (r) {
                    console.log(r.message);
                    if (r.message) {
                        //row.set_value("income_account", r.message);
                        row.income_account = r.message;
                    }
                }
            });
        }
    },
    income_account(frm, cdt, cdn) {
        let row = frappe.get_doc(cdt, cdn);
        console.log(frm.doc.customer);
        console.log(row.item_code);
        if (row.item_code) {
            frappe.call({
                method: "special_item_accountancy_code.custom_scripts_py.item_account_gl.get_correct_default_account",
                args: {
                    "customer": frm.doc.customer,
                    "item_code": row.item_code
                },
                callback: function (r) {
                    console.log(r.message);
                    if (r.message) {
                        //row.set_value("income_account", r.message);
                        row.income_account = r.message;
                    }
                }
            });
        }
    }
})