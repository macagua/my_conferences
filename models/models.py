# -*- coding: utf-8 -*-

from odoo import models, fields


class Conference(models.Model):
    # the model name (in dot-notation, module namespace)
    _name = 'myconferences.conference'
    # the model's informal name
    _description = 'Conferences'

    name = fields.Char('Conference Name', required=True)
    indexed = fields.Boolean('Indexed?', required=True)
    start_date = fields.Date('Start Date', required=True)
    end_date = fields.Date('End Date', required=True)
    fee = fields.Float('Registration Fee', required=True)

