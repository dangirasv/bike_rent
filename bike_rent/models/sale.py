from datetime import timedelta
from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.multi
    def action_confirm(self):

        # <AndriusD code
        def filter_rests(rec):
            product = rec.product_id
            return product.is_bike and product.type == 'service'  # /AndriusD code>

        def create_bike_rent_objects(so_record):
            for record_line in so_record.product_id.rented_bike_ids:
                rent_rec = self.env['bike.rent'].create({
                    'notes': so_record.product_id.description_sale,
                    'price': record_line.lst_price,
                    'partner_id': so_record.order_partner_id.id,
                    'bike_id': record_line.id,
                    'rent_time': so_record.product_id.rent_duration,
                    'sale_id': so_record.order_id.id
                })
                record.bike_rent_id = rent_rec.id

        for record in self.order_line.filtered(filter_rests):  # AndriusD code line
            create_bike_rent_objects(record)

        return super(SaleOrder, self).action_confirm()


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    rent_end_date = fields.Datetime(string='Rent End Date', compute='_compute_rent_end_date')
    bike_rent_id = fields.Many2one('bike.rent', string='Rent ID')

    @api.multi
    def _compute_rent_end_date(self):
        for line in self.filtered(lambda x: x.product_id.type == 'service' and x.product_id.is_bike):
            if line.bike_rent_id.rent_stop:
                line.rent_end_date = line.bike_rent_id.rent_stop
            else:
                line.rent_end_date = fields.Datetime.now() + timedelta(days=line.product_id.rent_duration)
