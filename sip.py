import sys
import sip_parser

sipParser = sip_parser.getparser()
gra = input('SIP>')

sipParser.parse(gra)

