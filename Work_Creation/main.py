# !! In order to run this user must have a part in his dev org
import requests
import json

DOI = "<YOUR ID>" 

workurl = 'https://api.devrev.ai/works.create'

workheaders = {
    'Authorization': '<YOUR PAT here>'
    "Content-Type": "application/json"
}

partURL = f"https://api.devrev.ai/parts.list?created_by={DOI}"

partheaders = {
    'Authorization': '<YOUR PAT>'
}

response = requests.get(partURL, headers=partheaders) #to get all the existing parts in the perticular DOI

#if success then show the user list of parts
if response.status_code == 200:
        parts_data = response.json()
        parts = parts_data.get('parts', [])
        if parts:
            print("Select one part : \n")
            i = 1
            #list the parts created
            for part in parts:
                print(f"{i}. {part['name']}",end="\n")
                i+=1
            
            selected_part = int(input()) #ask the user to select a perticular part by its number
            
            print("what you want to crate \n1. issue 2. token\n")
            selected_work = int(input()) #Can create issue or ticket
            
            work_name = input("Enter the work name : ") #user input for work name
            
            if(selected_work == 1): # if issue need to be created
                data = {
                    "type": "issue",
                    "applies_to_part": parts[selected_part-1]['id'],
                    "owned_by": ["don:identity:dvrv-us-1:devo/1RKdIsrHqq:devu/1"],
                    "title": work_name
                }
            elif selected_work == 2: #if ticket need to be created
                data = {
                    "type": "ticket",
                    "applies_to_part": parts[selected_part-1]['id'],
                    "owned_by": ["don:identity:dvrv-us-1:devo/1RKdIsrHqq:devu/1"],
                    "title": work_name
                }
            else:
                print("invalid input")
                exit(0)
                
            response = requests.post(workurl,headers=workheaders,json=data) #create the issue or ticket
            
            if(response.status_code == 200 or response.status_code == 201):
                print("Succesfully created an work")
            else:
                print(response.status_code)
        else:
            print("No parts found now")
            
            
else:
    print(f"Failed to retrieve parts data Status code: {response.status_code}")
    print(response.text)
