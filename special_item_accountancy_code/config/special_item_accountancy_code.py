from __future__ import unicode_literals
from frappe import _

def get_data():
	data = [
		{
			"label": _("Accounting Masters"),
			"icon": "fa fa-star",
			"items": [
				{
					"type": "doctype",
					"name": "Categorie comptable Tiers",
					"label": _("Categorie comptable Tiers"),
					"description": _("Categorie comptable Tiers")
				},
				{
					"type": "doctype",
					"name": "Special Item Accountancy Code Default",
					"label": _("Categorie comptable Tiers et code comptable Produit par défaut"),
					"description": _("Categorie comptable Tiers et code comptable Produit par défaut")
				}
			]
		}
	]

	return data
