
## Local Setup
1. Install Node LTS version
2. Install **[Serverless framework](https://www.serverless.com/framework/docs/getting-started)**
```npm -g install serverless```

## Project initialise with preferred language
Here we have two options for building APIs,
1. Python
2. NodeJS

Clone the repository locally and copy the stack you want to start working on.
Do,

```npm install```

Then 

```npm start```

You can then browse,
[http://localhost:3000/dev/hello](http://localhost:3000/dev/hello)

To reload after code changes just type ```rs``` and press enter.

## Add new API resouce

Goto serverless.yml
In the functions section you need to create a new function like below.
```yaml
functions:
    hello:
        handler: handler.hello
        events:
        - http:
            path: /hello
            method: get
            cors: true
    secondfn:
        handler: handler.secondfnname
        events:
        - http:
            path: /anypath
            method: get
            cors: true
```

### Deployment 

Setup **[Docker](https://www.docker.com/get-started)** locally in your development enviornment. 

docker compose up
