from odoo import http
from odoo.http import request

class Library(http.Controller):
    #
    # @http.route('/library/student/',website=True,auth='public')
    # def library_student(self,**kw):
    #     return "Hello student"
        # students = request.env['library.students'].sudo().search([])
    #     print("....",students)
    #     return request.render("british_library.library_student",{
    #         'students': students
    #     })

    @http.route('/student_webfrom',type='http',auth='public',website=True)
    def student_webform(self,**kw):
        book_rec = request.env['interest.book'].sudo().search([])
        return http.request.render('british_library.create_students',{'name' : 'Bhavin Vekariya',
                                                                      'book1_rec':book_rec})

    @http.route('/create/webstudent',type='http',auth="public",website=True)
    def create_webstudent(self,**kw):
        print('...data...',kw)
        request.env['library.students'].sudo().create(kw)
        # as well as author name create
        author_val = {
            'author' : kw.get('name')
        }
        request.env['library.authors'].sudo().create(author_val)
        return request.render('british_library.student_thanks',{})