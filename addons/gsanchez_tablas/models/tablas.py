#-*- coding: utf-8 -*-
from odoo import _, models, fields, api

class ClaseBaseAbr(models.Model):
	_name = "clase.base"

	def correlativo(self):
		newCor = self.search([], order = "name desc", limit = 1)
		for cor in newCor:
			return str(int(cor["name"]) + 1).zfill(2)

	name = fields.Char("Código", required = True, default = correlativo)
	descripcion = fields.Char("Descripción", required = True)
	abreviatura = fields.Char("Abreviatura")

	company_id = fields.Many2one('res.company', 'Company', required=True, index=True, default=lambda self: self.env.user.company_id.id)

	@api.onchange('name', 'descripcion', 'abreviatura')
	def upper_descripcion(self):
		if self.name:
			self.name = self.name.upper()

		if self.descripcion:
			self.descripcion = self.descripcion.upper()

		if self.abreviatura:
			self.abreviatura = self.abreviatura.upper()

class TipoDocumento(ClaseBaseAbr):
	_name = "tipo.documento"

class TipoDocumentoIdentidad(ClaseBaseAbr):
	_name = "tipo.documento.identidad"

class FormaPago(ClaseBaseAbr):
	_name = "forma.pago"

class CondicionPago(models.Model):
	_name = "condicion.pago"

	def correlativo(self):
		newCor = self.env["condicion.pago"].search([], order = "name desc", limit = 1)
		for cor in newCor:
			return str(int(cor["name"]) + 1).zfill(2)

	name = fields.Char("Código", required = True, default = correlativo)
	descripcion = fields.Char("Descripción", required = True)
	dias = fields.Integer("Número de días")

	company_id = fields.Many2one('res.company', 'Company', required=True, index=True, default=lambda self: self.env.user.company_id.id)

	@api.onchange('name', 'descripcion')
	def upper_descripcion(self):
		if self.name:
			self.name = self.name.upper()
		
		if self.descripcion:
			self.descripcion = self.descripcion.upper()

class SubDiario(models.Model):
	_name = "sub.diario"

	def correlativo(self):
		newCor = self.env["sub.diario"].search([], order = "name desc", limit = 1)
		for cor in newCor:
			return str(int(cor["name"]) + 1).zfill(2)

	name = fields.Char("Código", required = True, default = correlativo)
	descripcion = fields.Char("Descripción", required = True)

	company_id = fields.Many2one('res.company', 'Company', required=True, index=True, default=lambda self: self.env.user.company_id.id)

	@api.onchange('name', 'descripcion')
	def upper_descripcion(self):
		if self.name:
			self.name = self.name.upper()
		
		if self.descripcion:
			self.descripcion = self.descripcion.upper()

class PlanContable(models.Model):
	_name = "plan.contable"

	name = fields.Char("Cuenta", required = True)
	descripcion = fields.Char("Descripción", required = True)
	codsunat = fields.Char("Código SUNAT")
	nivel = fields.Selection([("P", "Principal"), ("S", "Sub cuenta"), ("R", "Registro")])
	tipo = fields.Selection([("ORD", "Orden"), ("ACT", "Activo"), ("PAS", "Pasivo y patrimonio"), 
								("NAT", "Naturaleza"), ("FUN", "Función"), ("RES", "Resultado"), ("MAY", "Mayor")])
	analisis = fields.Selection([("SIN", "Sin análisis"), ("BCO", "Cuentas de banco"), 
									("DOC", "Análisis por documentos"), ("SDT", "Solo detalle")], string = "Análisis", default = "SIN")

	company_id = fields.Many2one('res.company', 'Company', required=True, index=True, default=lambda self: self.env.user.company_id.id)


	@api.onchange('name', 'descripcion')
	def upper_descripcion(self):
		if self.name:
			self.name = self.name.upper()
		
		if self.descripcion:
			self.descripcion = self.descripcion.upper()

class CajaBanco(models.Model):
	_name = "caja.banco"

	def correlativo(self):
		newCor = self.env["caja.banco"].search([], order = "name desc", limit = 1)

		cCor = "01"
		for cor in newCor:
			cCor = str(int(cor["name"]) + 1).zfill(2)

		return cCor

	name = fields.Char("Código", required = True, default = correlativo)
	descripcion = fields.Char("Descripción", required = True)
	caja_banco_cuenta_ids = fields.One2many("caja.banco.cuenta", "caja_banco_id", string = "Cuentas")

	company_id = fields.Many2one('res.company', 'Company', required=True, index=True, default=lambda self: self.env.user.company_id.id)

	@api.onchange('name', 'descripcion')
	def upper_descripcion(self):
		if self.name:
			self.name = self.name.upper()
		
		if self.descripcion:
			self.descripcion = self.descripcion.upper()

class CajaBancoCuenta(models.Model):
	_name = "caja.banco.cuenta"

	caja_banco_id = fields.Many2one("caja.banco", ondelete = "cascade")
	name = fields.Char("Descripción", required = True)
	cuenta = fields.Char("Nro de cuenta")
	cci = fields.Char("CCI")
	plan_contable_id = fields.Many2one("plan.contable", string = "Cuenta contable asociada")


	@api.onchange('name')
	def upper_descripcion(self):
		if self.name:
			self.name = self.name.upper()

