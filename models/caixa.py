from odoo import models, fields, api, _


class FinancesDomestiquesCaixa(models.Model):
    _name = 'financesdomestiques.caixa'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Caixa del moviment financer'
    _rec_name = 'caixa'

    @api.multi
    def activa_desactiva(self):
        if self.env.user in self.user_id:
            self.write({'user_id': [(3, self.env.user.id)]})
            self.active = 'Inactiva'
        else:
            self.write({'user_id': [(4, self.env.user.id)]})
            self.active = 'Activa'
        return True

    def get_caixa_activa(self):
        self.active = 'Activa' if self.env.user in self.user_id else 'Inactiva'

    caixa = fields.Char(string="Caixa", required=True)
    color = fields.Char(string="Color", required=True, default='#DDDDDD')
    user_id = fields.Many2many('res.users', string='Related User')
    name_seq = fields.Char(string='Ref. Caixa ', required=True, copy=False, readonly=True, index=True,
                           default=lambda self: _('New'))

    active = fields.Char(string="Active", compute='get_caixa_activa')


    @api.model
    def create(self, vals):
        if vals.get('name_seq', _('New')) == _('New'):
            vals['name_seq'] = self.env['ir.sequence'].next_by_code('financesdomestiques.caixa.sequence') or _('New')

        result = super(FinancesDomestiquesCaixa, self).create(vals)
        return result
