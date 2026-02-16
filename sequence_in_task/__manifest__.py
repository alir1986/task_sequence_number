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
{
    'name': "Task Sequence Number",
    'version': '17.0.0.1',
    'summary': "Automatically assigns and displays a sequence number for tasks",
    'description': """
        Task Sequence Number enhances Odoo's project tasks by assigning
        an automatic sequence number to each task. The sequence is
        displayed in the task list view for quick identification.
        
        Key Features:
        📌 Automatic numbering of tasks
        📌 Sequence visible in the task tree view
        📌 Lightweight and easy to install
        📌 Fully integrated with Odoo's project workflow
    """,
    'category': 'Project',
    'author': "Alireza (AR)",
    'maintainer': "Alireza",
    'support': "alir.riazi@gmail.com",
    'license': 'LGPL-3',
    'depends': ['project'],
    'data': [
        'data/sequence.xml',
        'views/project_view.xml',
    ],
    'images': ['static/description/banner.png'],
        'assets': {
    'web.assets_backend': [
        'static/description/index.html',
       ],
     },
    'installable': True,
    'application': False,
    'auto_install': False,
}