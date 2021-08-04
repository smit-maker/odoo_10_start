from odoo import fields, models, api
import datetime

class StudentData(models.Model):
    _name = "student.data"
    _rec_name = "s_name"

    s_name = fields.Char(string="Student Name", copy=False, require=True)
    s_email = fields.Char(string="Email", copy=False, required=True)
    s_phone = fields.Char("Phone", copy=False, required=True)
    s_gender = fields.Selection([('male', 'Male'), ('female', 'Female')], required=True,
                                string="Gender")
    address = fields.Text(string="Address")
    join_date = fields.Datetime("Join Date")

class BookData(models.Model):
    _name = "book.data"
    _rec_name = "b_name"

    b_name = fields.Char(string="Book Name", copy=False, required=True)
    b_info = fields.Text(string="Book Information")
    author_name = fields.Char(string="Author Name", copy=False, required=True)
    no_of_book = fields.Integer(string="Books Quantity", required=True)

class IssueBooks(models.Model):
    _name = "issue.books"

    s_id = fields.Many2one("student.data", string="Student Name")
    b_id = fields.Many2many("book.data", "b_name", string="Book Name")
    issue_date = fields.Datetime("Issue Date", default=fields.Datetime.now())
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirmed'),
        ('issue', 'Issue'),
    ], string='Status', default='draft', index=True, readonly=True)

    @api.multi
    def action_done(self):
        self.state = 'confirm'

    @api.multi
    def action_confirm(self):
        self.state = 'issue'

    @api.multi
    def cancel(self):
        self.state = 'draft'
