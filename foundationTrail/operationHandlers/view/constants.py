INHERIT_ID_TMPLT = '<field name="inherit_id" ref="{inherited_view}" />'

VIEW_FILE_TMPLT = \
"""<?xml version="1.0" encoding="utf-8"?>
<odoo>

    <data>
        
        <record id="{view_name} model="ir.ui.view">
            <field name="name">{view_name.replace('_', '.')}</field>
            <field name="model">{model.replace('_', '.') if model is not None else ''}</field>
            <field name="arch" type="xml"></field>
        </record>

    </data>

</odoo>
"""


ERR_VIEW_DIRECTORY_NOT_FOUND = "Cannot find {view_directory} directory, so creating the file in the current directory (which is {current_directory})."
