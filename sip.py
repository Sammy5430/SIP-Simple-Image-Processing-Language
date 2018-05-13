import sys
import sip_parser

sipParser = sip_parser.getparser()
while True:
    parse_in = input('SIP >>')
    sipParser.parse(parse_in)
    intensity = {'HIGH': 1, 'MEDIUM': 3, "LOW": 6}


