from odoo import api,fields,models
from odoo.exceptions import ValidationError


class LibraryStudent(models.Model):
    _name = 'library.students'
    _description = 'Library Students'
    _rec_name='name'

    book_ids = fields.Many2many('interest.book','student_book_rel','stu_id','bk_id')
    book_id = fields.Many2one('interest.book','Book')
    sequence = fields.Integer(string='Sequence')
    active = fields.Boolean('Active',default=True)
    name = fields.Char(string='Student')
    age = fields.Integer(string='Age')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'other')
    ], required=True, default='male')
    blood_group = fields.Selection([
        ('a+', 'A+'),
        ('o+', 'O+'),
        ('b+', 'B+'),
        ('ab+','AB+')],required=True,default='a+',string='Blood Group')
    address = fields.Text(string='Address')
    contact = fields.Char(string='Contact')
    email = fields.Char(string='Email')

    @api.constrains('contact')
    def check_contact(self):
        for record in self:
            if record.contact and len(record.contact) !=10:
                raise ValidationError("Enter valid contact...!")
       # Use of name get function
    # def name_get(self):
    #     res = []
    #     for rec in self:
    #         res.append((rec.id, '%s %s' % (rec.contact,rec.gender)))
    #     return res
    #

    _sql_constraints = [
        ('name_unique',
         'UNIQUE(contact)',
         'Please enter unique number'
         ),
    ]

    # @api.model
    # def create(self,val_list):
    #     print("\n\n Create is called.......",self,val_list)
    #     book_name = super(LibraryStudent,self).create(val_list)
    #     print("After super called",book_name)
    #     book_name.write({'name':'New00' +str(book_name.id)})
    #     return book_name
    #
    # def write(self,vals):
    #     print("........f.....",self,vals)
    #     res = super(LibraryStudent,self).write(vals)
    #     print(".......res...",res)
    #     return res



    # @api.model
    # def search(self, domain, offset=0, limit=None, order=None, count=False):
    #     """SQL select id from table_name where gender='male'
    #         @return: Matching recordsets
    #     """
    #     print("\n\nSearch is called.......", self, domain, offset, limit, order, count)
    #     names = super(LibraryStudent, self).search(domain, offset=offset, limit=limit,
    #                                 order=order, count=count)
    #     return names


    def wiz_open(self):
        return self.env['ir.actions.act_window']._for_xml_id('british_library.student_update_action')

        # return {'type':'ir.actions.act_window',
        #         'res_model':'student.update.wizard',
        #         'view_mode':'form',
        #         'target':'new'}

    def view_book(self):
        # return {
        #     'name' : 'Book',
        #     'view_type' : 'form',
        #     'view_mode' : 'tree,form',
        #     'res_model' : 'interest.book',
        #     'domain' : [('id','in',self.book_ids.ids)],
        #     'type' : 'ir.actions.act_window',
        #
        # }

        partners = self.env['res.partner'].search([])
        print("....partner",partners.mapped('name'))
        print("....partner",partners.mapped('phone'))
        print("....partner",partners.sorted(lambda a:a.id))
        print("....partner",partners.sorted(lambda a:a.id,reverse=True))
        print("....partner",partners.filtered(lambda a:a.is_teacher))



    def update_book(self):
        books = self.env['interest.book'].search([('interest_book','ilike','History')])
        print(".....booksupdate...",books)
        for book in self:
            for bk in books:
                book.write({'book_ids':[(1,bk.id,{'price':2050})]})
            return True

    def remove_book(self):
        books = self.env['interest.book'].search([('interest_book','ilike','History')])
        print("...book remove..",books)
        for book in self:
            for bk in books:
                book.write({'book_ids': [(3,bk.id)]})

    def add_book(self):
        books = self.env['interest.book'].search([('interest_book','ilike','History')])
        print("....book add...",books)
        for book in self:
            for bk in books:
                book.write({'book_ids':[(4,bk.id)]})

    def removeall_book(self):
        for book in self:
            book.write({'book_ids':[(5,0,0)]})

    def replaceall_book(self):
        books = self.env['interest.book'].search([('interest_book','ilike','History')])
        print("...replace..",books)
        for book in self:
            for bk in books:
                book.write({'book_ids': [(6,0,bk.ids)]})

