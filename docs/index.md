---
hide:
- navigation
---
# Citation Date

## Concept

This is a regex date formula and decoder for dates in Philippine citations based on the following constraints:

1. Limit allowed years: `1900 - 2299`
2. Use regular days: `1 - 31`
3. Allow both traditional and unorthodox expression of months:
    - `Jan.`
    - `Dec.`
    - `mar`
    - `july`
    - `Sept`
4. Capture different date formats:
    - UK format: `day month, year`
    - US format: `month day, year`
5. Handle typographic issues, e.g. lacking space `Dec1,2000`

This is a dependency (to make it easier to test regex strings) referenced in the `Report` of [citation-report](https://github.com/justmars/citation-report); and the `Docket` of [citation-docket](https://github.com/justmars/citation-docket). These two libraries are, in turn, dependencies of [citation-utils](https://github.com/justmars/citation-utils). The `citation-` libraries are intended to parse long-form court decisions and documents that contain Philippine Supreme Court citations.

### Report Regex

:::citation_date.REPORT_DATE_REGEX

### Docket Regex

:::citation_date.DOCKET_DATE_REGEX

#### Group Name: `docket_date`

The regular expression that is constructed will include a group name
(see `(?<docket_date>...)`). This means that `DOCKET_DATE_REGEX` can be combined with
a future regex expression and when the match occurs for the docket date, that match
will be accessible through the group name.

```py
from citation_date import DOCKET_DATE_REGEX
import pprint

pprint.pprint(DOCKET_DATE_REGEX)
(
    "\n"
    "    (?P<docket_date>\n"
    "        \n"
    "(\n"
    "    (\n"
    "    (?:\n"
    "        Jan(?:uary)?|\n"
    "        Feb(?:ruary)?|\n"
    "        Mar(?:ch)?|\n"
    "        Apr(?:il)?|\n"
    "        May|\n"
    "        Jun(?:e)?|\n"
    "        Jul(?:y)?|\n"
    "        Aug(?:ust)?|\n"
    "        Sep(?:tember)?|\n"
    "        Sept|\n"
    "        Oct(?:ober)?|\n"
    "        (Nov|Dec)(?:ember)?\n"
    "    )\n"
    ")\n"
    "\n"
    "    [,\\.\\s]*\n"
    "    \n"
    "    (\n"
    "        ( \n"
    "            ([0]?[1-9])| # 01-09\n"
    "            ([1-2][0-9])| # 10-29\n"
    "            (3[01]) # 30-31\n"
    "        )\n"
    "    )\n"
    "\n"
    "    [,\\.\\s]*\n"
    "    \n"
    "    (\n"
    "        19[0-9][0-9]| # 1900 to 1999\n"
    "        2[0-2][0-9][0-9] # 2000 to 2299\n"
    "    )\n"
    "    \\b # ends with the last digit of the year\n"
    "\n"
    ")\n"
    "|\n"
    "(\n"
    "    \n"
    "    (\n"
    "        ( \n"
    "            ([0]?[1-9])| # 01-09\n"
    "            ([1-2][0-9])| # 10-29\n"
    "            (3[01]) # 30-31\n"
    "        )\n"
    "    )\n"
    "\n"
    "    [,\\.\\s]*\n"
    "    (\n"
    "    (?:\n"
    "        Jan(?:uary)?|\n"
    "        Feb(?:ruary)?|\n"
    "        Mar(?:ch)?|\n"
    "        Apr(?:il)?|\n"
    "        May|\n"
    "        Jun(?:e)?|\n"
    "        Jul(?:y)?|\n"
    "        Aug(?:ust)?|\n"
    "        Sep(?:tember)?|\n"
    "        Sept|\n"
    "        Oct(?:ober)?|\n"
    "        (Nov|Dec)(?:ember)?\n"
    "    )\n"
    ")\n"
    "\n"
    "    [,\\.\\s]*\n"
    "    \n"
    "    (\n"
    "        19[0-9][0-9]| # 1900 to 1999\n"
    "        2[0-2][0-9][0-9] # 2000 to 2299\n"
    "    )\n"
    "    \\b # ends with the last digit of the year\n"
    "\n"
    ")\n"
    "\n"
    "    )\n"
)
```

### Docket Date Format

:::citation_date.DOCKET_DATE_FORMAT

### decode_date()

::: citation_date.decoder.decode_date
