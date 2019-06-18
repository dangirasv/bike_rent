from odoo import api, models


class Website(models.Model):
    _inherit = 'website'

    @api.multi
    def sale_product_domain(self):
        result = super(Website, self).sale_product_domain()
        result += [('bike_shop', '=', True), ('type', '=', 'service')]
        return result
