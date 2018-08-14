# -*- coding: utf-8 -*-


import odoo
from odoo import http
from odoo.http import request

class claricoHomePage1(http.Controller):
    @http.route(['/page/homepage'], type='http', auth="public", website=True)
    def service(self, **kwargs):
        return request.render("artarad_noortec_website.noortec_homepage")