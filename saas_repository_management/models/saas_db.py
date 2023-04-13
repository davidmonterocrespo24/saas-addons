from odoo import models, fields


class SAASDB(models.Model):
    _inherit = 'saas.db'

    repository_ids = fields.Many2many('repository.repository', string='Repositories')
