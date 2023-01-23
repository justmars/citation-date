---
hide:
- navigation
---
# Citation Date

## Concept

This is a dependency: a regex date formula and decoder for dates referenced in [citation-report](https://github.com/justmars/citation-report); and [citation-docket](https://github.com/justmars/citation-docket). These two libraries are, in turn, dependencies of [citation-utils](https://github.com/justmars/citation-utils). The `citation-` libraries are intended to parse long-form court decisions and documents that contain Philippine Supreme Court citations.

## Dependency

This is a separate library to make it easier to test regex strings.

### Report

:::citation_date.decoder.report_date

### Docket

:::citation_date.decoder.docket_date

## Regex

The intended purpose for this more customized date string matching in Philippine citations is to:

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

This `regex` string is constructed via the python variable `docket_date`; note
that it has the same group name in the regex expression identified by
`(?<docket_date>...)`

```py
from citation_date import docket_date
import pprint

pprint.pprint(docket_date)
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

## decode_date() helper

::: citation_date.decoder.decode_date
