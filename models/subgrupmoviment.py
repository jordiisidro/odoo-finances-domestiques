from odoo import models, fields, api, _


class FinancesDomestiquesSubgrupMoviment(models.Model):
    _name = 'financesdomestiques.subgrupmoviment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Subgrup del moviment financer'
    _rec_name = 'subgrupmovimentstr'
    _order = 'subgrupmovimentstr'

    @api.depends('id_grupmoviment')
    def _compute_subgrup_moviment_str(self):
        for rec in self:
            rec.subgrupmovimentstr = rec.id_grupmoviment.grupmoviment + '\\' \
                                     + rec.subgrupmoviment if rec.id_grupmoviment else False

    subgrupmoviment = fields.Char(string="Subgrup de moviment", required=True)
    id_grupmoviment = fields.Many2one('financesdomestiques.grupmoviment', string='Grup moviment')

    subgrupmovimentstr = fields.Char(compute='_compute_subgrup_moviment_str', string='Subgrup moviment', store="True")

    user_id = fields.Many2one('res.users', string='Related User')
    name_seq = fields.Char(string='Ref. Subgrup moviment ', required=True, copy=False, readonly=True, index=True,
                           default=lambda self: _('New'))

    @api.model
    def create(self, vals):
        if vals.get('name_seq', _('New')) == _('New'):
            vals['name_seq'] = self.env['ir.sequence'].next_by_code(
                'financesdomestiques.subgrupmoviment.sequence') or _('New')

        result = super(FinancesDomestiquesSubgrupMoviment, self).create(vals)
        return result
