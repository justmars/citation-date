import re

from citation_date import DatedText, decode_date, docket_date, report_date


def test_docket():
    pattern = re.compile(docket_date, re.I | re.X)
    text = "G.R. No. 12345, Dec,1,  2000"
    match = pattern.search(text)
    date_match = match and match.group("docket_date")
    assert date_match == "Dec,1,  2000"
    assert decode_date(date_match) == "December 01, 2000"
    assert DatedText(raw=text).as_string == "December 01, 2000"


def test_report():
    pattern = re.compile(report_date, re.I | re.X)
    text = "1 SCRA 200 (1Dec.  2000)"
    match = pattern.search(text)
    date_match = match and match.group("report_date")
    assert date_match == "(1Dec.  2000)"
    assert decode_date(date_match) == "December 01, 2000"
    assert DatedText(raw=text).as_string == "December 01, 2000"
