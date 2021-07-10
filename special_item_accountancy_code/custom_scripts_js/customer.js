// Copyright (c) 2017, Britlog and contributors
// For license information, please see license.txt

frappe.ui.form.on("Customer", {
	setup: function(frm) {
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
                //console.log('HELLO soy');
                //console.log(r.message["result"]);
                //cur_frm.set_cur_list("grading_subject",r.message["result"]);
                //var x = r.message["result"]
            }
        });
		//frm.set_df_property('categorie_comptable', 'options', ['option a', 'option b']);
		//frm.refresh_field('grading_subject');

		//frm.set_query('categorie_comptable', function () {
		//	return {
		//		query: "item_accountancy_code.custom_scripts.item_account_gl.get_available_accountancy_code_type"
		//	}
		//});
	}
});