import json
import os
import unittest
from pathlib import Path
from .. import somef_cli
from ..utils import constants

test_data_path = str(Path(__file__).parent / "test_data") + os.path.sep
test_data_repositories = str(Path(__file__).parent / "test_data" / "repositories") + os.path.sep


class TestJSONExport(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Runs somef_cli once and saves the JSON"""
        cls.json_file = test_data_path + "test_json_widoco_export.json"
        
        somef_cli.run_cli(threshold=0.8,
                          ignore_classifiers=False,
                          repo_url="https://github.com/dgarijo/Widoco",
                          local_repo=None,
                          doc_src=None,
                          in_file=None,
                          output=cls.json_file,
                          graph_out=None,
                          graph_format="turtle",
                          codemeta_out=None,
                          pretty=True,
                          missing=False,
                          readme_only=False)

        with open(cls.json_file, "r") as f:
            cls.json_content = json.load(f)

    def test_issue_417(self):
        """Checks whether a repository correctly extracts to Codemeta"""
        somef_cli.run_cli(threshold=0.8,
                          ignore_classifiers=False,
                          repo_url="https://github.com/dgarijo/Widoco",
                          local_repo=None,
                          doc_src=None,
                          in_file=None,
                          output=None,
                          graph_out=None,
                          graph_format="turtle",
                          codemeta_out=test_data_path + "test-417.json-ld",
                          pretty=True,
                          missing=False,
                          readme_only=False)
        
        text_file = open(test_data_path + "test-417.json-ld", "r")
        data = text_file.read()
        text_file.close()
        json_content = json.loads(data)
        issue_tracker = json_content["issueTracker"]  # JSON is in Codemeta format
        
        #len(json_content["citation"]) 
        #codemeta category citation is now referencePublication
        assert issue_tracker == 'https://github.com/dgarijo/Widoco/issues' and len(json_content["referencePublication"]) > 0 and \
               len(json_content["name"]) > 0 and len(json_content["identifier"]) > 0 and \
               len(json_content["description"]) > 0 and len(json_content["readme"]) > 0 and \
               len(json_content["author"]) > 0 and len(json_content["buildInstructions"]) > 0 and \
               len(json_content["softwareRequirements"]) > 0 and len(json_content["programmingLanguage"]) > 0 and \
               len(json_content["keywords"]) > 0 and len(json_content["logo"]) > 0 and \
               len(json_content["license"]) > 0 and len(json_content["dateCreated"]) > 0
        
        os.remove(test_data_path + "test-417.json-ld")

    def test_issue_311(self):
        """Checks if Codemeta export has labels defined outside Codemeta"""
        somef_cli.run_cli(threshold=0.8,
                          ignore_classifiers=False,
                          repo_url=None,
                          doc_src=test_data_path + "repostatus-README.md",
                          in_file=None,
                          output=None,
                          graph_out=None,
                          graph_format="turtle",
                          codemeta_out=test_data_path + "test-repostatus-311.json-ld",
                          pretty=True,
                          missing=False)
        text_file = open(test_data_path + "test-repostatus-311.json-ld", "r")
        data = text_file.read()
        text_file.close()
        assert data.find("\"repoStatus\":") < 0
        os.remove(test_data_path + "test-repostatus-311.json-ld")

    def test_issue_150(self):
        """Codemeta export checks"""
        somef_cli.run_cli(threshold=0.8,
                          ignore_classifiers=False,
                          repo_url=None,
                          doc_src=test_data_path + "README-mapshaper.md",
                          local_repo=None,
                          in_file=None,
                          output=None,
                          graph_out=None,
                          graph_format="turtle",
                          codemeta_out=test_data_path + "test-150.json-ld",
                          pretty=True,
                          missing=False)
        text_file = open(test_data_path + "test-150.json-ld", "r")
        data = text_file.read()
        text_file.close()
        assert data.find(constants.CAT_ACKNOWLEDGEMENT) == -1
        os.remove(test_data_path + "test-150.json-ld")

    def test_issue_281(self):
        """Checks if missing categories are properly added to the output JSON, when required"""
        somef_cli.run_cli(threshold=0.8,
                          ignore_classifiers=False,
                          repo_url=None,
                          doc_src=test_data_path + "repostatus-README.md",
                          in_file=None,
                          output=test_data_path + "test-281.json",
                          graph_out=None,
                          graph_format="turtle",
                          codemeta_out=None,
                          pretty=True,
                          missing=True)
        text_file = open(test_data_path + "test-281.json", "r")
        data = text_file.read()
        text_file.close()
        assert data.find(constants.CAT_MISSING) > 0
        os.remove(test_data_path + "test-281.json")

    def test_issue_629(self):
        """Checks if citattion have news properties """
        # somef_cli.run_cli(threshold=0.8,
        #                   ignore_classifiers=False,
        #                   repo_url=None,
        #                   doc_src=None,
        #                   local_repo=test_data_repositories + "Widoco",
        #                   in_file=None,
        #                   output=test_data_path + "test_issue_629.json",
        #                   graph_out=None,
        #                   graph_format="turtle",
        #                   codemeta_out=None,
        #                   pretty=True,
        #                   missing=True)
        
        # with open(test_data_path + "test_issue_629.json", "r") as text_file:
        #     data = json.load(text_file) 

        # citation = data.get("citation", [])
        citation = self.json_content.get("citation", [])
        assert citation, "No 'citation' found in JSON"
        assert any(
            entry.get("result", {}).get("format") == "cff" and
            "doi" in entry.get("result", {}) and
            "title" in entry.get("result", {})
            for entry in citation
        ), "Citation.cff must have doi and title"

        # os.remove(test_data_path + "test_issue_629.json")

    def test_issue_651(self):
        """Checks if keywords is in the missing categories because is empty"""
        somef_cli.run_cli(threshold=0.8,
                          ignore_classifiers=False,
                          repo_url=None,
                          doc_src=test_data_path + "README-panda.md",
                          in_file=None,
                          output=test_data_path + "test-651.json",
                          graph_out=None,
                          graph_format="turtle",
                          codemeta_out=None,
                          pretty=True,
                          missing=True)

        with open(test_data_path + "test-651.json", "r") as text_file:
            data = json.load(text_file)

        assert 'keywords' in data.get(constants.CAT_MISSING, []), "Keywords is not in CAT_MISSING" 
        os.remove(test_data_path + "test-651.json")

    def test_issue_745(self):
        """Checks whether all the items in license has a spdx_id"""
        somef_cli.run_cli(threshold=0.8,
                            ignore_classifiers=False,
                            repo_url="https://github.com/sunpy/sunpy",
                            local_repo=None,
                            doc_src=None,
                            in_file=None,
                            output=test_data_path + "test_issue_745.json",
                            graph_out=None,
                            graph_format="turtle",
                            codemeta_out=None,
                            pretty=True,
                            missing=False,
                            readme_only=False)
        
        text_file = open(test_data_path + "test_issue_745.json", "r")
        data = text_file.read()
        text_file.close()
        json_content = json.loads(data)
        licenses = json_content["license"]

        for i, license_entry in enumerate(licenses):
            assert "spdx_id" in license_entry["result"], f"Missing 'spdx_id' in license{i}"
            assert license_entry["result"]["spdx_id"], f"'spdx_id' empty in license {i}"
        
        os.remove(test_data_path + "test_issue_745.json")

    def test_issue_653(self):
        """Checks if json from widoco repo has more than 30 releases"""
        assert len(self.json_content["releases"]) > 30, f"Expected more than 30 releases, found {len(self.json_content['release'])}"

    @classmethod
    def tearDownClass(cls):
        """delete temp file JSON just if all the test pass"""
        if os.path.exists(cls.json_file): 
            try:
                os.remove(cls.json_file)
                print(f"Deleted {cls.json_file}") 
            except Exception as e:
                print(f"Failed to delete {cls.json_file}: {e}")  

if __name__ == '__main__':
    unittest.main()
