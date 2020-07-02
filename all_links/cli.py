import sys
import logging
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

        parser.add_argument("--log", help="see detailed logs", type=str)

        self.args = parser.parse_args()
        self.write_simple_log = lambda text: sys.stdout.write(
            colored(f"\n => {text}\n", "red")
        )

    def _set_detailed_logs(self):
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        stdout_handler = logging.StreamHandler(sys.stdout)
        logger.addHandler(stdout_handler)

    def _handle_xml_output(self, links):
        self.write_simple_log(f"Creating {self.args.filename}.xml\n")
        writer = FileWriter(f"{self.args.filename}.xml")
        writer.write_architecture_to_xml(WebsiteArchitecture(links))
        self.write_simple_log(
            f"Website urls written in {self.args.filename}.xml successfully. \n"
        )

    def _handle_json_output(self, links):
        self.write_simple_log(f"Creating {self.args.filename}.json\n")
        writer = FileWriter(f"{self.args.filename}.json")
        writer.write_architecture_to_json(WebsiteArchitecture(links))
        self.write_simple_log(
            f"Website urls written in {self.args.filename}.json successfully. \n"
        )

    def _handle_stdout(self, links):
        stdout = LinksPrinter(links)
        sys.stdout.write(str(stdout))
        self.write_simple_log(f"Website urls written successfully into STDOUT. \n")

    def run(self):
        if self.args.log == "yes":
            self._set_detailed_logs()

        if self.args.output in ("json", "xml", "stdout"):
            self.write_simple_log(f"Asking {self.args.url}")
            website = Website(self.args.url)
            links = website.get_links()

            if self.args.output == "xml":
                self._handle_xml_output(links)

            if self.args.output == "json":
                self._handle_json_output(links)

            if self.args.output == "stdout":
                self._handle_stdout(links)

        else:
            self.write_simple_log(
                'ERROR:"output" argument as to be "xml", "json" or "stdout" !'
            )
