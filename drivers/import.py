import pages.home_page as pg
import sys
import os
base_dir = os.path.dirname(__file__) or '.'
sys.path.append("..")

home=pg.HomePage("lmao")