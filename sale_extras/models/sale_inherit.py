from odoo import fields, models, api


class SaleInherit(models.Model):
    _inherit = "sale.order"

    rdprice = fields.Char()
