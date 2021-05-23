from odoo import models, fields, api, _


class FinancesDomestiquesFormaPagament(models.Model):
    _name = 'financesdomestiques.formapagament'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Forma de pagament del moviment financer'
    _rec_name = 'formapagament'

    formapagament = fields.Char(string="Forma de pagament", required=True)
    user_id = fields.Many2one('res.users', string='Related User')
    name_seq = fields.Char(string='Ref. Forma pagament ', required=True, copy=False, readonly=True, index=True,
                           default=lambda self: _('New'))

    @api.model
    def create(self, vals):
        if vals.get('name_seq', _('New')) == _('New'):
            vals['name_seq'] = self.env['ir.sequence'].next_by_code('financesdomestiques.formapagament.sequence') or _(
                'New')

        result = super(FinancesDomestiquesFormaPagament, self).create(vals)
        return result
