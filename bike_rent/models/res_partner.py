from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    rent_ids = fields.One2many('bike.rent', 'partner_id', string='Rent Records')
    rent_count = fields.Integer(compute='_compute_rent_count', string='Rent Count')

    @api.depends('rent_ids')
    def _compute_rent_count(self):
        for record in self:
            record.rent_count = len(self.env['bike.rent'].search([('partner_id', 'child_of', self.id)]))

    def rent_history(self):
        return {
            'name': "Rent History",
            'type': 'ir.actions.act_window',
            'res_model': 'bike.rent',
            'view_mode': 'tree,form',
            'domain': "[('partner_id', 'child_of', active_id)]",
        }
