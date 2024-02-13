def bill_formating(bill):
    bill = bill.replace("R$","")
    bill = bill.replace("$","")

    return float(bill)


def tip_calculator(bill, tip_rate):
    tip_rate = tip_rate.replace("%","")
    tip_rate = float(tip_rate)
    
    if tip_rate<1:
        return bill * tip_rate
    
    else:
        return bill * (tip_rate/100)