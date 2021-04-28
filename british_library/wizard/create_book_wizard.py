from odoo import api,fields,models

class CreateBook(models.TransientModel):
    _name = 'create.book'

    title_id = fields.Many2one('book.books',string="Title")
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'other')
    ], required=True, default='male')


    def create_book(self):
        print("fff",self)
        for res in self:
            print('.........',res.title_id)
            print("fasff",res.gender)
