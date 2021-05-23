from odoo import models, fields, api, _


class FinancesDomestiquesGrupMoviment(models.Model):
    _name = 'financesdomestiques.grupmoviment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Grup del moviment financer'
    _rec_name = 'grupmoviment'

    @api.multi
    def open_moviments_grup(self):
        return {
            'name': _('Moviments'),
            'domain': [('id_detallmoviment.id_subgrupmoviment.id_grupmoviment', '=', self.id)],
            'view_type': 'form',
            'res_model': 'financesdomestiques.moviment',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }

    def get_moviments_count(self):
        count = self.env['financesdomestiques.moviment'].search_count(
            [('id_detallmoviment.id_subgrupmoviment.id_grupmoviment', '=', self.id)])
        self.moviments_count = count

    @api.onchange('grupmoviment')
    def set_upper(self):
        self.grupmoviment = str(self.grupmoviment).upper() if self.grupmoviment else ''
        return

    grupmoviment = fields.Char(string="Grup de moviment", required=True)
    color = fields.Char(string="Color", required=True, default='#DDDDDD')
    user_id = fields.Many2one('res.users', string='Related User')
    name_seq = fields.Char(string='Ref. Grup moviment ', required=True, copy=False, readonly=True, index=True,
                           default=lambda self: _('New'))

    moviments_count = fields.Integer(string='Moviment', compute='get_moviments_count')

    @api.model
    def create(self, vals):
        if vals.get('name_seq', _('New')) == _('New'):
            vals['name_seq'] = self.env['ir.sequence'].next_by_code('financesdomestiques.grupmoviment.sequence') or _(
                'New')
        result = super(FinancesDomestiquesGrupMoviment, self).create(vals)
        return result
