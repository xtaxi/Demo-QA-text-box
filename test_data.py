HAPPY_PATH_DATA = {
        "name": "Liviu Manea",
        "email": "alexandrumanea@yhmail.com",
        "cur_addr": "123 Test Street",
        "perm_addr": "456 Permanent Ave"
        }
INVALID_EMAIL_DATA = {
    "name": "Liviu Manea",
    "email": "not-an-email",
    "cur_addr": "Street 1",
    "perm_addr": "Street 2"
}
BOUNDARY_DATA = {
    "name": "Liviu Manea",
    "email": "alexandrumanea@yhmail.com",
    "cur_addr": "Street 1aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" * 30,
    "perm_addr": "Street 2" * 30
}