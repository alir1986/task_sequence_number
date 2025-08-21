# -*- coding: utf-8 -*-
################################################################################
#
#    Task Sequence Number
#
#    Copyright (C) 2025 Alireza (AR)
#    Author: Alireza (alir.riazi@gmail.com)
#
#    You can modify it under the terms of the GNU AFFERO
#    GENERAL PUBLIC LICENSE (AGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU AFFERO GENERAL PUBLIC LICENSE (AGPL v3) for more details.
#
#    You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
#    (AGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
################################################################################
from odoo import api, fields, models, _

class ProjectTaskType(models.Model):    
    _inherit = "project.task" 

    task_num = fields.Char(string="Task Number" ,help="Task Sequence Number", default=lambda self: _('New'), readonly=True, index=True)
    
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['task_num'] = self.env['ir.sequence'].next_by_code('project.task')
        
        return super(ProjectTaskType, self).create(vals_list)
    