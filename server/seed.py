from faker import Faker
from random import randint, choice
from server.app import app, db
from server.models.guest import Guest
from server.models.episode import Episode
from server.models.appearance import Appearance
from server.models.user import User


fake = Faker()


def seed():
    with app.app_context():

        print("clearing old data")

        db.session.query(Appearance).delete()
        db.session.query(Guest).delete()
        db.session.query(Episode).delete()
        db.session.query(User).delete()
        db.session.commit()



        print("seeding default users")

        user = User(username="admin")
        user.password = "password"
        db.session.add(user)



        print("seeding guests")
        core_guests = [

            Guest(name="Ngugi wa Thiongo", occupation="Writer"),
            Guest(name="Sylvester Stallone", occupation="Actor"),
            Guest(name="Bob Marley", occupation="Musician"),
            Guest(name="Soprano Kindiki", occupation="Wantam"),
            Guest(name="Mike Tyson", occupation="Boxer")
        ]
        db.session.add_all(core_guests)


        print("creating random guests")
        #generate 7 random guests with faker
        random_guests = []
        for _ in range(7):
            guest = Guest(
                name=fake.name(),
                occupation=fake.job()
            )
            random_guests.append(guest)

        #add all random guests to the session
        db.session.add_all(random_guests)
        #merge both static and random guests
        all_guests = core_guests + random_guests


        print("creating episodes")
        #create 5 fixed episodes with dates
        episodes = [
            Episode(date="2024-06-01", number=1),
            Episode(date="2024-06-02", number=2),
            Episode(date="2024-06-03", number=3),
            Episode(date="2024-06-04", number=4),
            Episode(date="2024-06-05", number=6)
        ]

        #generate 5 additional episodes with random dates
        for i in range(5):
            episodes.append(
                Episode(
                    date=str(fake.date_between(start_date="-2y", end_date="today")), number=5 + i #continue numbering
                    
                )
            )
        #add all episodes to the database and flush to get assigned ids
        db.session.add_all(episodes)
        db.session.flush()



        print("creating appearances")
        #create some fixed appearances for the core guests
        appearances = [
                Appearance(rating=5, guest_id=core_guests[0].id, episode_id=episodes[0].id),
                Appearance(rating=4, guest_id=core_guests[1].id, episode_id=episodes[0].id),
                Appearance(rating=3, guest_id=core_guests[2].id, episode_id=episodes[1].id)

            ]
        #add 10 random appearances from any guest in any episode
        for _ in range(10):
                appearances.append(
                    Appearance(
                        rating=randint(1,5), #random ration btwn 1 and 5
                        guest_id=choice(all_guests).id,
                        episode_id=choice(episodes).id
                    )
                )
        #save all appearances to the db
        db.session.add_all(appearances)
        db.session.commit()
        print("done seeding with core and faker")
     
# run seed function if file is executed directly
if __name__ == "__main__":
    seed()