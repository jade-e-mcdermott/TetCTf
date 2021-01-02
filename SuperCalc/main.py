import requests


# Helper Functions
def InjectedStuffIsTooLong(stringToCheck):
    if (len(stringToCheck) > 70):
        return True
    else:
        return False

def TryInjectedPayload(injectedPayload):
    baseUrl = "http://139.180.155.171?calc="
    fullRequest = baseUrl + injectedPayload
    if(InjectedStuffIsTooLong(injectedPayload) == False):
        response = requests.get(fullRequest)
        print("Stats: ", response.status_code)
        return response.text
    else:
        return "Injected payload too long."

def TryInjectedPayloadOnLocal(injectedPayload):
    baseUrl = "http://localhost:8081?calc="
    fullRequest = baseUrl + injectedPayload
    if(InjectedStuffIsTooLong(injectedPayload) == False):
        response = requests.get(fullRequest)
        print("Stats: ", response.status_code)
        return response.text
    else:
        return "Injected payload too long."

# Working Hax




# Main
injectedPayload = "%270%274"
results = TryInjectedPayloadOnLocal(injectedPayload)
print(results)

