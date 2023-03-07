# interview-uptrader

## Setup

1. Clone repository

```shell
$ git clone https://github.com/xp-rodion/interview-bolid
```

2. Configure environment:
    1. Copy example environment preset and open its:
    ```console
    $ cp .env.example .env && vim .env
    ```
    2. Configurate DB connection for local db or use default values for docker running:
   ```text
   POSTGRES_USER=
   POSTGRES_PASSWORD=
   POSTGRES_HOST=
   POSTGRES_PORT=
   POSTGRES_DB=
   
   SERVER_HOST=
   SERVER_PORT=
   ```
   
3. Run server:
   1. 
      Inside container:
      ```console
      $ docker-compose up -d --build
      ```
      
## Description
In the admin panel, you can configure sensor and events. Also all possible urls for api are registered in the swagger.