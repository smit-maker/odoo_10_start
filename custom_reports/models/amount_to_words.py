from num2words import num2words
from odoo import models, fields, api, _

class AmountToWord(models.Model):
    _inherit = 'purchase.order'

    amount_to_word = fields.Char("Amount In Word", compute="compute_in_word")

    @api.depends('amount_total')
    def compute_in_word(self):
        for record in self:
            if record.amount_total :
                record.amount_to_word = num2words(round(record.amount_total), lang='en_IN')

