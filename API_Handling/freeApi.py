import requests

url = "https://api.freeapi.app/api/v1/public/randomjokes?limit=10&query=science&inc=categories%2Cid%2Ccontent&page=1"
response = requests.get(url)
getdata = response.json()
user_data = getdata["data"]

def giveUsList(user_data):
    return user_data["data"]

myList = giveUsList()

def giveUsDict(myList):
   for i in range(len(myList)):
       return myList[i]

myDict = giveUsDict()

def giveUsJoke(myDict):
    return myDict["content"]

def fetch_random_jocks():
    if getdata["success"] and "data" in getdata:
        return giveUsJoke()
    else:
        raise Exception("Failed to fetch user data")


def main():
    try:
        requiredData  = fetch_random_jocks()
        print(requiredData)

    except:
        print("Exception Handled")

if __name__ == "__main__":
    main()