# -*- coding: utf-8 -*-
# from odoo import http


# class SaleExtras(http.Controller):
#     @http.route('/sale_extras/sale_extras', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_extras/sale_extras/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_extras.listing', {
#             'root': '/sale_extras/sale_extras',
#             'objects': http.request.env['sale_extras.sale_extras'].search([]),
#         })

#     @http.route('/sale_extras/sale_extras/objects/<model("sale_extras.sale_extras"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_extras.object', {
#             'object': obj
#         })
