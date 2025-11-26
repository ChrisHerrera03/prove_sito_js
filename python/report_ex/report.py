import csv
import json
def generate_report(csvpath,jsonpath):
    items = {}
    try:
        with open(csvpath,newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for line in reader:
                items[line['name']] = float(line['price'])
    except:
        return "Errore riscontrato nell'apertura del CSV"
    with open(jsonpath) as jsonfile:
        data = json.load(jsonfile)
        tax = data["tax"]
        for key,value in items.items():
            price_with_tax = value * tax / 100
            value += price_with_tax
            items[key] = value

    with open("report.csv","w",newline='') as report:
        writer = csv.DictWriter(report,['name','price'])
        writer.writeheader()
        for name, price in items.items():
            writer.writerow({
                'name':name,
                'price':price
            })
    return items
    

print(generate_report("items.csv","setting.json"))
        