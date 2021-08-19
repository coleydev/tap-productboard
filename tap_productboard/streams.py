"""Stream type classes for tap-productboard."""

from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_productboard.client import ProductboardStream

SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")

class FeatureStream(ProductboardStream):
    """Define custom stream."""
    print("FeatureStream")
    name = "features"
    path = "/features"
    primary_keys = ["id"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "features.json"
