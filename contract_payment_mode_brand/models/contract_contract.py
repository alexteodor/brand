# Copyright 2020 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class ContractContract(models.Model):

    _name = "contract.contract"
    _inherit = ["contract.contract", "res.brand.allowed.payment.mode.mixin"]
