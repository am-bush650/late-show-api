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

6. Testing

use postman or curl to test endpoints