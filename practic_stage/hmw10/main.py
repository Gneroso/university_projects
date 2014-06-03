from watchers import Writer, Caller
from agency import Agency


agency = Agency("OpeN AgencY")

Writer({
    'booked_phone': agency.booked_phone,
    'booked_cash': agency.booked_cash,
    'tickets': agency.tickets,
    'sold': agency.sold
}).watch(10)

Caller({
    'booked_phone': agency.booked_phone,
    'tickets': agency.tickets
}).watch(6 * 60 * 60)

agency.open()
