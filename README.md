# Fiscal server

# First steps
```
Add vars.env in directory with Dockerfile
Add settings.py in directory fiscal
```

# Start docker-compose
`docker-compose up -d --build`

# db connection
```
docker-compose exec db /bin/bash
psql -U <db_user> -p <db_name>
```

# web_server connection
`docker-compose exec web_server /bin/bash`

# test user requests
```
docker-compose exec web_server /bin/bash
cd fiscal/user_calls
python cashbox_post.py
python trip_post.py
```
