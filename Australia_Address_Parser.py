#https://au-addr-parser.readthedocs.io/en/latest/
#https://pypi.org/project/au-address-parser/

from au_address_parser import AbAddressUtility
data='PO Box 387 LAKEMBA NSW 2195 AUSTRALIA'
addr = AbAddressUtility(data)
print(addr.parsed_addr)