from odoo import models, fields, api

class Candidate(models.Model):
    _inherit = "res.partner"

    identification = fields.Char(string = "Nro de identificación")
    is_candidate = fields.Boolean(string = "Es Candidato")
    campus_id = fields.Many2one("university.campus", "Sede")

    _sql_constraints = {
        ("uniq_candidate_id", "unique(identification)", "Ya esta registrado un candidato con esa identificación")
    }

    @api.model
    def action_create_candidate(self, vals):
        message = "El candidato ha sido guardado correctamente."
        self.env['bus.bus']._sendone(self.env.user.partner_id, 'simple_notification', {
            'type': 'success',
            'title': ("En hora buena!"),
            'message': (message)
        })