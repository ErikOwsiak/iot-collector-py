
import gpiozero
import datetime as dt


class pinTickCounter:

   def __init__(self, hport, lbl, board_lbl):
      self.utc_dtc = dt.datetime.utcnow()
      self.total_ticks = 0
      self.rpt_ticks = 0
      self.last_tick = None
      self.hport = hport
      self.lbl = lbl
      self.board_lbl = board_lbl
      # use button to get incoming pulses
      self.button = gpiozero.Button(pin=hport, pull_up=False)
      self.button.held_time = 0.020
      self.button.when_held = pinTickCounter.on_held

   def start(self):
      pass

   @staticmethod
   def on_held(btn):
      print(btn)

   def clear_rpt(self):
      self.rpt_ticks = 0

   def clear_all(self):
      self.rpt_ticks = 0
      self.total_ticks = 0

   def get_rpt(self, frm=None):
      if frm is None:
         rpt = f"\"{self.board_lbl}\":{self.rpt_ticks}"
      else:
         rpt = frm % (self.board_lbl, self.rpt_ticks)
      self.clear_rpt()
      return rpt
