from odoo import models, fields

class Student(models.Model):
    _inherit = 'res.partner'
    _description = 'Estudiantes'

    is_student = fields.Boolean(string="Es estudiante", default=False)
    identification = fields.Char(string="Id de estudiante")
    program = fields.Char(string="Carrera")

    campus_id = fields.Many2one('university.campus', string="Sede")

    _sql_constraints = [
        ('uniq_identification', 'unique(identification)', "Ya esta registrado un estudiante con esa identificación."),
    ]

