from trytond.wizard import Wizard, StateView, StateTransition, Button , StateAction
from trytond.model import (ModelView, ModelSQL, MultiValueMixin, ValueMixin,
    DeactivableMixin, fields, Unique, sequence_ordered)
from trytond.pool import Pool
import xlsxwriter
import io
from trytond.report import Report



class HSNCODES(ModelSQL,ModelView):
    'HSNCODES'
    __name__ = 'product.hsn'

    hsn_code = fields.Char("Code")
    product_description = fields.Char("Description")
    rate = fields.Numeric("GST")