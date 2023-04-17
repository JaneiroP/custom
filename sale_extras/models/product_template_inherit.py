from odoo import fields, models, api


class ProductTemplateInherit(models.Model):
    _inherit = "product.template"

    name = fields.Char('name')

    def regexval(self):
        return '225/45%r%18'


