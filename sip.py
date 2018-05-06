import sys
import sip_parser

sipParser = sip_parser.getparser()
while True:
    gra = input('SIP >>')
    sipParser.parse(gra)


