"""REST client handling, including ProductboardStream base class."""

import requests
from base64 import b64encode
from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable

from singer_sdk.helpers.jsonpath import extract_jsonpath
from singer_sdk.streams import RESTStream


SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")


class ProductboardStream(RESTStream):
    """Productboard stream class."""

    url_base = "https://api.productboard.com"

    # OR use a dynamic url_base:
    # @property
    # def url_base(self) -> str:
    #     """Return the API URL root, configurable via tap settings."""
    #     return self.config["api_url"]

    records_jsonpath = "$.data.[*]"  # Or override `parse_response`.
    # Or override `get_next_page_token`.
    # next_page_token_jsonpath = "$.links.next"

    @property
    def http_headers(self) -> dict:
        print("http_headers")
        headers = {}
        auth_token = self.config.get("auth_token")

        headers["Authorization"] = f"Bearer {auth_token}"
        headers["X-Version"] = "1"

        return headers

    def get_url_params(
        self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> Dict[str, Any]:
        """Return a dictionary of values to be used in URL parameterization."""
        next_page_token = next_page_token or 0
        params = {"pageLimit": "100",
                  "pageOffset": next_page_token}
        return params

    def get_next_page_token(self, response: requests.Response, previous_token: int) -> str:
        print("get_next_page_token")
        print("Previous Token:", previous_token)

        resp_json = response.json()

        previous_token = previous_token or 0
        
        if resp_json['links']['next']:
            next_page_token = previous_token + 100
        else:
            next_page_token = None
        return next_page_token

    def parse_response(self, response: requests.Response) -> Iterable[dict]:
        """Parse the response and return an iterator of result rows."""
        # TODO: Parse response body and return a set of records.
        resp_json = response.json()
        print(resp_json['links']['next'])
        for row in resp_json["data"]:
            # self.logger.info(row.keys())
            # self.logger.info(row.get("_expandable"))
            # self.logger.info(row["_links"])
            yield row


# cli = TapProductboard.cli
