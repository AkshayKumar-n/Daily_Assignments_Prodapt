def validate(cusdict):
        valname=re.search("[A-Z]{1}[^A-Z]{0,25}$",cusdict["customername"])
        valid=re.search("[0-9]$",cusdict["customerid"])
        valamount=re.search("[0-9]$",cusdict["amount"])
        if valname and valid and valamount:
            return True
        else:
            return False