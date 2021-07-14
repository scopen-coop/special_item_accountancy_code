# -*- coding: utf-8 -*-
# Copyright (c) 2017, Britlog and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
import pdb


@frappe.whitelist()
def get_available_accountancy_code_type(doctype, txt, searchfield, start, page_len, filters):
    thirdparty_accountancy_categ_available = frappe.db.get_single_value('Special Item Accountancy Code Default', "categ_thirdparty").split("\n")
    return thirdparty_accountancy_categ_available


def get_correct_default_account(doc, method):
    pass
    #frappe.throw(doc)
    #if len(doc.taxes) == 0:
    #    item_tax_template = frappe.get_doc("Item Tax Template", "TVA 20")
    #   if item_tax_template is not None:
    #       doc.append("taxes", {"item_tax_template": item_tax_template.name})
