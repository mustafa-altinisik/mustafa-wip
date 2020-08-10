# -*- coding: utf-8 -*-

from odoo import models, fields, api

class vehicle(models.Model):
    _name = 'res.vehicle'
    _description = 'Vehicle'
    _order = 'name'

    name = fields.Char("Name", required=True, translate=True)
    plate = fields.Char("Plate")
    state = fields.Many2one('res.country.state', string='State', required=False)
