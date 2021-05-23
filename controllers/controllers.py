# -*- coding: utf-8 -*-
from odoo import http

# class FinancesDomestiques(http.Controller):
#     @http.route('/finances_domestiques/finances_domestiques/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/finances_domestiques/finances_domestiques/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('finances_domestiques.listing', {
#             'root': '/finances_domestiques/finances_domestiques',
#             'objects': http.request.env['finances_domestiques.finances_domestiques'].search([]),
#         })

#     @http.route('/finances_domestiques/finances_domestiques/objects/<model("finances_domestiques.finances_domestiques"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('finances_domestiques.object', {
#             'object': obj
#         })