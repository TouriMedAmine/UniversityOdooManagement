# - * - coding: utf - 8 -
# *-
#
from odoo import models, fields, api


class UniversityFiliere(models.Model):
    _name = 'university.filiere'

    filiere = fields.Selection([('informatique','Informatique'),('stat eco','Stat Eco')])
    annee = fields.Selection([('1','1'),('2','2'),('3','3')])

    etudiant_ids = fields.One2many(comodel_name='university.etudiant', inverse_name='filiere_id')
    classe_ids = fields.One2many(comodel_name='university.classe', inverse_name='filiere_id')


    def name_get(self):
        resultat = []
        for filiere in self:
            name =  filiere.filiere +' '+filiere.annee +"année"
            resultat.append((filiere.id,name))
        return resultat