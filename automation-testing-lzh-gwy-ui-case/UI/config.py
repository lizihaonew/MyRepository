PAGE_LOAD_WAIT_TIMEOUT = 10
TEST_SERVER_ADDRESS = {
    'web':
        {
            'wbs': 'http://192.168.0.222',
            'insurance': 'http://192.168.0.212:809',
            'fof': 'http://192.168.0.222:91',
            'gwy': 'http://192.168.0.212:808'
         },
    'app':
        {
            'wbs': 'http://192.168.0.222:82',
        }
}
ELEMENT_WAIT_TIMEOUT = 10

dict_data = {
    'wbs': {
        'Storage': 'userData',
        'LOGIN_API_ENDPOINT': '/api/saas/login.json',
        'DATA': 'data={"param":{"password":"6846860684f05029abccc09a53cd66f1","mobile":"18888888888"},"sign":"39cd118a9903b9948329b4c6ea2daff9"}',
        'HEADER': {'Content-Type': 'application/x-www-form-urlencoded'}
    },
    'insurance': {
        'Storage': '',
        'LOGIN_API_ENDPOINT': '',
        'DATA': '',
        'HEADER': {}
    },
    'fof': {
        'Storage': '',
        'LOGIN_API_ENDPOINT': '',
        'DATA': '',
        'HEADER': {}
    },
    'gwy': {
        'Storage': 'token',
        'LOGIN_API_ENDPOINT': '/api/gwy/user/login.json',
        'DATA': 'data={"param":{"mobile":"18800080008","password":"96e79218965eb72c92a549dd5a330112"},"sign":"2b78538442997ea1b47eda413c91bf95"}',
        'HEADER': {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
    }

}

