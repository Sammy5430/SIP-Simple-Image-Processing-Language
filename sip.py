import sys
import sip_parser

sipParser = sip_parser.getparser()
while True:
    try:
        parse_in = input('SIP >>')
        sipParser.parse(parse_in)
    except EOFError:
        break



