# The Late Show Api

A Restful API for managing a late night show that comprises of guests, episodes, appearances and user authentification built using flask, sqlalchemy, postgresql and jwt authentification

---

## Feautures

```

- Organised with MVC structure
- JWT based authentification
- Relational models with sqlalchemy
- Database migration with flask migrate
- Faker data seeding
- CRUD operations for:
  - Guests
  - Appearances
  - Episodes

```

---

## Tech Used

- Python 3.8+
- Flask
- Flask-Migrate
- SQLAlchemy
- PostgresSQL
- Flask-JWT-Extended
- Faker
- Pipenv
---

## Project structure
```

|
|──────── Server/
|   |────app.py
|   |────config.py
|   |────seed.py
|   |────moddels
|   |   |──appearance.py
|   |   |──episode.py
|   |   |──guest.py
|   |   |──user.py
|   |──── controllers
|       |──appearance_controller.py
|       |──auth_controller.py
|       |──episode_controller.py
|       |──guest_controller.py
|
|──────migrations
|──────.env
|──────pipfile
|──────README.md
|──────

```
---

# Set up Instructions


1. clone and set up


- bash
git clone https://github.com/username/late-show-api.git
cd late-show-api
pipenv install

2. Activate virtual environment

pipenv shell

3. Create .env

```
touch .env

paste the following
DATABASE_URL=postgresql://late_show_user:1234@localhost:5432/late_show_db
SECRET_KEY=supersecretkey
JWT_SECRET_KEY=superjwtsecret

```

4. Set up Database

```
bash

createdb late_show_db
psql -c "GRANT ALL PRIVILEGES ON DATABASE late_show_db TO late_show_user;"

```
or enter the postgresql shell and run

```
sql

GRANT ALL PRIVILEGES ON DATABASE late_show_db TO late_show_user:
\c late_show_db
GRANT ALL ON SCHEMA public TO late_show_user;
```

5. Migration and seeding

```
bash

export FLASK_APP=server/app.py

*Initialize migrations - run only once*
flask db init

*Generate migration*
flask db migrate -m "Initial Migration"

*Apply migration*
flask db upgrade

*seed data*
python -m server.seed
```

---

# Testing API's with postman

```
1. /register -register a user

- method: POST
- URL: http://127.0.0.1:5000/register
- Headers:
    - content-type: application/json
- Body(raw - json)
    {
      "username":"user1",
      "password":"userpassword"
    }
- Expected results HTTP 201 created or(200), user registered

```
```
2. /login

- method: POST
- URL: http://127.0.0.1:5000/login
- Headers:
    - content-type: application/json
- Body(raw - json)
    {
      "username":"user1",
      "password":"userpassword"
    }
- Expected results
        {
          "access_token: "weoejdbdndksisjssbsbsnsn..."
        }
    - copy the token

```  
```
3. /episodes/<id>

- method: DELETE
- URL: http://127.0.0.1:5000/episodes/1
- Headers:
    - content-type: application/json
    - authorization: Bearer token here...
```

```
4. /appearances

- method: POST
- URL: http://127.0.0.1:5000/appearances
- Headers:
    - content-type: application/json

  - sending token in protected areas
    - authorization: Bearer token here....
- Body(raw - json)
    {
      "guest_id": 1,
      "episode_id": 1,
      "rating": 8.5
    }
```