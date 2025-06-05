
from models import Company, Dev, Freebie 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///freebies.db')
Session = sessionmaker(bind=engine)
session = Session()

print("Clearing existing data...")
session.query(Freebie).delete()
session.query(Company).delete()
session.query(Dev).delete()
session.commit()
print("Existing data cleared.")

comp1 = Company(name="TechSolutions", founding_year=2005)
comp2 = Company(name="InnovateHub", founding_year=2010)
comp3 = Company(name="FutureWorks", founding_year=2015)
comp4 = Company(name="GlobalNexus", founding_year=2000) 

session.add_all([comp1, comp2, comp3, comp4])
session.commit() 
print("Created Companies:")
for company in session.query(Company).all():
    print(f"  ID: {company.id}, Name: {company.name}")


dev1 = Dev(name="Alice Smith")
dev2 = Dev(name="Bob Johnson")
dev3 = Dev(name="Charlie Brown")
dev4 = Dev(name="Diana Prince")
dev5 = Dev(name="Ethan Hunt")

session.add_all([dev1, dev2, dev3, dev4, dev5])
session.commit()
print("\nCreated Developers:")
for dev in session.query(Dev).all():
    print(f"  ID: {dev.id}, Name: {dev.name}")


print("\nCreating Freebies...")
freebie1 = Freebie(item_name='T-Shirt', value=20, company=comp1, dev=dev1)
freebie2 = Freebie(item_name='Coffee Mug', value=10, company=comp2, dev=dev2)
freebie3 = Freebie(item_name='Laptop Sticker Pack', value=5, company=comp1, dev=dev3)
freebie4 = Freebie(item_name='Water Bottle', value=15, company=comp3, dev=dev1)
freebie5 = Freebie(item_name='Wireless Charger', value=30, company=comp4, dev=dev2)
freebie6 = Freebie(item_name='Branded Pen', value=2, company=comp1, dev=dev4)
freebie7 = Freebie(item_name='Notebook', value=8, company=comp2, dev=dev5)
freebie8 = Freebie(item_name='Headphones', value=60, company=comp3, dev=dev1)
freebie9 = Freebie(item_name='USB Drive', value=12, company=comp4, dev=dev3)

session.add_all([freebie1, freebie2, freebie3, freebie4, freebie5, freebie6, freebie7, freebie8, freebie9])
session.commit()
print("Freebies created.")

print("\n--- Seeding Complete ---")
print(f"Total Companies in DB: {session.query(Company).count()}")
print(f"Total Developers in DB: {session.query(Dev).count()}")
print(f"Total Freebies in DB: {session.query(Freebie).count()}")

session.close() 