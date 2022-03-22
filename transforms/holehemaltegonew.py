from maltego_trx.maltego import MaltegoTransform, MaltegoMsg
from maltego_trx.template_dir.extensions import registry
from maltego_trx.transform import DiscoverableTransform
import trio
from holehe import *
from holehe.core import *


@registry.register_transform(display_name="Email to Registered Accounts [HOLEHE]", input_entity="maltego.EmailAddress",
                             description='Returns accounts associated with an email address.',
                             settings=[],
                             output_entities=["maltego.Unknown"])
class holehemaltegonew(DiscoverableTransform):

    @classmethod
    def create_entities(cls, request: MaltegoMsg, response: MaltegoTransform):

        async def maincore():

            def get_timeout():
                """Get Timeout from Gravatar.com"""
                check_timeout = httpx.get("https://gravatar.com")
                timeout_value = int(check_timeout.elapsed.total_seconds() * 6) + 5
                return (timeout_value)

            email = request.Value
            # Import Modules
            modules = import_submodules("holehe.modules")
            websites = get_functions(modules)
            # Get timeout
            timeout = get_timeout()
            # Def the async client
            client = httpx.AsyncClient(timeout=timeout)
            # Launching the modules
            out = []
            async with trio.open_nursery() as nursery:
                for website in websites:
                    nursery.start_soon(launch_module, website, email, client, out)

            # Sort by modules names
            out = sorted(out, key=lambda i: i['name'])
            # Close the client
            await client.aclose()

            for website in out:

                if website["exists"] == True:

                    web = response.addEntity("maltego.Website", website["domain"])
                    web.setNote("Found")

                    if website["emailrecovery"] != None:
                        email = response.addEntity("maltego.EmailAddress", website["emailrecovery"])
                        email.setLinkLabel("Found in " + website["domain"])

                    if website["phoneNumber"] != None:
                        email = response.addEntity("maltego.PhoneNumber", website["phoneNumber"])
                        email.setLinkLabel("Found in " + website["domain"])

                    if website["others"] != None:
                        response.addEntity("maltego.Phrase",
                                              "Found from " + website["name"] + str(website["others"]))

        trio.run(maincore)



