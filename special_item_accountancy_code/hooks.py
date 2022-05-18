# -*- coding: utf-8 -*-
from __future__ import unicode_literals

app_name = "special_item_accountancy_code"
app_title = "Special Item Accountancy Code"
app_publisher = "scopen.fr"
app_description = "Change les code compteable article en fonction du parametrage client"
app_icon = "octicon octicon-repo"
app_color = "grey"
app_email = "florian.henry@scopen.fr"
app_license = "AGPL 3.0"

# Includes in <head>
# ------------------

fixtures = [
    {
        "dt": ("Custom Field"),
        "filters": [["name", "in", (
            "Customer-categorie_comptable_tiers",
            "Supplier-categorie_comptable_tiers",
            "Item-special_item_accountancy_code",
            "Item-special_item_accountancy_code_details",
            "Item Group-special_item_accountancy_code",
            "Item Group-special_item_accountancy_code_details"
        )
                     ]]
    },
]

# include js, css files in header of desk.html
# app_include_css = "/assets/special_item_accountancy_code/css/special_item_accountancy_code.css"
# app_include_js = "/assets/special_item_accountancy_code/js/special_item_accountancy_code.js"

# include js, css files in header of web template
# web_include_css = "/assets/special_item_accountancy_code/css/special_item_accountancy_code.css"
# web_include_js = "/assets/special_item_accountancy_code/js/special_item_accountancy_code.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
doctype_js = {
    "Customer": ["custom_scripts_js/customer.js"],
    "Supplier": ["custom_scripts_js/supplier.js"],
    "Item": ["custom_scripts_js/item.js"],
}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "special_item_accountancy_code.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "special_item_accountancy_code.install.before_install"
# after_install = "special_item_accountancy_code.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "special_item_accountancy_code.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }
doc_events = {
   "Purchase Invoice": {
       "validate": "special_item_accountancy_code.custom_scripts_py.item_account_gl.get_correct_default_account_validate"
   },
   "Sales Invoice": {
        "validate": "special_item_accountancy_code.custom_scripts_py.item_account_gl.get_correct_default_account_validate"
   },
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"special_item_accountancy_code.tasks.all"
# 	],
# 	"daily": [
# 		"special_item_accountancy_code.tasks.daily"
# 	],
# 	"hourly": [
# 		"special_item_accountancy_code.tasks.hourly"
# 	],
# 	"weekly": [
# 		"special_item_accountancy_code.tasks.weekly"
# 	]
# 	"monthly": [
# 		"special_item_accountancy_code.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "special_item_accountancy_code.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "special_item_accountancy_code.event.get_events"
# }
override_whitelisted_methods = {
    "erpnext.stock.get_item_details.get_item_details": "special_item_accountancy_code.custom_scripts_py.item_account_gl.get_item_details_custom",
#    "frappe.model.mapper.make_mapped_doc": "special_item_accountancy_code.custom_scripts_py.item_account_gl.make_mapped_doc_custom",
}
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "special_item_accountancy_code.task.get_dashboard_data"
# }
