from odoo import models, fields

class Notice(models.Model) :
    _name = 'library.notice'
    _description = 'Les avis'

    content = fields.Text("Content", required=True)
    book_id = fields.Many2one("library.book", string="Book", required=True)