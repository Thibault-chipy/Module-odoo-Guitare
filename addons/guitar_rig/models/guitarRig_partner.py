from odoo import models, fields

#Fabricant
class ResPartner(models.Model):
    #Héritage de res.partner
    _inherit = 'res.partner'  

    #Nouveau champ : Est une marque de musique
    is_guitar_brand = fields.Boolean(string="Est une marque de musique", default=False)
    
    #Type de fabricant
    brand_type = fields.Selection([
        ('luthier', 'Luthier Indépendant'),
        ('industrial', 'Grande Marque'),
        ('boutique', 'Boutique / Artisanal')
    ], string="Type de Fabricant")

    #Histoire de la marque
    history = fields.Text(string="Histoire de la marque")