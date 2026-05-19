MANIFEST_FILENAME = '__manifest__.py'

INHERIT_ID_TMPLT = '<field name="inherit_id" ref="{inherited_view}" />'

VIEW_FILE_TMPLT = \
"""<?xml version="1.0" encoding="utf-8"?>
<odoo>

    <data>
        
        <record id="{view_name}" model="ir.ui.view">
            <field name="name">{name}</field>
            <field name="model">{model}</field>
            {inherit_id_string}
            <field name="arch" type="xml"></field>
        </record>

    </data>

</odoo>
"""

INFO_VIEW_FILE_CREATED = "View file created and added to the __manifest__.py file as {file_name}."

ERR_VIEW_DIRECTORY_NOT_FOUND = "Cannot find {view_directory} directory, so creating the file in the current directory (which is {current_directory})."

ERR_MANIFEST_FILE_NOT_FOUND = "Cannot find __manifest__.py, view file generated in {view_generation_dir} but not added to __manifest__.py"

ERR_MANIFEST_VALUE_NOT_VALID = "The manifest is either empty or invalid!"
