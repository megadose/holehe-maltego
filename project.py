import os
import sys
import transforms

from maltego_trx.registry import register_transform_function, register_transform_classes
from maltego_trx.server import app, application
from maltego_trx.handler import handle_run
from extensions import registry


# register_transform_function(transform_func)
register_transform_classes(transforms)

registry.write_transforms_config()
registry.write_settings_config()
registry.write_local_mtz("./Maltego-HOLEHE.mtz", command=os.getenv("INTERPRETER"), debug=False)

handle_run(__name__, sys.argv, app)
