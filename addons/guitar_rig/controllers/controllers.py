# -*- coding: utf-8 -*-
# from odoo import http


# class GuitarRig(http.Controller):
#     @http.route('/guitar_rig/guitar_rig', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/guitar_rig/guitar_rig/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('guitar_rig.listing', {
#             'root': '/guitar_rig/guitar_rig',
#             'objects': http.request.env['guitar_rig.guitar_rig'].search([]),
#         })

#     @http.route('/guitar_rig/guitar_rig/objects/<model("guitar_rig.guitar_rig"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('guitar_rig.object', {
#             'object': obj
#         })

