#  -*- coding: utf-8 -*-
#
from odoo import models, fields, api


class UniversityEtudiant(models.Model):
    _name = 'university.etudiant'

    f_name = fields.Char('Prenom')
    l_name = fields.Char('Nom')
    sexe = fields.Selection([('masculin','Masculin'),('feminin','Feminin')])
    cin = fields.Char('CIN')
    adresse = fields.Text('Adresse')
    redoublant = fields.Selection([('oui','Redoublant'),('non','Non redoublant')])
    dateNaissance = fields.Date('Date de naissance')
    email = fields.Char()
    numero = fields.Char()

    classe_ids = fields.Many2many(comodel_name='university.classe',
                                relation='etudiant_classe_rel',
                                column1='cin',
                                column2='classe')
    filiere_id = fields.Many2one(comodel_name='university.filiere')

    def name_get(self):
        resultat = []
        for etudiant in self:
            name = '[' + etudiant.filiere_id.filiere + '] '+ etudiant.l_name +' '+etudiant.f_name
            resultat.append((etudiant.id,name))
        return resultat
#
