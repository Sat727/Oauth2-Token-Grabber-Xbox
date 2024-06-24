# Oauth2-Token-Grabber-Xbox

I initially started this project for a client who ended up cancelling the commission after completion.

Here's a guide on how to setup, and use the bot

 ## Dependencies

- Python >= 3.7
- Discord.py
- Aiohttp
- xbox-webapi-python

Authentication

This project uses Xbox API. 

## Xbox API


Authentication is supported via OAuth2.

- Register a new application in [Azure AD](https://portal.azure.com/#blade/Microsoft_AAD_RegisteredApps/ApplicationsListBlade)
  - Name your app
  - Select "Personal Microsoft accounts only" under supported account types
  - Add <http://localhost:65432> as a Redirect URI of type "Web"
  - Copy your Application (client) ID for later use
  - On the App Page, navigate to "Certificates & secrets"
  - Generate a new client secret and save for later use

## bot.py

```py
    client_id = '' # Enter Azure Client ID here
    client_secret = '' # Enter Azure Secret here
```
After you have done these steps, you will need to generate a tokens.json file.

## Finalization

After you have completed all steps, your python script is ready to listen for traffic coming into localhost:65432. After the script has detected traffic containing a 'code' parameter, the bot will check the validity, and request authorization tokens from Xbox for the account.

This is intended to use in tandem with xbox-web-api. (Please check out their github and documentaion if you don't understand the use-case for this application)

## Contribute

- Feel free to make suggestions
- Feel free to report bugs


