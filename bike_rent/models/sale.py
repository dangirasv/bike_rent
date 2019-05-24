from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_confirm_and_export(self):
        self.action_confirm()
        for record in self.order_line:
            self.env['bike.rent'].create({
                'notes': record.name,
                'price': record.price_total,
                'partner_id': record.order_partner_id.id,
                'bike_id': record.product_id.id,
                'rent_time': record.product_id.rent_duration,
            })
