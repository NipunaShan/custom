import randomimport stringfrom odoo import api, fields, models, _, toolsclass SaleAgent(models.Model):    _name = "sale.agent"    _rec_name = "full_name"    _description = "Sale Agent Details"    email = fields.Char(string="Email")    password = fields.Char(string="Password")    full_name = fields.Char(string="Full Name")    nic = fields.Char(string="NIC")    mobile = fields.Char(string="Mobile NO")    agent_id = fields.Char(string="Agent ID")    secret_key = fields.Char(string="Secret Key")    sale_agent_categories_id = fields.Many2one(comodel_name="sale.agent.categories", string="Agent Category", required=True)    def generate_sequence(self):        length = 6        characters = string.ascii_letters + string.digits        sequence = ''.join(random.choice(characters) for i in range(length))        return sequence    @api.model    def create(self, vals):        if not vals.get('secret_key'):            vals['secret_key'] = self.generate_sequence()        return super(SaleAgent, self).create(vals)    def name_get(self):        res = []        for sale_agent in self:            res.append((sale_agent.id, '%s (%s)' % (sale_agent.full_name, sale_agent.emp_id)))        return res