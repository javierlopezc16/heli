# -*- coding: utf-8 -*-
from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    verify_user_group = fields.Boolean(string="Verificación del grupo de usuario", compute="verify_group_user")

    @api.onchange('partner_id')
    def verify_group_user(self):
        user_id = self.env.user
        if user_id.has_group('heli_access_permissions.group_product_access_price'):
            self.write({'verify_user_group': True})
        else:
            self.write({'verify_user_group': False})


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    verify_user_group = fields.Boolean(string="Verificación del grupo de usuario", related="order_id.verify_user_group")







