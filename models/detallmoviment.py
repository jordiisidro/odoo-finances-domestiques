from odoo import models, fields, api, _


class FinancesDomestiquesDetallMoviment(models.Model):
    _name = 'financesdomestiques.detallmoviment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Detall del grup del moviment financer'
    _rec_name = 'detallmovimentstr'
    _order = 'detallmovimentstr'

    @api.depends('id_subgrupmoviment')
    def _compute_grup_moviment(self):
        for rec in self:
            rec.grupmoviment = rec.id_subgrupmoviment.id_grupmoviment.grupmoviment if rec.id_subgrupmoviment else False

    @api.depends('id_subgrupmoviment')
    def _compute_detall_moviment_str(self):
        for rec in self:
            rec.detallmovimentstr = rec.id_subgrupmoviment.id_grupmoviment.grupmoviment + '\\' \
                                    + rec.id_subgrupmoviment.subgrupmoviment + '\\' \
                                    + rec.detallmoviment if rec.id_subgrupmoviment else False

    @api.multi
    def open_moviments_detall(self):
        return {
            'name': _('Moviments'),
            'domain': [('id_detallmoviment', '=', self.id)],
            'view_type': 'form',
            'res_model': 'financesdomestiques.moviment',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }

    def get_moviments_count(self):
        count = self.env['financesdomestiques.moviment'].search_count([('id_detallmoviment', '=', self.id)])
        self.moviments_count = count

    id_subgrupmoviment = fields.Many2one('financesdomestiques.subgrupmoviment', string='Subgrup moviment')
    detallmoviment = fields.Char(string="Detall de moviment", required=True)
    grupmoviment = fields.Many2one(string='Grup moviment', related='id_subgrupmoviment.id_grupmoviment', store=True)
    # grupmoviment = fields.Char(compute='_compute_grup_moviment', string='Grup moviment')
    detallmovimentstr = fields.Char(compute='_compute_detall_moviment_str', string='Detall moviment', store =True)

    moviments_count = fields.Integer(string='Moviment', compute='get_moviments_count')
    active = fields.Boolean("Active", default=True)

    user_id = fields.Many2one('res.users', string='Related User')
    name_seq = fields.Char(string='Ref. Detall moviment ', required=True, copy=False, readonly=True, index=True,
                           default=lambda self: _('New'))

    @api.model
    def create(self, vals):
        if vals.get('name_seq', _('New')) == _('New'):
            vals['name_seq'] = self.env['ir.sequence'].next_by_code('financesdomestiques.detallmoviment.sequence') or _(
                'New')

        result = super(FinancesDomestiquesDetallMoviment, self).create(vals)
        return result
