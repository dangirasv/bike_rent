from odoo import api, fields, models
from datetime import timedelta


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.multi
    def action_confirm(self):

        # <AndriusD code
        def filter_rests(rec):
            product = rec.product_id
            return product.is_bike and product.type == 'service'

        for record in self.order_line.filtered(filter_rests):  # /AndriusD code>
            rent_rec = self.env['bike.rent'].create({
                'notes': record.name,
                'price': record.price_total,
                'partner_id': record.order_partner_id.id,
                'bike_id': record.product_id.id,
                'rent_time': record.product_id.rent_duration,
            })
            record.bike_rent_id = rent_rec.id
        return super(SaleOrder, self).action_confirm()


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    rent_end_date = fields.Datetime(string='Rent End Date', compute='_compute_rent_end_date')
    bike_rent_id = fields.Many2one('bike.rent', string='Rent ID')

    @api.multi
    def _compute_rent_end_date(self):
        for line in self.filtered(lambda x: x.product_id.type == 'service' and x.product_id.is_bike):
            if line.state == 'draft' or line.state == 'sent':
                line.rent_end_date = fields.Datetime.now() + timedelta(days=line.product_id.rent_duration)
            else:
                line.rent_end_date = line.bike_rent_id.rent_stop
