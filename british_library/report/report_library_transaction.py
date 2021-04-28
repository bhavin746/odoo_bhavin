from odoo import api,models,_

class ReportLibraryTransaction(models.AbstractModel):
    _name = 'report.british_library.report_library_transaction'

    @api.model
    def _get_report_values(self,docids,data=None):
        print("\n\nMy Paremeter report parser....",docids,data)
        return {
            'doc_ids':docids,
            'doc_model':'library.transactions',
            'docs' : self.env['library.transactions'].browse(docids)
        }