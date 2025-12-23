from odoo import models, fields


class Session(models.Model):
    _name = 'guitar_rig.session'
    _description = 'Session de jeu / répète / enregistrement'

    name = fields.Char("Titre", required=True)
    start_datetime = fields.Datetime("Début de session", required=True)
    duration = fields.Float("Durée (heures)")
    mood = fields.Selection(
        [
            ('ok', 'OK'),
            ('great', 'Grande inspi'),
            ('bad', 'Pas en forme'),
        ],
        string="Humeur"
    )
    notes = fields.Text("Notes sur la session")


    # 1-N : Many2one vers le gear principal
    main_gear_id = fields.Many2one(
        'guitar_rig.gear',
        string="Matos principal"
    )

    # N-N : tous les gear utilisés
    gear_ids = fields.Many2many(
        'guitar_rig.gear', 'guitar_session_gear_rel',
        'session_id', 'gear_id',
        string="Matos utilisés"
    )




