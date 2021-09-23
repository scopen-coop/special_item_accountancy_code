

// TaxesAndTotalsExtend is just variable name
// erpnext.taxes_and_totals is function contain function you want to override
const TaxesAndTotalsExtend = erpnext.taxes_and_totals.extend({
	// calculate_item_values is function you want to override
	update_item_tax_map: () => {
		var me = this;
		console.log(me);
		var item_codes = [];
		$.each(this.frm.doc.items || [], function (i, item) {
			if (item.item_code) {
				item_codes.push(item.item_code);
			}
		});
	
		if (item_codes.length) {
			return this.frm.call({
				method: "special_item_accountancy_code.custom_scripts_py.item_account_gl.get_item_tax_info_custom",
				args: {
					company: me.frm.doc.company,
					tax_category: cstr(me.frm.doc.tax_category),
					item_codes: item_codes,
					doctype: me.frm.doc.doctype,
				},
				callback: function (r) {
					if (!r.exc) {
						$.each(me.frm.doc.items || [], function (i, item) {
							if (item.item_code && r.message.hasOwnProperty(item.item_code)) {
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
});
console.log(cur_frm);
// this tell current form to use this override script
/*$.extend(
	cur_frm.cscript,
	new TaxesAndTotalsExtend({frm: cur_frm}),
);*/