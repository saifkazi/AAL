from trytond.model import ModelSQL, ModelView,fields ,Workflow
from trytond.pool import Pool, PoolMeta
from trytond.pyson import  Eval
from trytond.exceptions import UserError, UserWarning

class WorkType( metaclass=PoolMeta):

    __name__ = 'production.work'
    treatment_freeparameter = fields.One2Many('treatment.freeparameter',
        'free_parameter', 'Steps' ,
        states={
            'invisible': ~Eval('treatment_boolean', True),
            },
        depends=['treatment_boolean']
        )
    quantitytaken = fields.Char("Quantity taken for treatment" , 
        states={
            'invisible': ~Eval('treatment_boolean', True),
            },
        depends=['treatment_boolean']
        )
    equipment_no =fields.Char("Equipmet No" ,
        states={
            'invisible': ~Eval('treatment_boolean', True),
            },
        depends=['treatment_boolean']
        )
    initial_ph = fields.Char("Initial pH" ,
        states={
            'invisible': ~Eval('treatment_boolean', True),
            },
        depends=['treatment_boolean']
        )
    initial_moisture = fields.Char("Initial Moisture" ,
        states={
            'invisible': ~Eval('treatment_boolean', True),
            },
        depends=['treatment_boolean']
        )
    final_ph = fields.Char("Final pH" , 
        states={
            'invisible': ~Eval('treatment_boolean', True),
            },
        depends=['treatment_boolean']
        )
    final_moisture = fields.Char("Final Moisture" , 
        states={
            'invisible': ~Eval('treatment_boolean', True),
            },
        depends=['treatment_boolean']
        )
    treatment_boolean = fields.Boolean('Treatment')
    fd_boolean = fields.Boolean('Final Distillation')
    ed_boolean = fields.Boolean('Extractive Distillation')
    ww_boolean = fields.Boolean('Water Washing')
    striping = fields.Boolean('Striping')

   
    # treatment material balance

    # materialbalance = fields.One2Many('treatment.materialbalance',
    #     'material_balance', "Material Balance",
    #     states={
    #         'invisible': ~Eval('treatment_boolean', True),
    #         },
    #     depends=['treatment_boolean']
    #     )

    treatment_input_qty = fields.Integer("Input qty",states={
            'invisible': ~Eval('treatment_boolean', True),
            },depends=['treatment_boolean'])
    treatment_output_qty = fields.Numeric("Output qty",states={
            'invisible': ~Eval('treatment_boolean', True),
            },depends=['treatment_boolean'])
    treatment_loss = fields.Numeric("Loss",states={
            'invisible': ~Eval('treatment_boolean', True),
            },depends=['treatment_boolean'])
    treatment_lye_collected = fields.Numeric("Lye collected",states={
            'invisible': ~Eval('treatment_boolean', True),
            },depends=['treatment_boolean'])

    treatment_input_qty_percent = fields.Float("Input qty",states={
            'invisible': ~Eval('treatment_boolean', True)
            },depends=['treatment_boolean'])

    treatment_output_qty_percent = fields.Function(fields.Float("Output qty",states={
            'invisible': ~Eval('treatment_boolean', True),
            },depends=['treatment_boolean']),'on_change_with_treatment_output_qty_percent') 

    treatment_loss_percent = fields.Function(fields.Float("Loss",states={
            'invisible': ~Eval('treatment_boolean', True),
            },depends=['treatment_boolean']),'on_change_with_treatment_loss_percent')
            
    treatment_lye_collected_percent = fields.Function(fields.Float("Loss",states={
            'invisible': ~Eval('treatment_boolean', True),
            },depends=['treatment_boolean']),'on_change_with_treatment_lye_collected_percent')


    qty_sulphuric = fields.Char("Quantity of Sulfuric acid used for ph adjustment" ,
        states={
            'invisible': ~Eval('treatment_boolean', True),
            },
        depends=['treatment_boolean']
        )
    qty_bht = fields.Char("Quantity of B.H.T added as stabilizer",
        states={
            'invisible': ~Eval('treatment_boolean', True),
            },
        depends=['treatment_boolean']
        )
    distillation_input = fields.One2Many('finaldistillation.input',
        'input_details', "Input Details",
        states={
            'invisible': ~Eval('fd_boolean', True),
            },
        depends=['fd_boolean']
        )
    
    first = fields.Boolean("Ensure that instrument is cleaned properly",
        states={
            'invisible': ~Eval('fd_boolean', True),
            },
        depends=['fd_boolean']
        )
    second = fields.Boolean("Ensure cooling water circulation & appropriate level of water",
        states={
            'invisible': ~Eval('fd_boolean', True),
            },
        depends=['fd_boolean']
        )

    third = fields.Boolean("Ensure that house pipe is cleaned",
        states={
            'invisible': ~Eval('fd_boolean', True),
            },
        depends=['fd_boolean']
        )

    fourth = fields.Boolean("Ensure that drums for fraction , main & for residue are available",
        states={
            'invisible': ~Eval('fd_boolean', True),
            },
        depends=['fd_boolean']
        )

    fifth = fields.Boolean("Ensure that earthing connections are proper",
        states={
            'invisible': ~Eval('fd_boolean', True),
            },
        depends=['fd_boolean']
        )
    analysis = fields.One2Many('finaldistillation.analysis',
        'analysis_record', "Temperature & analysis Record",
        states={
            'invisible': ~Eval('fd_boolean', True),
            },
        depends=['fd_boolean']
        )

    # Final Distilaltion material balance

    # mb = fields.One2Many('final.materialbalance',
    #     'balance_table', "Material Balance Summary",
    #     states={
    #         'invisible': ~Eval('fd_boolean', True),
    #         },
    #     depends=['fd_boolean']
    #     )
    # balance_table = fields.Many2One('production.work','Material Balance Summary')
    fd_mb_inputqty = fields.Numeric("Input qty",states={'invisible': ~Eval('fd_boolean', True)},depends=['fd_boolean'])
    fd_mb_water = fields.Numeric("Water",states={'invisible': ~Eval('fd_boolean', True)},depends=['fd_boolean'])
    fd_mb_f1 = fields.Numeric("F-1",states={'invisible': ~Eval('fd_boolean', True)},depends=['fd_boolean'])
    fd_mb_f2 = fields.Numeric("F-2",states={'invisible': ~Eval('fd_boolean', True)},depends=['fd_boolean'])
    fd_mb_main = fields.Numeric("Main",states={'invisible': ~Eval('fd_boolean', True)},depends=['fd_boolean'])
    fd_mb_aftermain = fields.Numeric("After Main",states={'invisible': ~Eval('fd_boolean', True)},depends=['fd_boolean'])
    fd_mb_residue = fields.Numeric("Residue",states={'invisible': ~Eval('fd_boolean', True)},depends=['fd_boolean'])
    fd_mb_loss = fields.Numeric("Loss",states={'invisible': ~Eval('fd_boolean', True)},depends=['fd_boolean'])

    fd_mb_inputqty_percent =fields.Function(fields.Float("Input qty",states={
            'invisible': ~Eval('fd_boolean', True),
            },depends=['fd_boolean']),'on_change_with_fd_mb_inputqty_percent')
    
    fd_mb_water_percent =fields.Function(fields.Float("Water",states={
            'invisible': ~Eval('fd_boolean', True),
            },depends=['fd_boolean']),'on_change_with_fd_mb_water_percent')
    
    fd_mb_f1_percent = fields.Function(fields.Float("F-1",states={
            'invisible': ~Eval('fd_boolean', True),
            },depends=['fd_boolean']),'on_change_with_fd_mb_f1_percent')

    fd_mb_f2_percent = fields.Function(fields.Float("F-2",states={
            'invisible': ~Eval('fd_boolean', True),
            },depends=['fd_boolean']),'on_change_with_fd_mb_f2_percent')
    
    fd_mb_main_percent = fields.Function(fields.Float("Main",states={
            'invisible': ~Eval('fd_boolean', True),
            },depends=['fd_boolean']),'on_change_with_fd_mb_main_percent')
    
    fd_mb_aftermain_percent = fields.Function(fields.Float("AfterMain",states={
            'invisible': ~Eval('fd_boolean', True),
            },depends=['fd_boolean']),'on_change_with_fd_mb_aftermain_percent')
    
    fd_mb_residue_percent  = fields.Function(fields.Float("Residue",states={
            'invisible': ~Eval('fd_boolean', True),
            },depends=['fd_boolean']),'on_change_with_fd_mb_residue_percent') 
    
    fd_mb_loss_percent = fields.Function(fields.Float("Loss",states={
            'invisible': ~Eval('fd_boolean', True),
            },depends=['fd_boolean']),'on_change_with_fd_mb_loss_percent') 




    # ed_mb = fields.One2Many('ed.materialbalance' , 'ed_balance' , "Material Balance Summary" , 
    #     states={
    #         'invisible': ~Eval('ed_boolean', True),
    #         },
    #     depends=['ed_boolean']
    #     )



    ed_mb_inputqty = fields.Numeric("Input qty",states={'invisible': ~Eval('ed_boolean', True)},depends=['ed_boolean'])
    ed_mb_f1_mix = fields.Numeric("F-1 mix",states={'invisible': ~Eval('ed_boolean', True)},depends=['ed_boolean'])
    ed_mb_recyclable_f1 = fields.Numeric("Recyclable f-1",states={'invisible': ~Eval('ed_boolean', True)},depends=['ed_boolean'])
    ed_mb_strippingmain = fields.Numeric("Stripping main",states={'invisible': ~Eval('ed_boolean', True)},depends=['ed_boolean'])
    ed_mb_aftermain = fields.Numeric("After main",states={'invisible': ~Eval('ed_boolean', True)},depends=['ed_boolean'])
    ed_mb_bottom = fields.Numeric("Bottom",states={'invisible': ~Eval('ed_boolean', True)},depends=['ed_boolean'])
    ed_mb_dist_loss = fields.Numeric("dist.loss",states={'invisible': ~Eval('ed_boolean', True)},depends=['ed_boolean'])


    ed_mb_inputqty_percent =fields.Function(fields.Float("Input qty",states={
            'invisible': ~Eval('ed_boolean', True),
            },depends=['ed_boolean']),'on_change_with_ed_mb_inputqty_percent')
    ed_mb_f1_mix_percent =fields.Function(fields.Float("F-1 mix",states={
            'invisible': ~Eval('ed_boolean', True),
            },depends=['ed_boolean']),'on_change_with_ed_mb_f1_mix_percent')
    ed_mb_recyclable_f1_percent =fields.Function(fields.Float("Recyclable f-1",states={
            'invisible': ~Eval('ed_boolean', True),
            },depends=['ed_boolean']),'on_change_with_ed_mb_recyclable_f1_percent')
    ed_mb_aftermain_percent =fields.Function(fields.Float("After main",states={
            'invisible': ~Eval('ed_boolean', True),
            },depends=['ed_boolean']),'on_change_with_ed_mb_aftermain_percent')
    ed_mb_bottom_percent =fields.Function(fields.Float("Bottom",states={
            'invisible': ~Eval('ed_boolean', True),
            },depends=['ed_boolean']),'on_change_with_ed_mb_bottom_percent')
    ed_mb_dist_loss_percent =fields.Function(fields.Float("dist.loss",states={
            'invisible': ~Eval('ed_boolean', True),
            },depends=['ed_boolean']),'on_change_with_ed_mb_dist_loss_percent')
    ed_mb_strippingmain_percent =fields.Function(fields.Float("Stripping main",states={
            'invisible': ~Eval('ed_boolean', True),
            },depends=['ed_boolean']),'on_change_with_ed_mb_strippingmain_percent')



    #Water washing    
    # ww_mb = fields.One2Many('ww.materialbalance' , 'ww_balance' , "Material Balance Summary" , 
    #     states={
    #         'invisible': ~Eval('ww_boolean', True),
    #         },
    #     depends=['ww_boolean']
    #     )
    


    ww_mb_inputqty = fields.Numeric("Input qty",states={'invisible': ~Eval('ww_boolean', True)},depends=['ww_boolean'])
    ww_mb_output = fields.Numeric("Output",states={'invisible': ~Eval('ww_boolean', True)},depends=['ww_boolean'])
    ww_mb_loss = fields.Numeric("Loss",states={'invisible': ~Eval('ww_boolean', True)},depends=['ww_boolean'])
    ww_mb_consumption = fields.Numeric("Consumption of water",states={'invisible': ~Eval('ww_boolean', True)},depends=['ww_boolean'])


    ww_mb_inputqty_percent =fields.Function(fields.Float("Input qty",states={
            'invisible': ~Eval('ww_boolean', True),
            },depends=['ww_boolean']),'on_change_with_ww_mb_inputqty_percent')

    ww_mb_output_percent =fields.Function(fields.Float("Output",states={
            'invisible': ~Eval('ww_boolean', True),
            },depends=['ww_boolean']),'on_change_with_ww_mb_output_percent')

    ww_mb_loss_percent =fields.Function(fields.Float("Loss",states={
            'invisible': ~Eval('ww_boolean', True),
            },depends=['ww_boolean']),'on_change_with_ww_mb_loss_percent')

    ww_mb_consumption_percent =fields.Function(fields.Float("Consumption of water",states={
            'invisible': ~Eval('ww_boolean', True),
            },depends=['ww_boolean']),'on_change_with_ww_mb_consumption_percent')



    # stripping = fields.One2Many('striping.materialbalance' , 'striping_balance' , "Material Balance Summary" , 
    #     states={
    #         'invisible': ~Eval('striping', True),
    #         },
    #     depends=['striping']
    #     )
    st_mb_inputqty = fields.Numeric("Input qty",states={'invisible': ~Eval('striping', True)},depends=['striping'])
    st_mb_f1_mix = fields.Numeric("F-1 mix",states={'invisible': ~Eval('striping', True)},depends=['striping'])
    st_mb_recyclable_f1 = fields.Numeric("Recyclable f-1",states={'invisible': ~Eval('striping', True)},depends=['striping'])
    st_mb_strippingmain = fields.Numeric("Stripping main",states={'invisible': ~Eval('striping', True)},depends=['striping'])
    st_mb_aftermain = fields.Numeric("After main",states={'invisible': ~Eval('striping', True)},depends=['striping'])
    st_mb_bottom = fields.Numeric("Bottom",states={'invisible': ~Eval('striping', True)},depends=['striping'])
    st_mb_dist_loss = fields.Numeric("dist.loss",states={'invisible': ~Eval('striping', True)},depends=['striping'])


    st_mb_inputqty_percent =fields.Function(fields.Float("Input qty",states={
            'invisible': ~Eval('striping', True),
            },depends=['striping']),'on_change_with_st_mb_inputqty_percent')
    st_mb_f1_mix_percent =fields.Function(fields.Float("F-1 mix",states={
            'invisible': ~Eval('striping', True),
            },depends=['striping']),'on_change_with_st_mb_f1_mix_percent')
    st_mb_recyclable_f1_percent =fields.Function(fields.Float("Recyclable f-1",states={
            'invisible': ~Eval('striping', True),
            },depends=['striping']),'on_change_with_st_mb_recyclable_f1_percent')
    st_mb_aftermain_percent =fields.Function(fields.Float("After main",states={
            'invisible': ~Eval('striping', True),
            },depends=['striping']),'on_change_with_st_mb_aftermain_percent')
    st_mb_bottom_percent =fields.Function(fields.Float("Bottom",states={
            'invisible': ~Eval('striping', True),
            },depends=['striping']),'on_change_with_st_mb_bottom_percent')
    st_mb_dist_loss_percent =fields.Function(fields.Float("dist.loss",states={
            'invisible': ~Eval('striping', True),
            },depends=['striping']),'on_change_with_st_mb_dist_loss_percent')
    st_mb_strippingmain_percent =fields.Function(fields.Float("Stripping main",states={
            'invisible': ~Eval('striping', True),
            },depends=['striping']),'on_change_with_st_mb_strippingmain_percent')
   
    @classmethod
    def __setup__(cls):
        super(WorkType, cls).__setup__()
        cls._buttons.update({
            'validate_mb_treatment': {
                        'invisible': ~Eval('treatment_boolean', True),
                        'depends': ['treatment_boolean'],
                        },
            'validate_mb_fd': {
                        'invisible': ~Eval('fd_boolean', True),
                        'depends': ['fd_boolean'],
                        },
            'validate_mb_stripping': {
                        'invisible': ~Eval('striping', True),
                        'depends': ['striping'],
                        },
            'validate_mb_ww': {
                        'invisible': ~Eval('ww_boolean', True),
                        'depends': ['ww_boolean'],
                        },
            'validate_mb_ed': {
                        'invisible': ~Eval('ed_boolean', True),
                        'depends': ['ed_boolean'],
                        },
            })


    # mb treatment

    @staticmethod
    def default_treatment_input_qty():
        return 0
    @staticmethod
    def default_treatment_output_qty():
        return 0
    @staticmethod
    def default_treatment_loss():
        return 0
    @staticmethod
    def default_treatment_lye_collected():
        return 0
    
    # def get_treatment_input_qty_percent(self,name):
    #     return 100

    @fields.depends('treatment_input_qty') 
    def on_change_with_treatment_input_qty_percent(self, name=None):
        return 100
    

    @fields.depends('treatment_output_qty','treatment_input_qty') 
    def on_change_with_treatment_output_qty_percent(self, name=None):
        try:
            test = self.treatment_output_qty/self.treatment_input_qty
            percent = test*100 
            return percent
            
        except :
            return 0
    
    @fields.depends('treatment_loss','treatment_input_qty') 
    def on_change_with_treatment_loss_percent(self, name=None):
        try:
            treatment_loss = self.treatment_loss
            treatment_input_qty = self.treatment_input_qty
            test = treatment_loss/treatment_input_qty 
            percent = test*100 
            return percent
            
        except :
            return 0                

    @fields.depends('treatment_lye_collected','treatment_input_qty') 
    def on_change_with_treatment_lye_collected_percent(self, name=None):
        try:
            percent = (self.treatment_lye_collected/self.treatment_input_qty)*100 
            return percent
        except :
            return 0

    @ModelView.button_change('treatment_output_qty','treatment_input_qty', 'treatment_loss', 'treatment_lye_collected')
    def validate_mb_treatment(self):
        sums = self.treatment_output_qty + self.treatment_loss + self.treatment_lye_collected

        if self.treatment_input_qty == sums:
            
            raise UserError("Value Matched","All Value Matched")
        else :
            raise UserError("Failed","Value Does not Match")    
    
    #mb Final Distillation
    
    @staticmethod
    def default_fd_mb_inputqty():
        return 0
    
    @staticmethod
    def default_fd_mb_water():
        return 0
    
    @staticmethod
    def default_fd_mb_f1():
        return 0
    
    @staticmethod
    def default_fd_mb_f2():
        return 0
    
    @staticmethod
    def default_fd_mb_main():
        return 0
    
    @staticmethod
    def default_fd_mb_aftermain():
        return 0
    
    @staticmethod
    def default_fd_mb_residue():
        return 0
    
    @staticmethod
    def default_fd_mb_loss():
        return 0


    @fields.depends('fd_mb_inputqty') 
    def on_change_with_fd_mb_inputqty_percent(self, name=None):
        return 100
    
    @fields.depends('fd_mb_inputqty','fd_mb_water') 
    def on_change_with_fd_mb_water_percent(self, name=None):
        try:
            test = self.fd_mb_water/self.fd_mb_inputqty
            percent = test*100 
            return percent
        except :
            return 0

    @fields.depends('fd_mb_inputqty','fd_mb_f1') 
    def on_change_with_fd_mb_f1_percent(self,name=None):
        try:
            test = self.fd_mb_f1/self.fd_mb_inputqty
            percent = test*100 
            return percent
        except :
            return 0
    
    @fields.depends('fd_mb_inputqty','fd_mb_f2')
    def on_change_with_fd_mb_f2_percent(self,name=None):
        try:
            test = self.fd_mb_f2/self.fd_mb_inputqty
            percent = test*100 
            return percent
        except :
            return 0
    
    @fields.depends('fd_mb_inputqty','fd_mb_main')
    def on_change_with_fd_mb_main_percent(self,name=None):
        try:
            test = self.fd_mb_main/self.fd_mb_inputqty
            percent = test*100 
            return percent
        except :
            return 0
    
    @fields.depends('fd_mb_inputqty','fd_mb_aftermain')
    def on_change_with_fd_mb_aftermain_percent(self,name=None):
        try:
            test = self.fd_mb_aftermain/self.fd_mb_inputqty
            percent = test*100 
            return percent
        except :
            return 0
    
    @fields.depends('fd_mb_inputqty','fd_mb_residue')
    def on_change_with_fd_mb_residue_percent(self,name=None):
        try:
            test = self.fd_mb_residue/self.fd_mb_inputqty
            percent = test*100 
            return percent
        except :
            return 0
    
    @fields.depends('fd_mb_inputqty','fd_mb_loss')
    def on_change_with_fd_mb_loss_percent(self,name=None):
        try:
            test = self.fd_mb_loss/self.fd_mb_inputqty
            percent = test*100 
            return percent
        except :
            return 0
    
    @ModelView.button_change('fd_mb_inputqty','fd_mb_loss', 'fd_mb_residue', 'fd_mb_aftermain','fd_mb_main','fd_mb_f2','fd_mb_f1','fd_mb_water')
    def validate_mb_fd(self):
        sums = self.fd_mb_loss + self.fd_mb_residue + self.fd_mb_aftermain + self.fd_mb_main + self.fd_mb_f2 + self.fd_mb_f1 + self.fd_mb_water

        if self.fd_mb_inputqty == sums:
            
            raise UserError("Value Matched","All Value Matched")
        else :
            raise UserError("Failed","Value Does not Match") 
    



    # striping material balance
    @fields.depends('st_mb_inputqty') 
    def on_change_with_st_mb_inputqty_percent(self, name=None):
        return 100
    
    @fields.depends('st_mb_inputqty','st_mb_f1_mix')
    def on_change_with_st_mb_f1_mix_percent(self,name=None):
        try:
            test = self.st_mb_f1_mix/self.st_mb_inputqty
            percent = test*100 
            return percent
        except :
            return 0
    
    
    @fields.depends('st_mb_inputqty','st_mb_recyclable_f1')
    def on_change_with_st_mb_recyclable_f1_percent(self,name=None):
        try:
            test = self.st_mb_recyclable_f1/self.st_mb_inputqty
            percent = test*100 
            return percent
        except :
            return 0

    
    @fields.depends('st_mb_inputqty','st_mb_aftermain')
    def on_change_with_st_mb_aftermain_percent(self,name=None):
        try:
            test = self.st_mb_aftermain/self.st_mb_inputqty
            percent = test*100 
            return percent
        except :
            return 0

    @fields.depends('st_mb_inputqty','st_mb_strippingmain')
    def on_change_with_st_mb_strippingmain_percent(self,name=None):
        try:
            test = self.st_mb_strippingmain/self.st_mb_inputqty
            percent = test*100 
            return percent
        except :
            return 0
    
    @fields.depends('st_mb_inputqty','st_mb_bottom')
    def on_change_with_st_mb_bottom_percent(self,name=None):
        try:
            test = self.st_mb_bottom/self.st_mb_inputqty
            percent = test*100 
            return percent
        except :
            return 0

    @fields.depends('st_mb_inputqty','st_mb_dist_loss')
    def on_change_with_st_mb_dist_loss_percent(self,name=None):
        try:
            test = self.st_mb_dist_loss/self.st_mb_inputqty
            percent = test*100 
            return percent
        except :
            return 0

    @ModelView.button_change('st_mb_inputqty','st_mb_f1_mix', 'st_mb_recyclable_f1', 'st_mb_aftermain','st_mb_strippingmain','st_mb_bottom','st_mb_dist_loss')
    def validate_mb_stripping(self):
        sums = self.st_mb_f1_mix + self.st_mb_recyclable_f1 + self.st_mb_aftermain + self.st_mb_strippingmain + self.st_mb_bottom + self.st_mb_dist_loss

        if self.st_mb_inputqty == sums:
            
            raise UserError("Value Matched","All Value Matched")
        else :
            raise UserError("Failed","Value Does not Match") 


    @staticmethod
    def default_st_mb_inputqty():
        return 0

    @staticmethod
    def default_st_mb_f1_mix():
        return 0

    @staticmethod
    def default_st_mb_recyclable_f1():
        return 0

    @staticmethod
    def default_st_mb_strippingmain():
        return 0

    @staticmethod
    def default_st_mb_aftermain():
        return 0

    @staticmethod
    def default_st_mb_bottom():
        return 0

    @staticmethod
    def default_st_mb_dist_loss():
        return 0

    # water washing
    @staticmethod
    def default_ww_mb_inputqty():
        return 0
    
    @staticmethod
    def default_ww_mb_output():
        return 0

    @staticmethod
    def default_ww_mb_loss():
        return 0

    @staticmethod
    def default_ww_mb_consumption():
        return 0


    @fields.depends('ww_mb_inputqty') 
    def on_change_with_ww_mb_inputqty_percent(self, name=None):
        return 100


    @fields.depends('ww_mb_inputqty','ww_mb_output')
    def on_change_with_ww_mb_output_percent(self,name=None):
        try:
            test = self.ww_mb_output/self.ww_mb_inputqty
            percent = test*100 
            return percent
        except:
            return 0
    
    @fields.depends('ww_mb_inputqty','ww_mb_loss')
    def on_change_with_ww_mb_loss_percent(self,name=None):
        try:
            test = self.ww_mb_loss/self.ww_mb_inputqty
            percent = test*100 
            return percent
        except :
            return 0
        

    @fields.depends('ww_mb_inputqty','ww_mb_consumption')
    def on_change_with_ww_mb_consumption_percent(self,name=None):
        try:
            test = self.ww_mb_consumption/self.ww_mb_inputqty
            percent = test*100 
            return percent
        except :
            return 0


    @ModelView.button_change('ww_mb_inputqty','ww_mb_output', 'ww_mb_loss', 'ww_mb_consumption')
    def validate_mb_ww(self):
        sums = self.ww_mb_output + self.ww_mb_loss + self.ww_mb_consumption 

        if self.ww_mb_inputqty == sums:
            
            raise UserError("Value Matched","All Value Matched")
        else :
            raise UserError("Failed","Value Does not Match") 

    
# extractive distillation

    @fields.depends('ed_mb_inputqty') 
    def on_change_with_ed_mb_inputqty_percent(self, name=None):
        return 100
    
    @fields.depends('ed_mb_inputqty','ed_mb_f1_mix')
    def on_change_with_ed_mb_f1_mix_percent(self,name=None):
        try:
            test = self.ed_mb_f1_mix/self.ed_mb_inputqty
            percent = test*100 
            return percent
        except :
            return 0
    
    
    @fields.depends('ed_mb_inputqty','ed_mb_recyclable_f1')
    def on_change_with_ed_mb_recyclable_f1_percent(self,name=None):
        try:
            test = self.ed_mb_recyclable_f1/self.ed_mb_inputqty
            percent = test*100 
            return percent
        except :
            return 0

    
    @fields.depends('ed_mb_inputqty','ed_mb_aftermain')
    def on_change_with_ed_mb_aftermain_percent(self,name=None):
        try:
            test = self.ed_mb_aftermain/self.ed_mb_inputqty
            percent = test*100 
            return percent
        except :
            return 0

    @fields.depends('ed_mb_inputqty','ed_mb_strippingmain')
    def on_change_with_ed_mb_strippingmain_percent(self,name=None):
        try:
            test = self.ed_mb_strippingmain/self.ed_mb_inputqty
            percent = test*100 
            return percent
        except :
            return 0
    
    @fields.depends('ed_mb_inputqty','ed_mb_bottom')
    def on_change_with_ed_mb_bottom_percent(self,name=None):
        try:
            test = self.ed_mb_bottom/self.ed_mb_inputqty
            percent = test*100 
            return percent
        except :
            return 0

    @fields.depends('ed_mb_inputqty','ed_mb_dist_loss')
    def on_change_with_ed_mb_dist_loss_percent(self,name=None):
        try:
            test = self.ed_mb_dist_loss/self.ed_mb_inputqty
            percent = test*100 
            return percent
        except :
            return 0

    @ModelView.button_change('ed_mb_inputqty','ed_mb_f1_mix', 'ed_mb_recyclable_f1', 'ed_mb_aftermain','ed_mb_strippingmain','ed_mb_bottom','ed_mb_dist_loss')
    def validate_mb_ed(self):
        sums = self.ed_mb_f1_mix + self.ed_mb_recyclable_f1 + self.ed_mb_aftermain + self.ed_mb_strippingmain + self.ed_mb_bottom + self.ed_mb_dist_loss

        if self.ed_mb_inputqty == sums:
            
            raise UserError("Value Matched","All Value Matched")
        else :
            raise UserError("Failed","Value Does not Match") 


    @staticmethod
    def default_ed_mb_inputqty():
        return 0

    @staticmethod
    def default_ed_mb_f1_mix():
        return 0

    @staticmethod
    def default_ed_mb_recyclable_f1():
        return 0

    @staticmethod
    def default_ed_mb_strippingmain():
        return 0

    @staticmethod
    def default_ed_mb_aftermain():
        return 0

    @staticmethod
    def default_ed_mb_bottom():
        return 0

    @staticmethod
    def default_ed_mb_dist_loss():
        return 0



    
    
    

    
        
        
    
    @fields.depends('operation')
    def on_change_with_treatment_boolean(self, name=None):
        if (self.operation == None):
            return False
        else:
            if (self.operation.operation_type == 'treatment'):
                print('Success')
                return True
    @fields.depends('operation')
    def on_change_with_fd_boolean(self, name=None):
        if (self.operation == None):
            return False
        else:
            if (self.operation.operation_type == 'final_distilation'):
                print("final distillation")
                return True


    @fields.depends('operation')
    def on_change_with_ed_boolean(self, name=None):
        if (self.operation == None):
            return False
        else:
            if (self.operation.operation_type == 'extractive_distilation'):
                print("Extractive distillation")
                return True

    @fields.depends('operation')
    def on_change_with_ww_boolean(self, name=None):
        if (self.operation == None):
            return False
        else:
            if (self.operation.operation_type == 'water_washing'):
                print("Water Washing")
                return True

    @fields.depends('operation')
    def on_change_with_striping(self, name=None):
        if (self.operation == None):
            return False
        else:
            if (self.operation.operation_type == 'stripping'):
                print("Striping")
                return True       

 
class TreatmentFreeParameter(ModelSQL,ModelView):
    "Treatment Free Parameters"
    __name__ = "treatment.freeparameter"
    free_parameter = fields.Many2One('production.work' , 'Free Parameter Id')
    srno = fields.Char("Sr.No")
    rm_addition_details = fields.Char("RM addition details")
    lye_colected = fields.Char("Quantity Consumed")
    m_c = fields.Char("%M/c")
    preoxide_value  = fields.Char("Preoxide value")
    sign  = fields.Char("Sign")
    

class TreatmentMaterialBalance(ModelSQL,ModelView):
    "Treatment Material Balance"
    __name__ = "treatment.materialbalance"
    material_balance = fields.Many2One('production.work' , 'Material Balance Id')
    input_qty = fields.Char("Input qty")
    output_qty = fields.Char("Output qty")
    loss = fields.Char("Loss")
    lye_collected = fields.Char("Lye collected")
    
class FinalDistillationInput(ModelSQL,ModelView):
    "Final Distilaltion Input Details"
    __name__ = "finaldistillation.input"
    input_details = fields.Many2One('production.work' , 'Final Distillation Input Id')
    product = fields.Many2One('product.product' , 'Name of Material' ,
        domain=[('producible', '=', True)])
    unit = fields.Char("Unit")
    quantity = fields.Char("Qty taken for distillation")

class FinalDistillationAnalysis(ModelSQL,ModelView):
    "Temperature & analysis Record"
    __name__ = "finaldistillation.analysis"
    analysis_record = fields.Many2One('production.work' , 'Temperature & analysis Record Id')
    date = fields.Date("Date")
    time = fields.Char("Time")
    bottom = fields.Char("Bottom")
    mid_1 = fields.Char("Mid-1")
    mid_2 = fields.Char("Mid-2")
    top = fields.Char("Top")
    vacuum = fields.Char("Vacuum")
    feed_rate = fields.Char("Feed rate")
    reflux = fields.Char("Reflux")
    collection = fields.Char("Collection")
    sample = fields.Char("Sample")
    m_c = fields.Char("M/C")
    ph = fields.Char("Ph")
    density = fields.Char("Density")
    purity = fields.Char("Purity By GC")

class DistillationMaterialBalanceSummary(ModelSQL,ModelView):
    "Distillation Material Balance Summary"
    __name__ = "final.materialbalance"
    balance_table = fields.Many2One('production.work','Material Balance Summary')
    inputqty = fields.Char("Input qty")
    water = fields.Char("Water")
    f1 = fields.Char("F-1")
    f2 = fields.Char("F-2")
    main = fields.Char("Main")
    aftermain = fields.Char("After Main")
    residue = fields.Char("Residue")
    loss = fields.Char("Loss")

class ExtractiveDistillaion(ModelSQL,ModelView):
    "Extractive Distillation"
    __name__ = "ed.materialbalance"
    ed_balance = fields.Many2One('production.work' , 'Material Balance Summary')
    inputqty = fields.Char("Input")
    mix = fields.Char("f-1 mix")
    f1 = fields.Char("recycleable f-1")
    main = fields.Char("stripping main")
    after = fields.Char("after main")
    bottom = fields.Char("bottom")
    dist = fields.Char("dist.loss")

class WaterWashing(ModelSQL,ModelView):
    "Water Washing Balance Summary"
    __name__ = "ww.materialbalance"
    ww_balance = fields.Many2One('production.work' , 'Material Balance Summary')
    inputqty = fields.Char("Input")
    output = fields.Char("Output")
    loss = fields.Char("Loss")
    water = fields.Char("consumption of water")

class Stripping(ModelSQL,ModelView):
    "Stripping Balance Summary"
    __name__ = "striping.materialbalance"
    striping_balance = fields.Many2One('production.work' , 'Material Balance Summary')
    inputqty = fields.Char("Input")
    mix = fields.Char("f-1 mix")
    f1 = fields.Char("recycleable f-1")
    main = fields.Char("stripping main")
    after = fields.Char("after main")
    bottom = fields.Char("bottom")
    dist = fields.Char("dist.loss")
