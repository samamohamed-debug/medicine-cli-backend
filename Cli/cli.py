import requests 
import argparse

BASE_URL= "http://127.0.0.1:8000"

def list_medicines():
    response = requests.get(
        f"{BASE_URL}/medicines"
    )
    
    medicines= response.json()
    
    for med in medicines:
        print(
            f"ID: {med['id']} |"
            f"Name: {med['name']} |" 
            f"Price: {med['price']}"
        )
        
def add_medicine(name , price):
    response=requests.post(
        f"{BASE_URL}/medicines",
        json={"name":name , "price":price}
    )
    print(response.json())
    
    
def delete_medicine(med_id):
    response=requests.delete(f"{BASE_URL}/medicines/{med_id}")
    if response.status_code==204:
        print("Deleted successfully")
    else:
        print("Error" ,response.text)

def main():
    parser= argparse.ArgumentParser()
    subparsers=parser.add_subparsers(dest="command")
    
    subparsers.add_parser("list")
    add_parser=subparsers.add_parser("add")
    add_parser.add_argument("name")
    add_parser.add_argument("price",type=float)
    
    delete_parser=subparsers.add_parser("delete")
    delete_parser.add_argument("id", type=int)
    
    args=parser.parse_args()
    if args.command== "list":
        list_medicines()
    elif args.command == "add":
        add_medicine(args.name,args.price)
    elif args.command == "delete":
        delete_medicine(args.id)
        
if __name__ =="__main__":
    main()