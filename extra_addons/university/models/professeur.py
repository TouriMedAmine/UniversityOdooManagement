# - * - coding: utf - 8 -
# *-
#
from odoo import models, fields, api


class UniversityProfesseur(models.Model):
    _name = 'university.professeur'

    f_name = fields.Char('Prenom')
    l_name = fields.Char('Nom')
    sexe = fields.Selection([('masculin', 'Masculin'), ('feminin', 'Feminin')])
    cin = fields.Char('CIN')
    adresse = fields.Text('Adresse')
    dateNaissance = fields.Date('Date de naissance')
    email = fields.Char()
    numero = fields.Char()

    departement_id = fields.Many2one(comodel_name='university.departement')
    classe_ids = fields.One2many(comodel_name='university.classe', inverse_name='professeur_id')


    def name_get(self):
        resultat = []
        for professeur in self:
            name = '[' + professeur.departement_id.nomDepartement + '] '+ professeur.l_name +' '+professeur.f_name
            resultat.append((professeur.id,name))
        return resultat

#
