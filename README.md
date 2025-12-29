# foundationTrail

`foundationTrail` an odoo module generator.

When creating a module for Odoo, the developer faces a few scaffolding actions that are mechanical and repetitive. Though simple, those actions are an easy break point for the developer, who finds themself to debug an unneeded problem.

Here comes in `foundationTrail`.
`foundationTrail` takes care of creating the necessary files, and update the `__manifest__.py` file accordingly.

As of now, using `foundationTrail`, you can:

1. Create a *whole new module*, comprehensive of `__manifest__.py` file, `models/` and `wizards/` directories, and a starting file in `models/`.
2. Create a *single model*, and it will be automatically added to the `__init__.py` file, in the `modules/` or in the `wizards/` directory.
3. Create a *view file*, and it will be automatically added to the `__manifest__.py` file.
4. Create the security file (`ir.model.access.csv`) entirely, and automatically add it to the `__manifest__.py` file.
5. Add a new line to the security file in the `security/` directory.


As of now, the operations that `foundationTrail` supports are quite limited. But more development is coming!