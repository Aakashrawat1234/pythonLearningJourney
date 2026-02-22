import requests

# params={
 #   "name":"Mike",
  #  "age":25
# }
#payload={
 #   "name":"Mike",
 #   "age":25
#}

# response=requests.get("https://httpbin.org/get",params=params)
# print(response.url)
# res_json=print(response.json())


# response=requests.post("https://httpbin.org/post",data=payload)
# print(response.url)
# res_json=print(response.json())



response=requests.get("https://httpbin.org/status/200")
if response.status_code==requests.codes.not_found:
        print("Not found")
else:      
        print(response.status_code)


headers={
        "User_Agent":"HelloWorld/1.1"
}
response=requests.get("https://httpbin.org/user-agent",headers=headers
                      )
print(response.text)