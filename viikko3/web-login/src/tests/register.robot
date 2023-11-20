*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go And Check Register Page
Test Teardown  Reset Application

*** Test Cases ***
Register With Valid Username And Password
    Set Username  ville
    Set Password  ville123
    Set Password Confirmation  ville123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  Ve
    Set Password  ville123
    Set Password Confirmation  ville123
    Submit Credentials
    Register Should Fail With Message  Username must be at least 3 characters long

Register With Valid Username And Invalid Password
# salasana ei sisällä halutunlaisia merkkejä
    Set Username  ville
    Set Password  villevii
    Set Password Confirmation  villevii
    Submit Credentials
    Register Should Fail With Message  Password must contain non-letter characters

Register With Nonmatching Password And Password Confirmation
    Set Username  ville
    Set Password  ville123
    Set Password Confirmation  Ville123
    Submit Credentials
    Register Should Fail With Message  Passwords do not match

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Go And Check Register Page
    Go To Register Page
    Register Page Should Be Open
