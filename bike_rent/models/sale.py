from odoo import api, fields, models
from datetime import timedelta


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.multi
    def action_confirm(self):

        def filter_rests(rec):
            product = rec.product_id
            return product.is_bike and product.type == 'service'

        for record in self.order_line.filtered(filter_rests):
            self.env['bike.rent'].create({
                'notes': record.name,
                'price': record.price_total,
                'partner_id': record.order_partner_id.id,
                'bike_id': record.product_id.id,
                'rent_time': record.product_id.rent_duration,
            })
        return super(SaleOrder, self).action_confirm()


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    # Cannot be stored since depends on Datetime.now()
    rent_end_date = fields.Datetime(string='Rent End Date', compute='_compute_rent_end_date', store=False)

    @api.multi
    def _compute_rent_end_date(self):
        for line in self.filtered(lambda x: x.product_id.type == 'service' and x.product_id.is_bike):
            line.rent_end_date = fields.Datetime.now() + timedelta(days=line.product_id.rent_duration)

