# -*- coding: utf-8 -*-

from odoo import models,fields, api
import datetime

class StaffAttendance(models.Model):
   _name = 'hotel_management.staff_attendance'
   _description = 'StaffAttendance'

# Fields ================================================================================================================================================

# Fields of "Staff Attendance" table
    # staff_id=fields.Many2one('hotel_management.staff',string='Staff id')
   name = fields.Many2one('hotel_management.staff', string='Staff')
   staff_staff_job_title=fields.Selection(string='staff_staff_job_title', selection=[('Manager', 'Manager'),
                                                                         ('Receptionist', 'Receptionist'),
                                                                         ('Housekeeper', 'Housekeeper'),
                                                                         ('Cheif', 'Cheif'),
                                                                         ('Driver', 'Driver'),
                                                                         ('Other', 'Other')])
   staff_attendance_date=fields.Date(string='staff_attendance_date')
   staff_attendance_in_time = fields.Char(string='staff_attendance_in_time')
   staff_attendance_total_hours_worked=fields.Char(string='staff_attendance_total_hours_worked')
   staff_attendance_out_time = fields.Char(string='staff_attendance_out_time', compute='_compute_current_out_time')


# Functions ==================================================================================================================================================

   def _compute_current_out_time(self):
       staff_attendance_in_time = fields.Datetime.now()
       self.staff_attendance_in_time = staff_attendance_in_time.strftime("%H:%M:%S")

   def _compute_current_out_time(self):
       staff_attendance_out_time = fields.Datetime.now()
       self.staff_attendance_out_time = staff_attendance_out_time.strftime("%H:%M:%S")


