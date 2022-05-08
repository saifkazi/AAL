from trytond.model import ModelSQL, ModelView, fields ,Workflow
from trytond.pool import Pool, PoolMeta
from trytond.report import Report
from trytond.pyson import If, Eval, Bool
from trytond.wizard import Wizard, StateTransition, StateView, Button ,StateAction
from trytond.transaction import Transaction
from trytond.pyson import PYSONEncoder
from trytond.exceptions import UserError

__all__ = ['QualityControlProduction','QualityShipmentIn','ProdShipment','TemperatureAnalysisRecord','PreProductionAnalysisWiz' ]


class ProductionReport(Report):
    __name__ = 'production.report'

    @classmethod
    def get_context(cls, production, data):
        pool = Pool()
        Production = pool.get('production')
        context = super(ProductionReport,cls).get_context(production,data)
        print("Production")
        print(str(production))
        print(str(data))
        # employee_id = Transaction().context.get('employee')
        print("this is production , " , production)
        production = Production(data["id"])
        context['production'] = production
        # inwards = ''
        # context['productname'] = production.product
        for i in production.inwardno:
            # print ("this is I" ,i.reference)
            inwards += i.reference + ", "
        context['inwards'] = inwards
        context['treatment_boolean'] = False
        for i in production.works:
            if i.operation.operation_type == "treatment":
                context['treatment_boolean'] = True
                context['treatment_equipment_no'] = i.equipment_no
                # context['from'] = i.cycles.from_
                # context['to'] = i.cycles.to
                # print ("this is I" ,i.cycles.to)
                context['initialPH'] = i.initial_ph
                context['finalPH'] = i.final_ph
                context['initialmoisture'] = i.initial_moisture
                context['finalmoisture'] = i.final_moisture
                context['phadjustment'] = i.qty_sulphuric
                context['stabilizer'] = i.qty_bht
                context['T_ip_qty'] = i.treatment_input_qty
                context['T_ip_qty_per'] = i.treatment_input_qty_percent
                context['T_io_qty'] = i.treatment_output_qty
                context['T_io_qty_per'] = i.treatment_output_qty_percent
                context['T_loss'] = i.treatment_loss
                context['T_loss_per'] = i.treatment_loss_percent
                context['T_lye'] = i.treatment_lye_collected
                context['T_lye_per'] = i.treatment_lye_collected_percent
        return context

class StockShipmentOut(Workflow,ModelSQL, ModelView):
    
    __name__ = "stock.shipment.out"

    post_prod_ref = fields.Many2One('quality.control.postproduction', 'Post Production Analysis')


        
class QualityControlProduction(Workflow,ModelSQL, ModelView):
    "Quality Control Production"
    __name__ = 'production'
    party = fields.Many2One('party.party','Party')
    reactorno = fields.Char('Reactor No')
    reactorcapacity =  fields.Integer('Reactor Capacity')
    postproduction_state = fields.Selection([
            ('pending', 'Pending'),
            ('approved', 'Approved'),
            ('rejected', 'Rejected'),
            ], 'Post Production Analysis',
            states={
                'invisible': ~Eval('state').in_(['running','done']),
                }, readonly=True)
    
    # details = fields.Text("Deviation Details")
    remarks = fields.Text("Remarks")
    # inputqty = fields.Char("Input qty")
    # water = fields.Char("Water")
    # f1 = fields.Char("F-1")
    # f2 = fields.Char("F-2")
    # main = fields.Char("Main")
    # aftermain = fields.Char("After Main")
    # residue = fields.Char("Residue")
    # loss = fields.Char("Loss")
    # inwardno = fields.Many2Many('prod.shipment.relation',
    #     'prodid','shipid', 'Inward',domain=[
    #         ('supplier', '=', ('party.party', Eval('party',-1))),
    #         ])

   
    @staticmethod
    def default_postproduction_state():
        return 'pending'

        

   

class QualityShipmentIn(Workflow,ModelSQL,ModelView):
    "Quality Shipment In"
    __name__ = "stock.shipment.in"
    inwardid = fields.Many2One('production','Inward ID')
    prodstate = fields.Boolean("In Production")
    net_wt = fields.Float('Net Wt.') 
    gross_wt = fields.Float('Gross Wt.') 
    tare_wt = fields.Float('Tare Wt.') 
    remaining_qty = fields.Float('Remaining Qty', readonly=True,
    states={
                'invisible': ~Eval('state').in_(['done']),
                })
    preproduction_state = fields.Selection([
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected')
        ], ' Pre Production Analysis', readonly=True,
        help="The current state of the Pre Production.",
        states={
                'invisible': ~Eval('state').in_(['received', 'done']),
                })
    
    production_state = fields.Selection([
        ('pending', 'Pending'),
        ('done', 'Done')
        ], 'Production',readonly=True, 
        help="The current state of the Production.",
        states={
                'invisible': ~Eval('state').in_(['done']),
                })
    
    @staticmethod
    def default_preproduction_state():
        return 'pending'
    
    
    # @staticmethod
    # def default_remaining_qty():
    #     print("sasa"+str(Transaction().context.get('active_id')))
    #     return 10
    
    
    @classmethod
    def __setup__(cls):
        super(QualityShipmentIn, cls).__setup__()
        cls._buttons.update({
                'preproduction': {
                    'invisible': ~Eval('state').in_(['received','done']),
                    'depends': ['state'],
                    },
                'process': {
                    'invisible': ~Eval('state').in_(['received','done']),
                    'depends': ['state'],
                    },
                'production': {
                    'invisible': ~Eval('state').in_(['done']),
                    'depends': ['state'],
                    },
                'production_process': {
                    'invisible': ~Eval('state').in_(['done']),
                    'depends': ['state'],
                    },
            })
    
    @classmethod
    @ModelView.button_action('quality_control.act_create_preproduction')
    def preproduction(cls, shipment):
        pass
    
    @classmethod
    @ModelView.button_action('quality_control.act_preproduction_process')
    def process(cls, shipment):
        pass

    @staticmethod
    def default_production_state():
        return 'pending'
    
    @classmethod
    @ModelView.button_action('quality_control.act_create_production')
    def production(cls, shipment):
        pass

class Process(Wizard):
    'Process'
    __name__ = 'shipment.preproduction.process'
    start = StateTransition()

    def transition_start(self):
        active_id = Transaction().context.get('active_id')
        try:
            reg_id = \
                Pool().get('stock.shipment.in').browse([active_id])[0]
            
        except:
            raise UserError("You cannot process.")

        PRE_QC =  Pool().get('quality.control.preproduction')
        pre_qc = PRE_QC.search([
                ('shipment', '=', reg_id),
                ])
        ShipmentIn = Pool().get('stock.shipment.in')
        Production = Pool().get('production')
        
        shipments = ShipmentIn.search([
                ('id', '=', active_id),
                ])
        List = []

        for i in pre_qc:
            List.append(i.state)

        if len(List) == 0:
            ShipmentIn.write(shipments, {'preproduction_state': 'pending'})
        else:
            if "draft" in List:
                ShipmentIn.write(shipments, {'preproduction_state': 'pending'})                
            elif "rejected" in List:
                ShipmentIn.write(shipments, {'preproduction_state': 'pending'})
            else: 
                ShipmentIn.write(shipments, {'preproduction_state': 'approved'})
                

            

        return 'end'
    
    def end(self):
        return 'reload'
     


class PreProductionAnalysisWiz(Wizard):
    "PreProduction Analysis"
    __name__ = 'shipment.preproduction.create'
    start_state = 'ask'
    ask = StateAction('quality_control.shipment_pre_act_qualitycontrol_form')


    def do_ask(self, action):
        ask = Transaction().context.get('active_id')

        try:
            reg_id = \
                Pool().get('stock.shipment.in').browse([ask])[0]
        except:
            raise UserError("You cannot process.")
        
        supplier = reg_id.id

        action['pyson_domain'] = PYSONEncoder().encode([
            ('shipment', '=', supplier)
            ])
        
        action['pyson_context'] = PYSONEncoder().encode({
            'shipment': supplier,
            })
        return action, {}

class ProductionProcess(Wizard):
    "Shipment Production Create"
    __name__ = 'shipment.production.create'
    start_state = 'ask'
    ask = StateAction('quality_control.shipment_production_form')


    def do_ask(self, action):
        ask = Transaction().context.get('active_id')

        try:
            reg_id = \
                Pool().get('stock.shipment.in').browse([ask])[0]
        except:
            raise UserError("You cannot process.")
        
        supplier = reg_id.supplier.id

        action['pyson_domain'] = PYSONEncoder().encode([
            ('party', '=', supplier)
            ])
        
        action['pyson_context'] = PYSONEncoder().encode({
            'party': supplier,
            })
        return action, {}

        

    
   

class CreatePreProduction(ModelView):
    "PreProduction Analysis"
    __name__ = 'preproduction.create.ask'
    shipment = fields.Many2One('stock.shipment.in', "Shipment", required=True)

    @classmethod
    def default_shipment(cls):
        context = Transaction().context
        if context.get('active_model') == 'stock.shipment.in':
            return context.get('active_id')

class ProdShipment(ModelSQL):
    
    "Prod Shipment Relation"
    __name__ = "prod.shipment.relation"
    
    shipid = fields.Many2One('stock.shipment.in','Shipment ID')
    prodid = fields.Many2One('production','Production ID')
    

class TemperatureAnalysisRecord(ModelSQL,ModelView):
    "Temperature and Analysis Record"
    __name__ = "temp.analysis.record"
    temp_table = fields.Many2One('production' , 'Temperature Record')
    date = fields.Date("Date")
    time = fields.Char("Time")
    bottom = fields.Char("Bottom")
    mid1 = fields.Char("Mid-1")
    mid2 = fields.Char("Mid-2")
    top = fields.Char("Top")
    vaccum = fields.Char("Vaccum")
    feedrate = fields.Char("Feed Rate")
    reflux = fields.Char("Reflux")
    collection = fields.Char("Collection")
    sample = fields.Char("Sample")
    mc = fields.Char("M/C")
    ph = fields.Char("ph")
    density = fields.Char("Density")
    purity = fields.Char("Purity By GC")
    purity1 = fields.Char(" ")
    purity2 = fields.Char(" ")
    purity3 = fields.Char(" ")
    purity4 = fields.Char(" ")
    purity5 = fields.Char(" ")
    sign = fields.Char("Sign")

