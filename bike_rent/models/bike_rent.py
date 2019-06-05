# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo import exceptions
from datetime import timedelta


class BikeRent(models.Model):
    _name = 'bike.rent'
    _description = 'basic class to hold bike rent info'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    bike_id = fields.Many2one('product.product', string='Bike', required=True, domain=[('is_bike', '=', True)],)
    bike_description = fields.Text(related='bike_id.description', string='Description', store=True)
    image = fields.Binary(related='bike_id.image', string='Picture', store=True)
    partner_id = fields.Many2one('res.partner', string='Customer Name', required=True)
    price = fields.Float(string='Bike Rent Price')
    rent_start = fields.Datetime(string='Rent Start', default=fields.Datetime.now, required=True)
    rent_stop = fields.Datetime(string='End of Rent', compute='_compute_rent_stop', store=True)
    rent_time = fields.Integer(string='Rent Time (Days)')
    notes = fields.Text(string='Rent Notes')
    name = fields.Char(help='Model name, mainly used for UI purposes', default='Rent Info')

    @api.depends('rent_start', 'rent_time')
    def _compute_rent_stop(self):
        for record in self:
            record.rent_stop = record.rent_start + timedelta(days=record.rent_time)

    @api.onchange('rent_start', 'rent_stop')
    def _onchange_verify_stop_date(self):
        if self.rent_stop and self.rent_stop < self.rent_start:
            raise exceptions.UserError('End of Rent Time cannot be earlier than Rent Start Time')
