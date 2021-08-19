"""Tests standard tap features using the built-in SDK tests library."""

import datetime

from singer_sdk.testing import get_standard_tap_tests

from tap_productboard.tap import TapProductboard

SAMPLE_CONFIG = {
    "start_date": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d"),
    "auth_token": f"eyJ0eXAiOiJKV1QiLCJraWQiOiIwYmYzYWNjYzcwODlhODJjYjMxNjRhYmNiMDhjYzQ2OTM3N2QxZmM2YTkzMzY2YmQzM2MxZTFiODgyZjg3YTA5IiwiYWxnIjoiUlM1MTIifQ.eyJpc3MiOiJhYzMzYTNlOC00MjQyLTQyMGMtYjE5Ni1hMzQ5MDE1YjhmZTQiLCJzdWIiOiIyNzU3NyIsInJvbGUiOiJhZG1pbiIsImF1ZCI6Imh0dHBzOi8vYXBpLnByb2R1Y3Rib2FyZC5jb20iLCJ1c2VyX2lkIjoyNzU3Nywic3BhY2VfaWQiOiIxMTczMyIsImlhdCI6MTYyOTI1MjU5NX0.ErOu5NlRtyuUe5AoLzFY7rRn_dvquKdI7t3vO-uaHYn_zK3pITcOTB0vinqc_l50yO92rQW_5ySDdgo6kQM7h7TnUyArLPWAEdgIvEn-jVKWgFgZtHkKGCFmwZjzCLRBjf3znfCLcrAGY-eCpa3AQBGTi-h8KaDTLC48tay0YhYjYKbx2Axzr9U9HZjm2YSdeHlGTTmKdWibkQXqWsdPjiX9nRRcQUzI2g8yGj_364YyP3okUcAfgz4lln-vpn9cvHf1bgmnikaewxMqI7ntmYI2BMYK_pPCyUxvqGoZ65HAInww25V0SS7PG8AbbB-V138KhAHlQHb-I_yyvdszlA"
}


# Run standard built-in tap tests from the SDK:
def test_standard_tap_tests():
    """Run standard tap tests from the SDK."""
    tests = get_standard_tap_tests(
        TapProductboard,
        config=SAMPLE_CONFIG
    )
    for test in tests:
        test()


# TODO: Create additional tests as appropriate for your tap.
