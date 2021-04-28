from odoo import models,fields,api

class LibraryBooks(models.Model):
    _name = 'library.books'
    _description = 'Library Books'
    _rec_name = 'title_id'

    book_id = fields.Many2one('library.transactions','Book Id')
    title_id = fields.Many2one('book.books','Title Name')
    sequence = fields.Integer(string='Sequence')
    curncy_id = fields.Many2one(related='book_id.currency_id')
    price = fields.Float(string="Price")
    quantity = fields.Float(string="Quantity")

    @api.onchange('title_id')
    def _on_change(self):
        for record in self:
            if record.title_id:
                record.price = record.title_id.price




