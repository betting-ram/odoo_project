# -*- coding: utf-8 -*-
from odoo import http

# class NewModulecustomAddons(http.Controller):
#     @http.route('/new_modulecustom_addons/new_modulecustom_addons/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/new_modulecustom_addons/new_modulecustom_addons/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('new_modulecustom_addons.listing', {
#             'root': '/new_modulecustom_addons/new_modulecustom_addons',
#             'objects': http.request.env['new_modulecustom_addons.new_modulecustom_addons'].search([]),
#         })

#     @http.route('/new_modulecustom_addons/new_modulecustom_addons/objects/<model("new_modulecustom_addons.new_modulecustom_addons"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('new_modulecustom_addons.object', {
#             'object': obj
#         })