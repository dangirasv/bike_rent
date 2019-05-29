from odoo import api, models


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
