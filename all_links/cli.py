import sys
from argparse import ArgumentParser

from termcolor import colored

from all_links.website import Website
from all_links.printer import LinksPrinter
from all_links.writer import FileWriter
from all_links.website import WebsiteArchitecture


class CLI:
    def __init__(self):
        parser = ArgumentParser()
        parser.add_argument(
            "url", help="The website URL (ex: https://reachip.github.io)", type=str
        )
        parser.add_argument("output", help="Output : xml - json - stdout", type=str)
        parser.add_argument(
            "--filename",
            help="output filename if you want to generate a JSON or XML format",
            type=str,
        )
        self.args = parser.parse_args()

    def run(self):
        if self.args.output in ("json", "xml", "stdout"):
            website = Website(self.args.url)
            links = website.get_links()

            if self.args.output == "xml":
                writer = FileWriter(f"{self.args.filename}.xml")
                writer.write_architecture_to_xml(WebsiteArchitecture(links))

            if self.args.output == "json":
                writer = FileWriter(f"{self.args.filename}.json")
                writer.write_architecture_to_json(WebsiteArchitecture(links))

            if self.args.output == "stdout":
                stdout = LinksPrinter(links)
                sys.stdout.write(str(stdout))

        else:
            sys.stdout.write(
                colored(
                    '\n ERROR:"output" argument as to be "xml", "json" or "stdout" ! \n',
                    "red",
                )
            )
