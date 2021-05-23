from odoo import models, fields, api, _


class FinancesDomestiquesMoviment(models.Model):
    _name = 'financesdomestiques.moviment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Moviment financer'
    _order = 'datamoviment desc'
    _rec_name = 'name_seq'

    @api.depends('id_detallmoviment')
    def _compute_grup_moviment_str(self):
        for rec in self:
            rec.grupmoviment = rec.id_detallmoviment.id_subgrupmoviment.id_grupmoviment.grupmoviment \
                if rec.id_detallmoviment else False

    @api.depends('id_detallmoviment')
    def _compute_subgrup_moviment_str(self):
        for rec in self:
            rec.subgrupmoviment = rec.id_detallmoviment.id_subgrupmoviment.subgrupmoviment \
                if rec.id_detallmoviment else False

    @api.depends('id_detallmoviment')
    def _compute_detall_moviment_str(self):
        for rec in self:
            rec.detallmoviment = rec.id_detallmoviment.detallmoviment \
                if rec.id_detallmoviment else False



    id_detallmoviment = fields.Many2one('financesdomestiques.detallmoviment', string='Detall moviment')
    id_caixa = fields.Many2one('financesdomestiques.caixa', string='Caixa')
    id_formapagament = fields.Many2one('financesdomestiques.formapagament', string='Forma Pagament')
    datamoviment = fields.Date(string="Data del moviment", required=True)
    base_currency_id = fields.Many2one('res.currency')
    importmoviment = fields.Monetary(string="Import del moviment", required=True, currency_field='base_currency_id')

    grupmoviment = fields.Char(compute='_compute_grup_moviment_str', string='Grup moviment', store=True)
    subgrupmoviment = fields.Char(compute='_compute_subgrup_moviment_str', string='Subgrup moviment', store=True)
    detallmoviment = fields.Char(compute='_compute_detall_moviment_str', string='Detall moviment', store=True)

    user_id = fields.Many2one('res.users', string='Related User', default=lambda self: self.env.user)
    name_seq = fields.Char(string='Ref. Moviment ', required=True, copy=False, readonly=True, index=True,
                           default=lambda self: _('New'))

    @api.model
    def create(self, vals):
        if vals.get('name_seq', _('New')) == _('New'):
            vals['name_seq'] = self.env['ir.sequence'].next_by_code('financesdomestiques.moviment.sequence') or _(
                'New')

        result = super(FinancesDomestiquesMoviment, self).create(vals)
        return result
