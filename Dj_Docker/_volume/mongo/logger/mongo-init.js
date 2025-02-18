db = db.getSiblingDB('admin');
// log as root admin if you decided to authenticate in your docker-compose file
db.auth("root", "root");
// create database
db = db.getgetSiblingDB('logger');
//create user
db.createUser({
    'user': "user",
    'pwd': "user",
    'roles': [{
        'role': 'dbOwner',
        'db': 'logger'}]});

// First collection required for mongo init.
db.createCollection('init');