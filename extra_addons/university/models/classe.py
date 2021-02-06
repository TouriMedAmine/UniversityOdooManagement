from odoo import models, fields, api
#

class UniversityClasse(models.Model):
    _name = 'university.classe'
    _rec_name = 'classe'

    classe = fields.Char()
    code = fields.Char('code')

    filiere_id = fields.Many2one(comodel_name='university.filiere')
    professeur_id = fields.Many2one(comodel_name='university.professeur')
    etudiant_ids = fields.Many2many(comodel_name='university.etudiant',
                                  relation='classe_etudiant_rel',
                                  column1='classe',
                                  column2='cin')
    num_etudiant = fields.Integer(string='Nombre des etudiants', compute='comp_etud')

    def comp_etud(self):
        self.num_etudiant = len(self.etudiant_ids)
