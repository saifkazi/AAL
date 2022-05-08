# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

from trytond.pool import Pool
# from qualitycontrol import QualityControl
from . import qualitycontrol
from . import production
from . import routing
from . import work
from . import stock

__all__ = ['register']


def register():
    Pool.register(
        work.Stripping,
        work.WaterWashing,
        work.ExtractiveDistillaion,
        work.DistillationMaterialBalanceSummary,
        work.FinalDistillationAnalysis,
        work.FinalDistillationInput,
        work.TreatmentMaterialBalance,
        work.WorkType,
        work.TreatmentFreeParameter,
        routing.OperationType,
        qualitycontrol.PostProductionCustomerSpecification,
        qualitycontrol.PostProductionRejectedAnalysis,
        qualitycontrol.PostProductionAnalysis,
        qualitycontrol.PostProductionAnalysis1,
        qualitycontrol.PreProductionLabCritarea1,
        # qualitycontrol.PreProductionCustomerSpecification,
        qualitycontrol.PreProductionRejectedAnalysis,
        qualitycontrol.PreProductionLabCritarea,
        qualitycontrol.QualityControlPreproduction,
        qualitycontrol.QualityControlPostproduction,
        production.QualityControlProduction,
        production.QualityShipmentIn,
        production.ProdShipment,
        production.TemperatureAnalysisRecord,
        production.CreatePreProduction,
        production.StockShipmentOut,
        # production.MaterialBalanceSummary,
        qualitycontrol.DeviationTable,
        qualitycontrol.StandardAnalysis,
        qualitycontrol.GcAnalysis,


        
        module='quality_control', type_='model')
    Pool.register(
        production.PreProductionAnalysisWiz,
        production.Process,
        production.ProductionProcess,
        module='quality_control', type_='wizard')
    Pool.register(
        production.ProductionReport,
        stock.InwardReport,
        module='quality_control', type_='report')