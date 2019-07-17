#-*- coding: utf-8 -*-
from odoo import _, models, fields, api

class AsientoCabecera(models.Model):
	_name = "asiento.cabecera"

	name = fields.Char("Número de asiento", required = True)
	sub_diario_id = fields.Many2one("sub.diario", string = "Sub Diaio")
	anyo = fields.Char("Año")
	mes = fields.Char("Mes")
	fecha = fields.Date("Fecha")
	glosa = fields.Char("Glosa")
	asiento_detalle_ids = fields.One2many("asiento.detalle", "asiento_cabecera_id", string = "Detalle del asiento")
	debe = fields.Float("Debe", compute = "_compute_totales", store = True)
	haber = fields.Float("Haber", compute = "_compute_totales", store = True)

	company_id = fields.Many2one('res.company', 'Company', required=True, index=True, default=lambda self: self.env.user.company_id.id)

	@api.depends("asiento_detalle_ids.debe", "asiento_detalle_ids.haber")
	def _compute_totales(self):
		tot_debe = 0.00
		tot_haber = 0.00

		for item in self.asiento_detalle_ids:
			tot_debe += item.debe
			tot_haber += item.haber

		self.debe = tot_debe
		self.haber = tot_haber

class AsientoDetalle(models.Model):
	_name = "asiento.detalle"

	name = fields.Char("Glosa", required = True)
	asiento_cabecera_id = fields.Many2one("asiento.cabecera", ondelete = "cascade")
	orden = fields.Integer("Orden")
	plan_contable_id = fields.Many2one("plan.contable", string = "Cuenta contable", required = True)
	debe = fields.Float("Debe")
	haber = fields.Float("Haber")
