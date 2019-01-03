# -*- coding: utf-8 -*-

from odoo import models, fields, api


class MrpBom(models.Model):
    _inherit = 'mrp.bom'

    is_unbuild = fields.Boolean("Is Unbuild")

    @api.multi
    def compute_percentage(self):
        for bom in self:
            total_value = sum(bom.bom_line_ids.mapped('cost_price'))
            for line in bom.bom_line_ids:
                line.cost_percentage = line.cost_price / total_value * 100
