from trytond.model import ModelSQL, ModelView, fields
from trytond.pool import Pool, PoolMeta
from trytond.report import Report

class InwardReport(Report):
    __name__ = 'inward.report'

    @classmethod
    def get_context(cls, inward, data):
        pool = Pool()
        Inward = pool.get('stock.shipment.in')
        context = super(InwardReport,cls).get_context(inward,data)
        print("Inward")
        print(str(inward))
        print(str(data))
        # employee_id = Transaction().context.get('employee')
        
        inward = Inward(data["id"])
        context['inward'] = inward
        context['bulk'] = True
        # inwards = ''
        # context['productname'] = production.product
        # for i in production.inwardno:
        #     print ("this is I" ,i.reference)
        #     inwards += i.reference + ", "
        # context['inwards'] = inwards
        return context