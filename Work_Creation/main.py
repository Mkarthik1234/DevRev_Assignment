# !! In order to run this user must have a part in his dev org
import requests
import json

DOI = "don:identity:dvrv-us-1:devo/1RKdIsrHqq:devu/1"

workurl = 'https://api.devrev.ai/works.create'

workheaders = {
    'Authorization':'eyJhbGciOiJSUzI1NiIsImlzcyI6Imh0dHBzOi8vYXV0aC10b2tlbi5kZXZyZXYuYWkvIiwia2lkIjoic3RzX2tpZF9yc2EiLCJ0eXAiOiJKV1QifQ.eyJhdWQiOlsiamFudXMiXSwiYXpwIjoiZG9uOmlkZW50aXR5OmR2cnYtdXMtMTpkZXZvLzFSS2RJc3JIcXE6ZGV2dS8xIiwiZXhwIjoxODEwNDY0MTkwLCJodHRwOi8vZGV2cmV2LmFpL2F1dGgwX3VpZCI6ImRvbjppZGVudGl0eTpkdnJ2LXVzLTE6ZGV2by9zdXBlcjphdXRoMF91c2VyL2dvb2dsZS1vYXV0aDJ8MTE0MjQ1NDMwNzQ2NTMyNTc0ODE1IiwiaHR0cDovL2RldnJldi5haS9hdXRoMF91c2VyX2lkIjoiZ29vZ2xlLW9hdXRoMnwxMTQyNDU0MzA3NDY1MzI1NzQ4MTUiLCJodHRwOi8vZGV2cmV2LmFpL2Rldm9fZG9uIjoiZG9uOmlkZW50aXR5OmR2cnYtdXMtMTpkZXZvLzFSS2RJc3JIcXEiLCJodHRwOi8vZGV2cmV2LmFpL2Rldm9pZCI6IkRFVi0xUktkSXNySHFxIiwiaHR0cDovL2RldnJldi5haS9kZXZ1aWQiOiJERVZVLTEiLCJodHRwOi8vZGV2cmV2LmFpL2Rpc3BsYXluYW1lIjoia2FydGhpayIsImh0dHA6Ly9kZXZyZXYuYWkvZW1haWwiOiI0bm0yMGNtMDE3QG5tYW1pdC5pbiIsImh0dHA6Ly9kZXZyZXYuYWkvZnVsbG5hbWUiOiJNIEtBUlRISUsiLCJodHRwOi8vZGV2cmV2LmFpL2lzX3ZlcmlmaWVkIjp0cnVlLCJodHRwOi8vZGV2cmV2LmFpL3Rva2VudHlwZSI6InVybjpkZXZyZXY6cGFyYW1zOm9hdXRoOnRva2VuLXR5cGU6cGF0IiwiaWF0IjoxNzE1ODU2MTkwLCJpc3MiOiJodHRwczovL2F1dGgtdG9rZW4uZGV2cmV2LmFpLyIsImp0aSI6ImRvbjppZGVudGl0eTpkdnJ2LXVzLTE6ZGV2by8xUktkSXNySHFxOnRva2VuLzh4c0RnUmxTIiwib3JnX2lkIjoib3JnXzlJM1FBaTVLeWlFazJ2aXQiLCJzdWIiOiJkb246aWRlbnRpdHk6ZHZydi11cy0xOmRldm8vMVJLZElzckhxcTpkZXZ1LzEifQ.iD0IsPqNu_thKlreB5SLwwiVk5MOL0z9LkOFFy4vCaSyhcnVUZIy8YQrCXZ4hNT433VfWfJUUMp2wRDLyP_khVlHp7uSmxOcdzSrYxYSVjZBLIxaErA9JxMJBvFASuMIRCO19183YEXHKxSv5o22cXWjNGE-nERB0iYF7VKsfi_izLN0giHYmdLVBQxyzDH9Hwd6vOVHtFZ0QGH58jY2My_PktJcGCgRq3wrrYB4SyXJm_WabPDZ_ZIAdqL5SXCV8XF2w-7FpjjS4xrgCKjB0MH-p5UijK5h4QXEafU_WM5nhGHSnYWWOK2sz0lxGaD5_Y2WQbQlYKZM7re4RKuCCw',
    "Content-Type": "application/json"
}

partURL = f"https://api.devrev.ai/parts.list?created_by={DOI}"

partheaders = {
    'Authorization': 'eyJhbGciOiJSUzI1NiIsImlzcyI6Imh0dHBzOi8vYXV0aC10b2tlbi5kZXZyZXYuYWkvIiwia2lkIjoic3RzX2tpZF9yc2EiLCJ0eXAiOiJKV1QifQ.eyJhdWQiOlsiamFudXMiXSwiYXpwIjoiZG9uOmlkZW50aXR5OmR2cnYtdXMtMTpkZXZvLzFSS2RJc3JIcXE6ZGV2dS8xIiwiZXhwIjoxODEwNDY0MTkwLCJodHRwOi8vZGV2cmV2LmFpL2F1dGgwX3VpZCI6ImRvbjppZGVudGl0eTpkdnJ2LXVzLTE6ZGV2by9zdXBlcjphdXRoMF91c2VyL2dvb2dsZS1vYXV0aDJ8MTE0MjQ1NDMwNzQ2NTMyNTc0ODE1IiwiaHR0cDovL2RldnJldi5haS9hdXRoMF91c2VyX2lkIjoiZ29vZ2xlLW9hdXRoMnwxMTQyNDU0MzA3NDY1MzI1NzQ4MTUiLCJodHRwOi8vZGV2cmV2LmFpL2Rldm9fZG9uIjoiZG9uOmlkZW50aXR5OmR2cnYtdXMtMTpkZXZvLzFSS2RJc3JIcXEiLCJodHRwOi8vZGV2cmV2LmFpL2Rldm9pZCI6IkRFVi0xUktkSXNySHFxIiwiaHR0cDovL2RldnJldi5haS9kZXZ1aWQiOiJERVZVLTEiLCJodHRwOi8vZGV2cmV2LmFpL2Rpc3BsYXluYW1lIjoia2FydGhpayIsImh0dHA6Ly9kZXZyZXYuYWkvZW1haWwiOiI0bm0yMGNtMDE3QG5tYW1pdC5pbiIsImh0dHA6Ly9kZXZyZXYuYWkvZnVsbG5hbWUiOiJNIEtBUlRISUsiLCJodHRwOi8vZGV2cmV2LmFpL2lzX3ZlcmlmaWVkIjp0cnVlLCJodHRwOi8vZGV2cmV2LmFpL3Rva2VudHlwZSI6InVybjpkZXZyZXY6cGFyYW1zOm9hdXRoOnRva2VuLXR5cGU6cGF0IiwiaWF0IjoxNzE1ODU2MTkwLCJpc3MiOiJodHRwczovL2F1dGgtdG9rZW4uZGV2cmV2LmFpLyIsImp0aSI6ImRvbjppZGVudGl0eTpkdnJ2LXVzLTE6ZGV2by8xUktkSXNySHFxOnRva2VuLzh4c0RnUmxTIiwib3JnX2lkIjoib3JnXzlJM1FBaTVLeWlFazJ2aXQiLCJzdWIiOiJkb246aWRlbnRpdHk6ZHZydi11cy0xOmRldm8vMVJLZElzckhxcTpkZXZ1LzEifQ.iD0IsPqNu_thKlreB5SLwwiVk5MOL0z9LkOFFy4vCaSyhcnVUZIy8YQrCXZ4hNT433VfWfJUUMp2wRDLyP_khVlHp7uSmxOcdzSrYxYSVjZBLIxaErA9JxMJBvFASuMIRCO19183YEXHKxSv5o22cXWjNGE-nERB0iYF7VKsfi_izLN0giHYmdLVBQxyzDH9Hwd6vOVHtFZ0QGH58jY2My_PktJcGCgRq3wrrYB4SyXJm_WabPDZ_ZIAdqL5SXCV8XF2w-7FpjjS4xrgCKjB0MH-p5UijK5h4QXEafU_WM5nhGHSnYWWOK2sz0lxGaD5_Y2WQbQlYKZM7re4RKuCCw'
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
            print("No parts found")
            
else:
    print(f"Failed to retrieve parts data Status code: {response.status_code}")
    print(response.text)
