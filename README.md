# WorkedLogJira
Get worked log from Jira in a human way.

### Replace with your Jira endpoint
On line 15 change with your jira api endpoint

```
 'server': 'https://tracker.yourdomain.com:9000/'
```
### Replace your username and password with Jira's one:
Have a look at line 11 in work.py, and change with your username/password.
```
credentials = (username, 'password')
```

### Build Dockerfile
```
docker build . -t workedlog
```

### Run image as executable with:
```
docker run -it workedlog
```

### The result will be:
```
Developer: username
Ticket Amount: 12
Original Estimates: 22.5h
Logged Hours: 19.25h
Focus Factor: 100.883116883%
Tickets:
NNEO-9999
...
```