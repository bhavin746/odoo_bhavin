from odoo import api, fields, models
# from odoo.addons.base.models.res_users import check_identity

class LibraryTransaction(models.Model):
    _name = 'library.transactions'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Library Transaction'
    _rec_name = 'student_id'

    student_id = fields.Many2one('library.students', 'Student', track_visibility='always')
    title_ids = fields.One2many('library.books', 'book_id', string='Title', required=True)
    contact = fields.Char('Contact')
    currency_id = fields.Many2one('res.currency', 'Currency', track_visibility='always')

    sub_total = fields.Integer('Sub Total', compute="_compute_subtotal")
    final_total = fields.Integer("Final Total (12% GST)", compute="_compute_subtotal")
    state = fields.Selection([
        ('paid', 'Paid'),
        ('unpaid', 'UnPaid'),
        ('cancel', 'Cancel')
    ], default='paid')

    def lib_paid(self):
        for record in self:
            # when record is archieve then automatic all record shown usinf astive_test
            # student = self.env['library.students'].search_count([])
            # print("fff",student)
            # allstuddent = self.env['library.students'].with_context(active_test=False).search_count([])
            # print("fjsdjfsdkjf",allstuddent)
            record.state = 'paid'

    def lib_unpaid(self):
        for record in self:
            record.state = 'unpaid'
            return {
                'effect':{
                    'fadeout' : 'slow',
                    'message' : 'Transaction is unpaid...',
                    'type' : 'rainbow_man',
                }
            }

    def lib_cancel(self):
        for record in self:
            record.state = 'cancel'

    @api.onchange('student_id')
    def _change(self):
        for record in self:
            if record.student_id:
                record.contact = record.student_id.contact

    @api.depends('title_ids')
    def _compute_subtotal(self):
        for record in self:
            record.sub_total = sum(rec.price * rec.quantity for rec in record.title_ids)
            record.final_total = record.sub_total + 0.12 * record.sub_total




    # set default values field
    # @api.model
    # def default_get(self,fields):
    #     res = super(LibraryTransaction,self).default_get(fields)
    #     res['student_id'] = 1
    #     return res

    # def view_tital(self):
    #     #odoo search
    #     students_obj = self.env['library.students']
    #     print("\n\n students_obj....",students_obj)
    #     #odoo with AND
    #     students = students_obj.search([('gender','=','male'),('age','<','22')])
    #     print("\n\n Gender....",students)
    #     #odoo with OR
    #     students_or = students_obj.search(['|',('gender','=','male'),('age','>=','22')])
    #     print("\n\n Student_or.......",students_or)
    #
    #     #count
    #     students_count = self.env['library.students'].search_count([])
    #     print("........student_count....",students_count)
    #     students = students_obj.search_count([('gender','=','male'),('age','<','22')])
    #     print("\n\n students.....",students)
    #
    #     #browse
    #     student_browse = self.env['library.students'].browse(12)
    #     print("\n\n Browse......",student_browse)
    #
    #     #exists
    #     if student_browse.exists():
    #         print("yaaaaaa......")
    #     else:
    #         print("nooooooooo.....oooo...")
    #
    #     return {
    #         'name':'Titles',
    #         'view_type':'form',
    #         'view_mode':'tree,form',
    #         'res_model':'library.books',
    #         'domain':[('id','in',self.title_ids.ids)],
    #         'type': 'ir.actions.act_window',
    #     }


    # check security

    # @check_identity
    def del_data(self):
        return super(LibraryTransaction, self).unlink()

    # def create_set(self):
    #     # 1st method automatic fill one2many field
    #     title_obj = self.env['library.books']
    #     title_obj.create([{'title_id' :15,'price':120,'quantity':2,'book_id':self.id}])

    #     2nd method
        # self.write({
        # 'title_ids' : [(0,0,{
        #     'title_id' : 15,
        #     'price' : 500,
        #     'quantity' : 1
        # }),
        #     (0, 0, {
        #         'title_id': 17,
        #         'price': 500,
        #         'quantity': 1
        #     })]
        # })
        #



