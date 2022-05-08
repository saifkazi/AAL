# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

try:
    from trytond.modules.hsn-sac.tests.test_hsn-sac import suite  # noqa: E501
except ImportError:
    from .test_hsn-sac import suite

__all__ = ['suite']
