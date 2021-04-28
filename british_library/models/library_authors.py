from odoo import models,fields

class LibraryAuthors(models.Model):
    _name = 'library.authors'
    _description = 'Authors Records'
    _rec_name = 'author'


    author = fields.Char(string='Authors Name')
    author_image = fields.Binary(string='Authors Image',attachment=True)
    books_number = fields.Integer(string='Number of Books')
    birth_date = fields.Date(string='Birth of Date')
    death_date = fields.Date(string='Death of Date')
    biography = fields.Text('Biography')
    note = fields.Text('Notes')