from odoo import fields, models

class StudentData(models.Model):
    _name = "student.data"
    _rec_name = "s_name"

    s_name = fields.Char(string="Student Name", copy=False, require=True)
    # s_id = fields.Many2one("issue.books",string="Student Id")
    s_email = fields.Char(string="Email", copy=False, required=True)
    s_phone = fields.Char("Phone", copy=False, required=True)

class BookData(models.Model):
    _name = "book.data"
    _rec_name = "b_name"

    b_name = fields.Char(string="Book Name", copy=False, required=True)
    # b_id = fields.Many2one("issue.books",string="Book Id")
    author_name = fields.Char(string="Author Name", copy=False, required=True)

class IssueBooks(models.Model):
    _name = "issue.books"

    s_id = fields.Many2one("student.data", string="Student Name")
    b_id = fields.Many2many("book.data", "b_name", string="Book Name")
    # b_list = fields.Selection( string="Book List")
