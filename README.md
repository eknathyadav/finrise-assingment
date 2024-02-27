
## API Reference

#### Register User

```http
  POST http://127.0.0.1:8000/feed/user/register/
```

Request Payload :

`{
    "username": "test_user",
    "password": "test_user"
}`

Response Payload : 

`{
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA5MDczNTE5LCJpYXQiOjE3MDkwNzMyMTksImp0aSI6IjcwNjRjZTY3YWVkYzRkODg5ZGE5ZWFiZjI2ZGExYTQ2IiwidXNlcl9pZCI6NX0.II9tkfUWIpU_6a-9za1DhobW5jkizGvfgzgSCn-9ius"
}
`

#### Login User

```http
  POST http://127.0.0.1:8000/feed/user/login/
```

Request Payload :

`{
    "username": "test_user",
    "password": "test_user"
}`

Response Payload : 

`{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcwOTE1OTY5MywiaWF0IjoxNzA5MDczMjkzLCJqdGkiOiIzN2I4NWRkYTI3N2Q0MzUyOTc0MjE0YzFjMjc4MjVjMiIsInVzZXJfaWQiOjR9.aYeFaU0oX_AQ90hCPLFELxvCbeCr75kH0CcFVRQJYg4",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA5MDczNTkzLCJpYXQiOjE3MDkwNzMyOTMsImp0aSI6ImFhN2QyNGYwMDExNjQyYTg4ZDcyOTRmZTRjYzI1MDRmIiwidXNlcl9pZCI6NH0.WCCb7JXvy6wo0UkJUp4yTF79gKePa7MSq4s15jmQN-8"
}
`


#### Websocket subscribe feedback API

```ws
  ws://127.0.0.1:8000/live-feed/subscribe/
```

Headers :

{
    "authorization" : "Bearer Token(will get from above APIs)"
}

Response : 

{"message": "{\"stream\":\"btcusd_perp@bookTicker\",\"data\":{\"u\":867676672061,\"e\":\"bookTicker\",\"s\":\"BTCUSD_PERP\",\"ps\":\"BTCUSD\",\"b\":\"56876.5\",\"B\":\"2634\",\"a\":\"56876.6\",\"A\":\"486\",\"T\":1709072332115,\"E\":1709072332129}}"}

{"message": "{\"stream\":\"btcusd_perp@bookTicker\",\"data\":{\"u\":867676671851,\"e\":\"bookTicker\",\"s\":\"BTCUSD_PERP\",\"ps\":\"BTCUSD\",\"b\":\"56876.5\",\"B\":\"2235\",\"a\":\"56876.6\",\"A\":\"489\",\"T\":1709072332098,\"E\":1709072332105}}"}


## Project Setup 


```
git clone https://github.com/eknathyadav/finrise-assingment.git
```

```
pip install -r requirements.txt
```

```
Run redis server at 6379

For windows please refer to https://riptutorial.com/redis/example/29962/installing-and-running-redis-server-on-windows
```

```
To run the server : 

python manage.py runserver 
```

```
To run the external websocket API in different process
python manage.py tasks 
```
