# -*- coding: utf-8 -*-

from odoo import models,fields, api

class Staff(models.Model):
  _name = 'hotel_management.staff'
  _description = 'Staff'

#   staff_id=fields.Integer(string="staff_id")

  

  # Fields ================================================================================================================================================

# Fields of "Staff" table


  name = fields.Char(string="Name  ", required=True)
  work_mobile = fields.Char(string='work mobile ', required=True)
  work_phone = fields.Char(string="work phone ")
  work_email= fields.Char(string='Work Email  ')
  gender=fields.Selection(string='Gender',selection=[('male','Male'),
                                                     ('female','Female'),
                                                     ('other','Other')],
                                                     default = 'male')
  # hotel_name=fields.One2many('hotel_management.location','h_name',string='Hotel Location')
  department = fields.Selection(string='Staff Type', selection=[('management', 'Management'),
                                                                ('reception', 'Reception'),
                                                                ('housekeeper', 'Housekeeper'),
                                                                ('cooking', 'Cooking'),
                                                                ('driver', 'Driver'),
                                                                ('housekeeper', 'Housekeeper'),
                                                                ('other', 'Other')],
                                                                required=True)
  job_title= fields.Selection(string='Job title', selection=[('Manager', 'Manager'),
                                                                    ('Receptionist', 'Receptionist'),
                                                                    ('Housekeeper', 'Housekeeper'),
                                                                    ('Cheif', 'Cheif'),
                                                                    ('Driver', 'Driver'),
                                                                    ('Other', 'Other')])
  date_of_birth=fields.Datetime(string='Date_Of_Birth')
  marital_status=fields.Selection(string='Marital Status',selection=[('Single','Single'),
                                                                     ('Married','Married'),
                                                                     ('Legal cohabitant','Legal cohabitant'),
                                                                     ('Divorced','Divorced')])

  working_schedule=fields.Selection(string='Working Schedule',selection=[('Standard 40 hours/Week','Standard 40 hours/Week'),
                                                                         ('Standard 38 hours/Week','Standard 38 hours/Week'),
                                                                         ('Standard 35 hours/Week','Standard 35 hours/Week')])
  nationality=fields.Selection(string='Nationality',selection=[('India','India'),
                                                               ('Pakistan','Pakistan'),
                                                               ('America','America'),
                                                               ('Afganisthan','Afganisthan'),
                                                               ('Turki','Turki')])
  address = fields.Text(string='Current Address : ')
  salary=fields.Float(string='salary')


# Functions ==================================================================================================================================================

  def action_open(self):
       print("----------StaffAttendance---------")
       return {
           'type': 'ir.actions.act_window',
           'name': 'StaffAttendance',
           'res_model': 'hotel_management.staff_attendance',
           # 'domain': [('staff_id', '=', self.id)],
           'view_mode': 'tree,form',
           'target': 'current',
       }

  def action_cl(self):
      print("----------Contract---------")
      return {
          'type': 'ir.actions.act_window',
          'name': 'Contract',
          'res_model': 'hotel_management.contract',
          # 'domain': [('staff_id', '=', self.id)],
          'view_mode': 'tree,form',
          'target': 'current',
       }