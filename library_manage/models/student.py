from odoo import fields, models, api
import datetime

class StudentData(models.Model):
    _name = "student.data"
    _description = "Student Data"
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
    _description = "Book Data"
    _rec_name = "b_name"

    b_name = fields.Char(string="Book Name", copy=False, required=True)
    b_info = fields.Text(string="Book Information")
    author_name = fields.Char(string="Author Name", copy=False, required=True)
    no_of_book = fields.Integer(string="Books Quantity")
    issue_book = fields.Integer(string="Issue Book")

class IssueBooks(models.Model):
    _name = "issue.books"
    _description = "Issue Book"

    s_id = fields.Many2one("student.data", string="Student Name")
    b_issue = fields.One2many("book.info", "b_id", string="Book Qua")
    issue_date = fields.Datetime("Issue Date", default=fields.Datetime.now())
    state = fields.Selection([
        ('draft', 'Draft'),
        ('issue', 'Issue'),
        ('receive', 'Receive'),
    ], string='Status', default='draft', index=True, readonly=True)
    y = fields.Many2one("book.data", string="book Data") #

    @api.multi
    def action_issue(self):
        for i in self.b_issue:
            # print(i.x.issue_book)
            if (i.a_quantity - i.x.issue_book) >= i.no_qu:
                self.state = 'issue'
                i.x.issue_book = i.x.issue_book + i.no_qu

    @api.multi
    def action_receive(self):
        for i in self.b_issue:
            i.x.issue_book = i.x.issue_book - i.no_qu
        self.state = 'receive'

    @api.multi
    def cancel(self):
        if self.state == 'issue':
            for i in self.b_issue:
                i.x.issue_book = i.x.issue_book - i.no_qu
        self.state = 'draft'

class BookInfo(models.Model):
    _name = "book.info"
    _description = "Book Info . . ."


    b_id = fields.Many2one("issue.books", string="Book Name") #relation issue book
    x = fields.Many2one("book.data", string="book Data") #relation book data
    no_qu = fields.Integer(string="Issue Quantity", required=True) #input to no of book parches
    a_quantity = fields.Integer(string="avalable Quantity") #show the actual Quantity
    r_quantity = fields.Integer(string="R Quantity") #Remaning Quantity

    @api.onchange('x')
    def actual_quantity(self):
        for i in self:
            if i.x:
                i.a_quantity = i.x.no_of_book - i.x.issue_book

    @api.onchange('no_qu', 'a_quantity')
    def remaning_quantity(self):
        for j in self:
            if j.x:
                j.r_quantity = j.a_quantity - j.no_qu
        print(self.x)

