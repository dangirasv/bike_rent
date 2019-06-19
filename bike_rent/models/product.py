from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_bike = fields.Boolean(string="It's a Bike")
    bike_shop = fields.Boolean(string='Available in Shop')
    manufacturer = fields.Char(string='Manufacturer')
    model = fields.Char(string='Model')


class ProductProduct(models.Model):
    _inherit = 'product.product'

    rent_ids = fields.One2many('bike.rent', 'bike_id', string='Rent Records')
    rent_duration = fields.Integer(string='Rent Duration (Days)')
    product_bike_id = fields.Many2one(
        'product.product',
        string='Bike ID',
        index=True,
        ondelete='cascade',
        domain=[('is_bike', '=', True)],
    )
    rented_bike_ids = fields.One2many('product.product', 'product_bike_id', string='Rented Bikes')
