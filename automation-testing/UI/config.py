PAGE_LOAD_WAIT_TIMEOUT = 10
TEST_SERVER_ADDRESS = {
    'web':
        {
            'wbs': 'http://192.168.0.222',
            'insurance': 'http://192.168.0.212:809',
            'fof': 'http://192.168.0.222:81'
         },
    'app':
        {
            'wbs': 'http://192.168.0.222:82',
        }


}
ELEMENT_WAIT_TIMEOUT = 10


DATA = 'data={"param":{"password":"6846860684f05029abccc09a53cd66f1","mobile":"18888888888"},' \
       '"sign":"39cd118a9903b9948329b4c6ea2daff9"}'

HEADER = {
    'Content-Type': 'application/x-www-form-urlencoded'
}
LOGIN_API_ENDPOINT = '/api/saas/login.json'

