from termcolor import colored
from website import WebsiteArchitecture


class LinksPrinter:
    def __init__(self, links):
        self.links = links

    def __str__(self):
        website_architecture = WebsiteArchitecture(self.links)
        output = ""

        for key, links in website_architecture.to_dict().items():
            output += f"\n{colored(f'===> {key}', 'green', attrs=['bold'])}\n\n"

            for link in links:
                output += f"|   {colored(link, 'yellow', attrs=['bold'])}\n"

        output += "\n\n"

        return output
