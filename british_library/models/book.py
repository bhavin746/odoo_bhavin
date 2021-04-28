from odoo import models,fields,api

class BookBook(models.Model):
    _name = 'book.books'
    _description = 'Book Books'
    _rec_name = 'title'


    title = fields.Char(string='Title',required=True)
    description = fields.Text()
    about = fields.Text()
    image= fields.Binary(string='Image')
    author_id = fields.Many2one('library.authors','Author')
    publisher = fields.Char(string='Publisher')
    edition = fields.Char(string="Edition")
    price = fields.Float(string="Price")



    def test(self):
        print("vvv")

