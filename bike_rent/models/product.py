from odoo import models, fields


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_bike = fields.Boolean(string="It's a Bike")
    manufacturer = fields.Char(string='Manufacturer')
    model = fields.Char(string='Model')


class ProductProduct(models.Model):
    _inherit = 'product.product'

    rent_ids = fields.One2many('bike.rent', 'bike_id', string='Rent Records')
