import pytest
import os
from all_links.website import WebsiteArchitecture
from all_links.writer import FileWriter


class TestFileWriter:
    writer = FileWriter("test_output")

    @pytest.fixture
    def website_arch(self, website_links):
        return WebsiteArchitecture(website_links)

    def test_to_json(self, website_arch):
        self.writer.write_architecture_to_json(website_arch)
        assert os.path.exists("test_output") is True

    def test_to_xml(self, website_arch):
        self.writer.write_architecture_to_xml(website_arch)
        assert os.path.exists("test_output") is True
