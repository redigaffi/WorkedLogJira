# WorkedLogJira
Get worked log from Jira in a human way.


##### Build Dockerfile
```
docker build . -t workedlog
```

##### Preparing .env file
Rename the .env.sample to .env and replace with your Jira credentials/endpoint.


##### Run image as executable with:
```
docker run --env-file .env -it workedlog
```

##### The result will be:
```
Developer: username
Ticket Amount: 12
Original Estimates: 22.5h
Logged Hours: 19.25h
Focus Factor: 100.883116883%
Tickets:
CODE-9999
...
```