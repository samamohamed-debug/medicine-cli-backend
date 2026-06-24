import requests 
import argparse
import sys

BASE_URL= "http://127.0.0.1:8000"

def list_medicines():
    try:
        response=requests.get(f"{BASE_URL}/medicines")
        for med in response.json():
            print(f"ID: {med['id']} | Name: {med['name']} | Price: {med['price']} | In Stock: {med.get('in_stock', True)}")
    except: print("Error: Server is down.")
        
def add_medicine(name , price, in_stock, quantity):
    try:
        response = requests.post(f"{BASE_URL}/medicines", json={"name": name, "price": price, "in_stock": in_stock})
        print(response.json())
    except: print("Error: Server is down.")
    
    
def delete_medicine(med_id):
    try:
        response = requests.delete(f"{BASE_URL}/medicines/{med_id}")
        print("Deleted successfully" if response.status_code == 204 else f"Error: {response.text}")
    except: print("Error: Server is down.")
    
class CustomArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        print("Error : Invalid or Missing Command")
        print("-- How to use this program --")
        print("1. To view medicines : python cli.py list")
        print("2. To add mediciens : python cli.py [name] [price]")
        print("3. To delete mediciens : python cli.py [id]")
        sys.exit(2)

def main():
    parser= CustomArgumentParser(description="Medicine Management CLI - Easily list, add, or delete medicines.")
    subparsers=parser.add_subparsers(dest="command", parser_class=CustomArgumentParser)
    
    subparsers.add_parser("list")
    add_parser=subparsers.add_parser("add")
    add_parser.add_argument("name")
    add_parser.add_argument("price",type=float)
    add_parser.add_argument("in_stock", type=str) 
    
    delete_parser=subparsers.add_parser("delete")
    delete_parser.add_argument("id", type=int)
    
    args=parser.parse_args()
    
    if args.command is None:
        parser.error("")
     
    if args.command== "list":
        list_medicines()
    elif args.command == "add":
        is_available = args.in_stock.lower() == "true"
        add_medicine(args.name, args.price, is_available)
    elif args.command == "delete":
        delete_medicine(args.id)
        
if __name__ =="__main__":
    main()