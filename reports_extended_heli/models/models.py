# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    reserve_uf = fields.Monetary('Reserva')

    foot_uf = fields.Monetary('Pie')

    subsidy_uf = fields.Monetary('Subsidio')

    saving_uf = fields.Monetary('Ahorro')

    against_writing_uf = fields.Monetary('Contra Escritura')

    mortgage_credit_uf = fields.Monetary('Crédito Hipotecario')

    total_uf = fields.Monetary('Total', compute='calculate_total_uf')

    @api.onchange('reserve_uf', 'foot_uf', 'subsidy_uf', 'saving_uf', 'against_writing_uf', 'mortgage_credit_uf')
    def calculate_total_uf(self):
        self.total_uf = self.reserve_uf + self.foot_uf + self.subsidy_uf + self.saving_uf + self.against_writing_uf + self.mortgage_credit_uf


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    total_pend = fields.Monetary('Monto Pendiente', compute='compute_total_pend')

    def compute_total_pend(self):
        for po in self:
            total_pend = sum((line.price_unit * line.qty_received) - (line.price_unit * line.qty_invoiced) for line in po.order_line)
            total_taxes = sum(line.price_tax for line in po.order_line.filtered(lambda x: x.qty_received > 0 and x.qty_invoiced <= 0))
            po.total_pend = total_pend + total_taxes








