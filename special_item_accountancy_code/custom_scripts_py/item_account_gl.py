# -*- coding: utf-8 -*-
# Copyright (c) 2021, scopen.fr and contributors
# For license information, please see license.txt

from __future__ import unicode_literals

import json

import frappe
from erpnext.stock.get_item_details import (get_item_details, process_args,
                                            purchase_doctypes, sales_doctypes)
from frappe import _
from frappe.model.mapper import make_mapped_doc
from six import string_types


@frappe.whitelist()
def get_item_details_custom(args, doc=None, for_validate=False, overwrite_warehouse=True):
    # standard feature
    out = get_item_details(args, doc, for_validate, overwrite_warehouse)
    print('toto')
    # PRocess arges and doc to use it as object
    args = process_args(args)
    if isinstance(doc, string_types):
        doc = json.loads(doc)

    # deal with tax code selling or buying
    transaction_type = None
    type_thirdparty = None
    if doc:
        if doc.get('doctype') in purchase_doctypes:
            transaction_type = 'Achat'
            type_thirdparty = 'Supplier'
        if doc.get('doctype') in sales_doctypes:
            transaction_type = 'Vente'
            type_thirdparty = 'Customer'

    # by defaut we don't know what we are working on
    if args.customer is not None:
        thirdparty = args.customer

    if args.supplier is not None:
        thirdparty = args.supplier

    # on Quotation there is no accountancy code
    if doc and doc.get('doctype') == 'Quotation':
        type_thirdparty = None

    if type_thirdparty is not None:
        account = get_correct_default_account(thirdparty, type_thirdparty, args.item_code)
        if transaction_type == 'Vente' and account is not None:
            out.income_account = account
        if transaction_type == 'Achat' and account is not None:
            out.expense_account = account

    return out


def get_correct_default_account(thirdparty, type_thirdparty, item_code):
    if thirdparty is not None:
        doc_thirdparty = frappe.get_doc(type_thirdparty, thirdparty)
        categ_compta_thirdparty = doc_thirdparty.categorie_comptable_tiers
        doc_item = frappe.get_doc('Item', item_code)
        account = None

        for thirdparty_setup_categ in frappe.db.get_all(doctype="Categorie comptable Tiers et code comptable Produit",
                                                        as_list=True,
                                                        filters={'parent': 'Special Item Accountancy Code Default'}):
            thirdparty_categ = frappe.get_doc("Categorie comptable Tiers et code comptable Produit",
                                              thirdparty_setup_categ[0])
            if thirdparty_categ.categorie_comptable_tiers == categ_compta_thirdparty:
                if type_thirdparty == 'Customer':
                    account = thirdparty_categ.compte_de_produits
                if type_thirdparty == 'Supplier':
                    account = thirdparty_categ.compte_de_charges
                    break

        for item_group_categ in frappe.db.get_all(doctype="Categorie comptable Tiers et code comptable Produit",
                                                  as_list=True,
                                                  filters={'parent': doc_item.item_group, 'parenttype': 'Item Group'}):
            thirdparty_categ = frappe.get_doc("Categorie comptable Tiers et code comptable Produit",
                                              item_group_categ[0])
            if thirdparty_categ.categorie_comptable_tiers == categ_compta_thirdparty:
                if type_thirdparty == 'Customer':
                    account = thirdparty_categ.compte_de_produits
                if type_thirdparty == 'Supplier':
                    account = thirdparty_categ.compte_de_charges
                    break

        if len(doc_item.special_item_accountancy_code_details) != 0:
            for detail in doc_item.special_item_accountancy_code_details:
                if detail.categorie_comptable_tiers == categ_compta_thirdparty:
                    if type_thirdparty == 'Customer':
                        account = detail.compte_de_produits
                    if type_thirdparty == 'Supplier':
                        account = detail.compte_de_charges
                    break

        return account


@frappe.whitelist()
def make_mapped_doc_custom(method, source_name, selected_children=None, args=None):
    out = make_mapped_doc(method, source_name, selected_children, args)

    method_selling = {'erpnext.selling.doctype.sales_order.sales_order.make_sales_invoice',
                      'erpnext.stock.doctype.delivery_note.delivery_note.make_sales_invoice'}
    if method in method_selling:
        customer = frappe.get_doc('Customer', out.customer)
        if (customer.categorie_comptable_tiers is None) or (customer.categorie_comptable_tiers == ""):
            frappe.throw(_('Cutomer accountancy category is missing'))
        for itm in out.items:
            itm.income_account = get_correct_default_account(out.customer, 'Customer', itm.item_code)

    method_buying = {'erpnext.buying.doctype.purchase_order.purchase_order.make_purchase_invoice',
                     'erpnext.stock.doctype.purchase_receipt.purchase_receipt.make_purchase_invoice'}
    if method in method_buying:
        supplier = frappe.get_doc('Supplier', out.supplier)
        if (supplier.categorie_comptable_tiers is None) or (supplier.categorie_comptable_tiers == ""):
            frappe.throw(_('Cutomer accountancy category is missing'))
        for itm in out.items:
            itm.expense_account = get_correct_default_account(out.supplier, 'Supplier', itm.item_code)

    return out
