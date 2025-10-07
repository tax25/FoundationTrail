# Aodoo

Aodoo - an odoo module generator.

The aim of Aodoo is to automate all those processes (module creation, model creation, view creation, etc...) so that one can fully concentrate on developing the actual model rather than on creating the boilerplate.

This is a really immature project. Some functionalities are already developed.


## *NOTE on 7th October 2025*
The development of this project has gone a long way since the start.
Now quite a lot of things can be done with **aodoo**.
Here's a recap:

1. Create a new module from scratch - either an app or a module. Dependencies can be specified right away.
2. Create a new model inside an existing module, with it being inserted into the `__init__.py` file. With a basic security line in `security/ir.model.access.csv`
3. Create a new view inside an existing module, with it being inserted into the `__manifest__.py` file.
4. Create a new wizard, given the right flags, in an existing module.

The thing that I feel is missing from this tool (other than a fair bit of polishing) is the possibility to insert a new record inside an already existing xml file.
I believe that would be of great help.
