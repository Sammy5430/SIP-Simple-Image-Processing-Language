import sys
import sip_parser

sipParser = sip_parser.getparser()
while True:
    gra = input('SIP >>')
    # gra = input('img{'
    #             'translate(100,10)'
    #             'rotate(right)')
    sipParser.parse(gra)


