# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResCompany(models.Model):
    _inherit = 'res.company'

    footer = fields.Binary(string="Company Footer", readonly=False)








