# -*- coding: utf-8 -*-

from odoo import models, fields

class conference(models.Model):
    _name = 'myconferences.conference'
    _description = 'a model for a conference'

    confname = fields.Char('Conference Name', required=True)
    indexed = fields.Boolean('Indexed?', required=True)
    startdate = fields.Date('Start Date', required=True)
    enddate = fields.Date('End Date', required=True)
    fee = fields.Float('Registration Fee', required=True)
