# -*- coding: utf-8 -*-

from odoo import models,fields, api

class Contract(models.Model):
  _name = 'hotel_management.contract'
  _description = 'Contract'

# Fields ================================================================================================================================================

# Fields of "Contract" table
  name=fields.Many2one('hotel_management.staff',string='Staff')
  department=fields.Selection(string='Staff Type', selection=[('management','Management'),
                                                              ('reception','Reception'),
                                                              ('housekeeper','Housekeeper'),
                                                              ('cooking','Cooking'),
                                                              ('driver','Driver'),
                                                              ('housekeeper','Housekeeper'),
                                                              ('other','Other')])
  job_position=fields.Selection(string='Job Position',selection=[('management','Manager'),
                                                                 ('reception','Receptionist'),
                                                                 ('housekeeper','Housekeeper'),
                                                                 ('cooking','Cheif'),
                                                                 ('driver','Driver'),
                                                                 ('other','Other')])
  hotel=fields.Char(string='Hotel')
  salary_structure_type=fields.Selection(string='Salary Structure Type',selection=[('manager','Manager'),
                                                                                   ('receptioninst','Receptionist'),
                                                                                   ('cheif','Cheif'),
                                                                                   ('other staff','Other Staff')])
  contract_duraction=fields.Selection(string='Contract Duraction',selection=[('6 months','6 Months'),
                                                                             ('1 year','1 year'),
                                                                             ('2 year','2 year')],
                                                                             default='6 months')
  start_date=fields.Date(string='Start Date')
  end_date=fields.Date(string='End Date')
  working_schedule = fields.Selection(string='Working Schedule', selection=[('Standard 40 hours/Week', 'Standard 40 hours/Week'),
                                                                            ('Standard 38 hours/Week', 'Standard 38 hours/Week'),
                                                                            ('Standard 35 hours/Week', 'Standard 35 hours/Week')],
                                                                             default='Standard 40 hours/Week')
  contract_details = fields.Text(string='Contract Details')


# Functions ==================================================================================================================================================

  def action_open(self):
       print("----------test---------")
       return {
           'type': 'ir.actions.act_window',
           'name': 'Contract',
           'res_model': 'hotel_management.staff',
           # 'domain': [('staff_id', '=', self.id)],
           'view_mode': 'tree,form',
           'target': 'current',
       }