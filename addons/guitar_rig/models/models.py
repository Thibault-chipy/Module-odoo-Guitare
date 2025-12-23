# -*- coding: utf-8 -*-

from odoo import models, fields, api


class guitar_rig(models.Model):
    _name = 'guitar_rig.guitar_rig'
    _description = 'guitar_rig.guitar_rig'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100

