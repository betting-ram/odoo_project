# -*- coding: utf-8 -*-

from odoo import models, fields, api
from . import phonebook

class new_module(models.Model):
 	_inherit = 'sale.order'
 	new_field = fields.Char(string = 'order number')

