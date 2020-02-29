# all_links : Get all links of a website

The all_links CLI let you get all links of a given website.
The output can be generated in three ways: to JSON, to XML or printed to from terminal (stdout).

## Positional arguments

url                  The website URL (ex: https://reachip.github.io)
output               Output : xml - json - stdout

## Optional arguments

-h, --help           display help message
--filename FILENAME  output filename if you want to generate a JSON or XML format 

## Installation

### Just with pip

```
pip install --user lxml beautifulsoup4 requests
```