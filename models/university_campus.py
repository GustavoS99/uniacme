from odoo import models, fields

class UniversityCampus(models.Model):
    _name = 'university.campus'
    _description = 'Campus de la universidad'

    name = fields.Char(string="Nombre de la sede", required=True)
    location = fields.Selection([
        ('+01:00', 'Bélgica'),
        ('-05:00', 'Colombia'),
        ('-04:00', 'Venezuela'),
        ('-03:00', 'Argentina')
    ], string="Zona horaria", required=True)

    student_ids = fields.One2many('res.partner', 'campus_id', string="Estudiantes")

    _sql_constraints = [
        ('uniq_name', 'unique(name)', "Ya existe una sede con ese nombre"),
    ]