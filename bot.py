
from urllib.parse import urlparse, parse_qs
from xbox.webapi.authentication.manager import AuthenticationManager
from xbox.webapi.authentication.models import OAuth2TokenResponse
from xbox.webapi.common.signed_session import SignedSession
from xbox.webapi.scripts import CLIENT_ID, CLIENT_SECRET, TOKENS_FILE
import string, random, asyncio
from urllib.parse import urlparse, parse_qs
from aiohttp import web
from urllib.parse import urlparse, parse_qs
client_id = ''
client_secret = ''
tokens_file = TOKENS_FILE
recovery_code = None
valid_characters = list(string.ascii_lowercase+str(123456789))

async def main():
    async with SignedSession() as session:
        auth_mgr = AuthenticationManager(session, client_id, client_secret, "")
        try:
            with open(tokens_file) as f:
                tokens = f.read()
                #print(tokens)
            # Assign gathered tokens
            auth_mgr.oauth = OAuth2TokenResponse.model_validate_json(tokens)
        except:
            print("Something went wrong!")

        async def handle_request(request):
            print('test')
            parsed_url = urlparse(request.path_qs)
            query_params = parse_qs(parsed_url.query)
            if 'code' in query_params:
                code = query_params['code'][0]
                print("Received code:", code)
                tokens = await auth_mgr.request_oauth_token(code)
                if tokens:
                    file_name = f'./accounts/{"".join(random.choices(valid_characters, k=10))}.json'
                    file = open(file_name, 'w+')
                    file.write(tokens.model_dump_json())
            return web.Response(text="Received code")

        app = web.Application()
        app.router.add_get('/', handle_request)
        runner = web.AppRunner(app)
        await runner.setup()
        site = web.TCPSite(runner, 'localhost', 65432)
        await site.start()
        print("Server started")
        while True:
            await asyncio.sleep(1)


if __name__ == "__main__":
    asyncio.run(main())