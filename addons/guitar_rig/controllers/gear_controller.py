from odoo import http, models, fields, api
from odoo.exceptions import ValidationError

class Gear(http.Controller):
    @http.route('/guitar_rig/gear/allGears', type='http', auth='public', website=True)
    
    def list(self,**kwargs):
        gear = http.request.env['guitar_rig.gear']
        gears= gear.search([])
        return http.request.render(
            "guitar_rig.list_gear_template",
            {'gears': gears}
        )
     
