from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    rent_ids = fields.One2many('bike.rent', 'partner_id', string='Rent Records')
    rent_count = fields.Integer(compute='_compute_rent_count', string='Rent Count')

    @api.depends('rent_ids')
    def _compute_rent_count(self):
        for record in self.filtered('id'):
            record.rent_count = len(self.env['bike.rent'].search([('partner_id', 'child_of', self.id)]))

    def rent_history(self):
        act = self.env.ref('bike_rent.bike_rent_action').read()[0]
        act['domain'] = [('partner_id', 'child_of', self.id)]
        return act
