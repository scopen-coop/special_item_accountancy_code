

erpnext.TransactionController.extend({
    update_item_tax_map_custom: function() {
		cosole.log('toito');
		var me = this;
		var item_codes = [];
		$.each(this.frm.doc.items || [], function(i, item) {
			if(item.item_code) {
				item_codes.push(item.item_code);
			}
		});

		if(item_codes.length) {
			return this.frm.call({
				method: "special_item_accountancy_code.custom_scripts_py.item_account_gl.get_item_tax_info_custom",
				args: {
					company: me.frm.doc.company,
                    doctype:me.frm.doc.doctype,
					tax_category: cstr(me.frm.doc.tax_category),
					item_codes: item_codes
				},
				callback: function(r) {
					if(!r.exc) {
						$.each(me.frm.doc.items || [], function(i, item) {
							if(item.item_code && r.message.hasOwnProperty(item.item_code)) {
								if (!item.item_tax_template) {
									item.item_tax_template = r.message[item.item_code].item_tax_template;
									item.item_tax_rate = r.message[item.item_code].item_tax_rate;
								}
								me.add_taxes_from_item_tax_template(item.item_tax_rate);
							} else {
								item.item_tax_template = "";
								item.item_tax_rate = "{}";
							}
						});
						me.calculate_taxes_and_totals();
					}
				}
			});
		}
	},    
})

console.log(erpnext.TransactionController);