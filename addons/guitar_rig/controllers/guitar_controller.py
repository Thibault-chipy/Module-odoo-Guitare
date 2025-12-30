from odoo import http
class Guitar(http.Controller):
    @http.route('/guitarRig/allguitars', type='http', auth='public', website=True)

    def list(self, **kw):
        guitars = http.request.env['guitar_rig.gear'].search([])
        return http.request.render('guitar_rig.list_gear_template', {
            'gears': guitars
        })