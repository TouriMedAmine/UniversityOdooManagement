# - * - coding: utf - 8 -
# *-

from odoo import models, fields, api


class UniversityDepartement(models.Model):
    _name = 'university.departement'
    _rec_name = 'nomDepartement'

    nomDepartement = fields.Char('Nom du departement')
    code = fields.Char('code')

    professeur_ids = fields.One2many(comodel_name='university.professeur', inverse_name='departement_id')


