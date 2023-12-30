from maltego_trx.decorator_registry import TransformRegistry, TransformSet

registry = TransformRegistry(
        owner="Megadose/Mario Rojas (aka Turroks)",
        author="Megadose/Mario Rojas (aka Turroks)",
        host_url="https://transforms.mro.com",
        seed_ids=["holehe"]
)

# The rest of these attributes are optional

holehe_set = TransformSet('HOLEHE', "Maltego HOLEHE Transforms")

# metadata
registry.version = "0.1"

# global settings
# from maltego_trx.template_dir.settings import api_key_setting
# registry.global_settings = [api_key_setting]

# transform suffix to indicate datasource
# registry.display_name_suffix = " [ACME]"

# reference OAuth settings
# registry.oauth_settings_id = ['github-oauth']
