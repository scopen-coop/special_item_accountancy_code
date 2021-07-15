# -*- coding: utf-8 -*-
# Copyright (c) 2017, Britlog and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
import json
from erpnext.stock.get_item_details import get_item_details, process_args

@frappe.whitelist()
def get_item_details_custom(args, doc=None, for_validate=False, overwrite_warehouse=True):
    out = get_item_details(args, doc, for_validate, overwrite_warehouse)
    args = process_args(args)

    out.income_account = get_correct_default_account(args.customer, args.item_code)

    return out

def get_correct_default_account(customer, item_code):

    doc_customer = frappe.get_doc('Customer', customer)
    categ_compta_thirdparty = doc_customer.categorie_comptable_tiers

    doc_item = frappe.get_doc('Item', item_code)
    if len(doc_item.special_item_accountancy_code_details) != 0:
        for detail in doc_item.special_item_accountancy_code_details:
            if detail.categorie_comptable_tiers == categ_compta_thirdparty:
                return detail.compte_de_produits

    else:
        for thirdparty_setup_categ in frappe.db.get_all(doctype="Categorie comptable Tiers et code comptable Produit",
                                                    as_list=True,
                                                    filters={'parent': 'Special Item Accountancy Code Default'}):
            thirdparty_categ = frappe.get_doc("Categorie comptable Tiers et code comptable Produit",
                                              thirdparty_setup_categ[0])
            print(thirdparty_categ.categorie_comptable_tiers)
            print(categ_compta_thirdparty)
            if thirdparty_categ.categorie_comptable_tiers == categ_compta_thirdparty:
                return thirdparty_categ.compte_de_produits