# -*- coding: utf-8 -*-

from odoo import models, fields


class RepositoryRepository(models.Model):
    _inherit = 'repository.repository'

    saas_db_ids = fields.Many2many('saas.db', string='SaaS Databases')

