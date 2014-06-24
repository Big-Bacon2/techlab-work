# author: Big-Bacon2
if country == "US":
    if total <= "50":
        print "Shipping Costs $6.00"
    elif total <= "100":
            print "Shipping Costs $9.00"
    elif total <= "150":
            print "Shipping Costs $12.00"
    else:
        print "FREE"

if country == "Canada":
    if total <= "50":
        print "Shipping Costs $8.00"
    elif total <= "100":
        print "Shipping Costs $12.00"
    elif total <= "150":
        print "Shipping Costs $15.00"
    else:
        print "FREE"