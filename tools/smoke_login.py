import sys
sys.path.insert(0, r'C:\Users\Administrator\Downloads\GEMAO-FLASK')
from MyFlaskapp import create_app

def run():
    app = create_app()
    client = app.test_client()

    # Test valid user credentials
    resp = client.post('/login', data={'username':'user','password':'user_password'}, follow_redirects=True)
    print('Valid user login status:', resp.status_code)
    print('Location after valid user login (first 200 chars):')
    print(resp.get_data(as_text=True)[:200])

    # Test invalid credentials
    resp2 = client.post('/login', data={'username':'bad','password':'x'}, follow_redirects=True)
    print('\nInvalid login status:', resp2.status_code)
    print('Invalid login page snippet:')
    print(resp2.get_data(as_text=True)[:200])

if __name__ == '__main__':
    run()
