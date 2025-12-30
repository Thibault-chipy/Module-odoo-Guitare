from odoo import http
class Guitar(http.Controller):
    @http.route('/guitarRig/allgear', type='http', auth='public', website=True)

    def list(self, **kw):
        gears = http.request.env['guitar_rig.gear'].search([])
        return http.request.render('guitar_rig.list_gear_template', {
            'gears': gears
        })