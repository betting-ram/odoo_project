from odoo import models, fields, api
#from .import models


class PhoneBook(models.Model):
    _name = 'phone.book'
    _description = 'Phone book'

    name = fields.Char(string="Name", required=True)
    related_partner = fields.Many2one('res.partner', string="Related Partner")
    date_of_joining = fields.Date(string="Date of Joining")
    category_id = fields.Many2many('res.partner.category', string="Tags")
    city = fields.Char(string="City", required=True)
    street = fields.Char(string="street", required=True)
    country_id = fields.Many2one(
        'res.country', string="Country", required=True)
    address_for_printing = fields.Char('Printing Address')
    address = fields.Char('Full Address', compute='_calculate_address')

    def print_name(self):
        print("Name of the record: %s" % self.name)
        return True

    @api.depends('country_id', 'city', 'street')
    def _calculate_address(self):
        if self.city == False:
            return
        if self.street == False:
            return
        if self.country_id.name == False:
            return

        full_address = self.country_id.name + ' ,' + self.city + ' ,' + self.street
        self.address = full_address

        self.return_full_address()

    @api.model
    @api.onchange('name', 'address')
    def return_full_address(self):
        if self.name and self.address:
            self.address_for_printing = 'customer: ' + self.name + ' ' + self.address

    @api.model
    def create(self, values):
        if 'name' in values:
            values['name'] = values['name'].upper()
            new_rec = super(PhoneBook, self).create(values)
            return new_rec
