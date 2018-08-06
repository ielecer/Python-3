import whois

data = raw_input("Enter a domain:")
w = whois.whois(data)
print w
# print w.expiration_date
# print w.text