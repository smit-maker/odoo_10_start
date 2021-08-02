from odoo import fields, models, api

class StudentProfile(models.Model):
    _name = "student.profile"
    # _inherit = "student.profile"
    # school_id = fields.Many2one("school.profile", string="School Name")
    s_name = fields.Char(string="Student Name", copy=False, required = True)
    s_email = fields.Char(string="Email", copy=False, required = True)
    s_phone = fields.Char("Phone", copy=False, required = True)
    join_date = fields.Datetime("Join Date")
    result = fields.Float(compute='_get_sum', string="Result")
    sub1 = fields.Float(string="SUBJECT 01")
    sub2 = fields.Float(string="SUBJECT 02")
    sub3 = fields.Float(string="SUBJECT 03")

    @api.depends('sub1', 'sub2', 'sub3')
    def _get_sum(self):
        for i in self:
            i.result = i.sub1 + i.sub2 + i.sub3
            i.result = i.result / 3


class SchoolProfile(models.Model):
    _name = "school.profile"
    # _inherit = "school.profile"

    name = fields.Char(string="School Name", copy=False, required = True)
    # school_list = fields.One2many("school.profile", "school_id", string="schools List")
    email = fields.Char(string="Email", copy=False,  required = True)
    phone = fields.Char("Phone", copy=False, required = True)
    school_rank = fields.Integer(string="Rank")
    address = fields.Text(string="Address")
    open_date = fields.Datetime("Open Date")
    # currency_id = fields.Many2one("res.currency", string="Currency")
    school_type = fields.Selection([('public', 'Public School'),
                                    ('private', 'Private School')],
                                   string="Type of School",
                                   required=True
                                   )

class Mark(models.Model):
    _name = "marks.profile"

    mark = fields.Float(string="Total Makes")
    result = fields.Float(string="Result")