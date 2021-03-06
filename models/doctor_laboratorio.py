# -*- coding: utf-8 -*-
##############################################################################
#
#	OpenERP, Open Source Management Solution
#	Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#	This program is free software: you can redistribute it and/or modify
#	it under the terms of the GNU Affero General Public License as
#	published by the Free Software Foundation, either version 3 of the
#	License, or (at your option) any later version.
#
#	This program is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	GNU Affero General Public License for more details.
#
#	You should have received a copy of the GNU Affero General Public License
#	along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
import logging
_logger = logging.getLogger(__name__)
from openerp.osv import fields, osv
from openerp.tools.translate import _
import time
from datetime import date, datetime, timedelta
from lxml import etree


class doctor_laboratorio(osv.osv):


	_name = "doctor.laboratorio"

	_columns = {
		'name' : fields.char('Nombre', required=True, size=60),
		'active': fields.boolean('activo'),
		'fuente': fields.char('Fuente'),
	}


doctor_laboratorio()



class doctor_attention_laboratorio(osv.osv):

	_name = "doctor.attention.laboratorio"

	_columns = {
		'attentiont_id': fields.many2one('doctor.attentions', 'Attention'),
		'laboratorio_id': fields.many2one('doctor.laboratorio', 'Laboratorio', required=True,
										   ondelete='restrict'),
		'fecha': fields.date('Fecha',),
		'resultado': fields.char('Resultado',),

	}

doctor_attention_laboratorio()