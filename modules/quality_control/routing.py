from trytond.model import ModelSQL, ModelView, fields
from trytond.pool import Pool, PoolMeta


class OperationType(metaclass=PoolMeta):
    __name__ = 'production.routing.operation'
    operation_type = fields.Selection([
        ('extractive_distilation', 'Extractive Distilation'),
        ('stripping', 'Stripping'),
        ('treatment', 'Treatment'),
        ('water_washing', 'Water Washing'),
        ('final_distilation', 'Final Distilation'),
        ], string='Type' , required = True )


