from odoo import api,fields,models

class StudentUpdateWizard(models.TransientModel):
    _name = 'student.update.wizard'

    student = fields.Char(string='Student')


    def update_student(self):
        print("Yeahhhhhhhh",self)
        res = self.env['library.students'].browse(self._context.get('active_ids')).update({'name':self.student})
        return res