# -*- coding: utf-8 -*-
'''
This module is about course manager
'''

from openerp import models, fields

class Course(models.Model):
    '''
    This class create a module for course entity
    '''
    _name = 'openacademy.course' # Model odoo name
    name = fields.Char(string='Title', required=True) # Field reserved to record name
    description = fields.Text(string='Description')
