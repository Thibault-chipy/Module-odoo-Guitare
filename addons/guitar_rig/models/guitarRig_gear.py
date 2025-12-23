from odoo import models, fields, api
from odoo.exceptions import ValidationError
class Gear(models.Model):
    _name = 'guitar_rig.gear'
    _description = 'Élément de matériel (guitare / pédale / plugin / ampli)'

    name = fields.Char("Nom", required=True)                 # texte
    gear_type = fields.Selection(                            # select
        [
            ('guitar', 'Guitare'),
            ('pedal', 'Pédale'),
            ('plugin', 'Plugin'),
            ('amp', 'Ampli'),
        ],
        string="Type",
        required=True,
    )
    purchase_date = fields.Date("Date d'achat")              # date
    price = fields.Float("Prix d'achat")                     # numérique
    image = fields.Binary("Photo")                           # image


    # 1-N : gear -> sessions où c'est le gear principal
    main_session_ids = fields.One2many(
        'guitar_rig.session', 'main_gear_id',
        string="Sessions (gear principal)"
    )

    # N-N : gear <-> sessions où il est utilisé
    session_ids = fields.Many2many(
        'guitar_rig.session', 'guitar_session_gear_rel',
        'gear_id', 'session_id',
        string="Sessions (tous les gear)"
    )

    # Relation many2one avec Fabricant
    manufacturer_id = fields.Many2one('res.partner', string="Fabricant", 
                                      domain=[('is_guitar_brand', '=', True)])

# Champ calculé pour l'affichage dans la liste
    manufacturer_label = fields.Char(
        string="Fabricant",
        compute='_compute_manufacturer_label'
    )

    @api.depends('manufacturer_id')
    def _compute_manufacturer_label(self):
        for record in self:
            if record.manufacturer_id:
                # Si un fabricant est lié, on prend son nom
                record.manufacturer_label = record.manufacturer_id.name
            else:
                record.manufacturer_label = "Inconnu"

        
    # Champ related : pays du fabricant
    manufacturer_country_id = fields.Many2one(
        'res.country',
        string="Pays fabricant",
        related='manufacturer_id.country_id',
        store=True,
        readonly=True,
    )

    manufacturer_country_label = fields.Char(
        string="Pays fabricant",
        compute='_check_manufacturer_country'
    )   

    #Vérif sur le pays du fabricant
    @api.constrains('manufacturer_country_id')
    def _check_manufacturer_country(self):
        for record in self:
            if record.manufacturer_country_id:
                record.manufacturer_country_label = record.manufacturer_country_id.name
            else:
                record.manufacturer_country_label = "Inconnu"
                
    # champ calculé : nb total de sessions où ce gear apparaît
    session_count = fields.Integer(
        string="Nb de sessions",
        compute='_compute_session_count',
        store=True,
    )

    #Vérif sur le calcul du nombre de sessions
    @api.depends('session_ids', 'main_session_ids')
    def _compute_session_count(self):
        for record in self:
            record.session_count = len(record.session_ids) + len(record.main_session_ids)
    
    
    # Champ visible seulement pour admin (dans la vue)
    internal_notes = fields.Text("Notes internes")

    @api.constrains('price')
    def _check_price(self):
        for record in self:
            if record.price < 0:
                raise ValidationError("Pas de prix négatif autorisé.")
            
    #Calcul de vérif sur le prix
    def action_verify_price(self):
        for record in self:
            if record.price < 0:
                # Cas Erreur 
                raise ValidationError("Attention ! Le prix ne peut pas être négatif.")
            
            else:
                # Cas Succès 
                return {
                    'type': 'ir.actions.client',
                    'tag': 'display_notification',
                    'params': {
                        'title': 'Vérification',
                        'message': 'Le prix est valide !',
                        'type': 'success',  
                        'sticky': False,    
                    }
                }