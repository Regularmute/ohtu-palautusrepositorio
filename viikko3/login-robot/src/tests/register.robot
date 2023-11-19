*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  Kalevi  Kalevi333
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  jaakko  abcabc1
    Output Should Contain  User with username jaakko already exists

Register With Too Short Username And Valid Password
# ...

Register With Enough Long But Invalid Username And Valid Password
# ...

Register With Valid Username And Too Short Password
# ...

Register With Valid Username And Long Enough Password Containing Only Letters
# ...

*** Keywords ***
Create User And Input New Command
    Create User  jaakko  jaakko123
    Input New Command
