# Copyright (C) 2019 Open Source Integrators
# Copyright 2019 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Account Brand",
    "summary": "Send branded invoices and refunds",
    "version": "12.0.2.1.0",
    "category": "Accounting Management",
    "website": "https://github.com/OCA/account-invoicing",
    "author": "Open Source Integrators,"
              "ACSONE SA/NV,"
              "Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "depends": [
        'account',
        'brand',
    ],
    "data": [
        "views/account_invoice.xml",
        "views/res_partner_account_brand.xml",
        "security/res_partner_account_brand.xml",
    ],
    "installable": True,
    "development_status": "Beta",
    "maintainers": ["osi-scampbell"],
}
