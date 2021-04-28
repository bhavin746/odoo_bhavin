from odoo import api,fields,models


class LibraryInterstedBook(models.Model):
    _name = 'interest.book'
    _rec_name = 'interest_book'

    interest_book = fields.Char('Book')
    price = fields.Float("Price")


