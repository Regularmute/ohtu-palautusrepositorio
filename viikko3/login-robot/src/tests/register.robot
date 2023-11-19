*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input New Command
    Input Credentials  Kalevi  Kalevi333
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
# ...

Register With Too Short Username And Valid Password
# ...

Register With Enough Long But Invalid Username And Valid Password
# ...

Register With Valid Username And Too Short Password
# ...

Register With Valid Username And Long Enough Password Containing Only Letters
# ...

*** Keywords ***
Input New Command And Create User
    Input New Command
    Create User  jaakko  jaakko123
