from eaty_app.settings.base import *

#Override base.py settings here


try:
  from eaty_app.settings.local import *
except:
  pass