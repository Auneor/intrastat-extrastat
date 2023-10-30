# -*- coding: utf-8 -*-

import logging
from odoo import api, SUPERUSER_ID

_logger = logging.getLogger(__name__)

__name__ = "Upgrade to 16.0.2.0.0"


def migrate(cr, version):
    if not version:
        return

    _logger.info("Set Tags Manager default values")
    env = api.Environment(cr, SUPERUSER_ID, {})

    cr.execute("""
        UPDATE product_template AS pt
        SET hs_code_id = CAST(split_part(ir.value_reference, ',', 2) AS Integer)
        FROM ir_property AS ir
        WHERE 
            split_part(ir.res_id, ',', 1) = 'product.template'
            AND pt.id = CAST(split_part(ir.res_id, ',', 2) AS Integer)
            AND CAST(split_part(ir.value_reference, ',', 2) AS Integer) IN (SELECT id FROM hs_code);
        """)

    cr.execute("""
        UPDATE product_category AS pc
        SET hs_code_id = CAST(split_part(ir.value_reference, ',', 2) AS Integer)
        FROM ir_property AS ir
        WHERE 
            split_part(ir.res_id, ',', 1) = 'product.category'
            AND pc.id = CAST(split_part(ir.res_id, ',', 2) AS Integer)
            AND CAST(split_part(ir.value_reference, ',', 2) AS Integer) IN (SELECT id FROM hs_code);
        """)



