from main import Session, Users, Auditorium, Booking

session = Session()

user = Users(uid=1, email="yaroslav@gmail.com", password="1234", name = "Yaroslav")
auditorium1 = Auditorium(uid=1, number="123")
auditorium2 = Auditorium(uid=2, number="214")

booking = Booking(uid=1, from_user=user, from_auditorium=auditorium1, auditorium_status="Locked", booking_date_start="12.12.2020", booking_date_final="15.12.2020")

session.add(user)
session.add(auditorium1)
session.add(auditorium2)
session.add(booking)
session.commit()

print(session.query(Users).all())
print(session.query(Auditorium).all())
print(session.query(Booking).all())

session.close()