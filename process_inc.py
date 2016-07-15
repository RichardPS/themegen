class SiteInfo(object):
	def __init__(self, nursery):
		self.specialpages = {
		    'kidparent': 'Children',
		    'kidname': 'Kids\' Zone',
		    'newsparent': 'News and Events',
		    'newsname': 'Latest News',
		    'letterparent': 'News and Events',
		    'lettername': 'Newsletters',
		    'calendarparent': 'News and Events',
		    'calendarname': 'Calendar',
		    'tourparent': 'About Us',
		    'tourname': 'School Tour',
		}

		self.sitemaparray = []
		self.topicslugs = []
		self.topicnames = []
		self.pagescript = []
		self.themeslug = 'BuildTemplate'
		self.nursery = nursery
		self.currenttopic = ''

	def set_kp(self, parent):
		self.specialpages['kidparent'] = parent

	def set_kn(self, name):
		self.specialpages['kidname'] = name

	def set_np(self, parent):
		self.specialpages['newsparent'] = parent

	def set_nn(self, name):
		self.specialpages['newsname'] = name

	def set_lp(self, parent):
		self.specialpages['letterparent'] = parent

	def set_ln(self, name):
		self.specialpages['lettername'] = name

	def set_cp(self, parent):
		self.specialpages['calendarparent'] = parent

	def set_cn(self, name):
		self.specialpages['calendarname'] = name

	def set_tp(self, parent):
		self.specialpages['tourparent'] = parent

	def set_tn(self, name):
		self.specialpages['tourname'] = name

	def set_themeslug(self, themename):
		self.themeslug = themename

	def set_nursery(self, nursery):
		self.nursery = nursery

	def set_currenttopic(self, current):
		self.currenttopic = current

	def set_sitemaparray(self, sitemap):
		self.sitemaparray = sitemap

	def ext_topicnames(self, topicname):
		self.topicnames.extend([topicname])

	def ext_topicslugs(self, topicslug):
		self.topicslugs.extend([topicslug])

	def ext_pagescript(self, pageline):
		self.pagescript.extend([pageline])