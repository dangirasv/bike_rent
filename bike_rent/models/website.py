from odoo import api, models


class Website(models.Model):
    _inherit = 'website'

    @api.multi
    def sale_product_domain(self):
        return [('sale_ok', '=', True), ('bike_shop', '=', True), ('type', '=', 'service')] +\
               self.get_current_website().website_domain()
