#-*- coding: utf-8 -*-
from odoo import models, fields

class Book(models.Model):
    _name = 'library.book'
    _description = 'Les livres'

    name= fields.Char("Title", required=True)
    isbn = fields.Char("isbn")
    active = fields.Boolean("Actif ?", default=True)
    date_published = fields.Date("Date published")
    image = fields.Binary("Cover")
    