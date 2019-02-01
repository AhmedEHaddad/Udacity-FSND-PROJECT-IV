from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime
from database_setup import Category, Base, Item, User

engine = create_engine('sqlite:///electroportal.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
User1 = User(name="Ahmad EH", email="ahmed.e.h.2.55@gmail.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()


# items for Smartphones
category1 = Category(user_id=1, name="Smartphones")

session.add(category1)
session.commit()

item1 = Item(user_id=1, name="Huawei Mate 30", description="Huawei's 5G phone will be foldable.",
                     date=datetime.datetime.now(), price="$600", type="Smartphone", model="P30 or Mate 30", manufacturer="HUAWEI", category=category1)

session.add(item1)
session.commit()

item2 = Item( user_id=1, name="Samsung Galaxy S10", description="5G Smartphone with up to 12GB of RAM and 1TB of storage space.",
                     date=datetime.datetime.now(), price="$600", type="Smartphone", model="Galaxy S10", manufacturer="SAMSUNG", category=category1)
session.add(item2)
session.commit()

item3 = Item( user_id=1, name="OnePlus 7", description="with its penchant for crazy speed and performance syncing well with the rapid data transfer speeds of 5G.",
                     date=datetime.datetime.now(), price="$600", type="Smartphone", model="7", manufacturer="OnePlus", category=category1)
session.add(item3)
session.commit()

item4 = Item( user_id=1, name="Oppo 5G flagship", description="",
                    date=datetime.datetime.now(), price="$600", type="Smartphone", model="5G", manufacturer="OPPO", category=category1)

session.add(item4)
session.commit()

item5 = Item( user_id=1, name="Honor 5G phone", description="No details about the Honor 5G smartphone have yet been revealed.",
                     date=datetime.datetime.now(), price="$550", type="Smartphone", model="5G", manufacturer="Honor", category=category1)
session.add(item5)
session.commit()






# items for Computers
category1 = Category(user_id=1, name="Computers")

session.add(category1)
session.commit()

item1 = Item( user_id=1, name="MSI GT75 TITAN-057", description="",
                    date=datetime.datetime.now(), price="$1300", type= "Laptop", model="TITAN", manufacturer="MSI", category=category1)

session.add(item1)
session.commit()

item2 = Item( user_id=1, name="MicroSD card memory", description="MicroSD Card Memory 16/32/64 GB",
                    date=datetime.datetime.now(), price="$7.50", type = "Card Memoery", model="MicroSD", manufacturer="SanDisk", category=category1)

session.add(item2)
session.commit()



# items for Gaming Consoles
category1 = Category(user_id=1, name="Gaming")

session.add(category1)
session.commit()

item1 = Item( user_id=1, name="GTX 1080 SLi Laptop", date=datetime.datetime.now(), description='18.4" GTX 1080 SLi Gaming Laptop', price="$1200", type= "Laptop", model="GTX", manufacturer="SLi", category=category1)

session.add(item1)
session.commit()

item2 = Item( user_id=1, name="Wireless Joypad", date=datetime.datetime.now(), description="Wireless Joypad for PS4 console", price="$20", type= "JoyPad", model="N/A", manufacturer="N/A", category=category1)

session.add(item2)
session.commit()


# items for Home Electronics
category1 = Category(user_id=1, name="Home Elcetronics")

session.add(category1)
session.commit()

item1 = Item( user_id=1, name="4K Curve TV Smart TV", date=datetime.datetime.now(), description="132''-75'' 4K Curve TV Smart TV with WI-FI", price="$170", type= "Smart Tv", category=category1)

session.add(item1)
session.commit()

item2 = Item(date=datetime.datetime.now(), user_id=1, name="Dual In-Ear True Wireless TW Bluetooth Earbud Headset with Charging Case", price="$27", type= "Charging set", category=category1)

session.add(item2)
session.commit()

# items for Auto Electronics
category1 = Category(user_id=1, name="Auto Elcetronics")

session.add(category1)
session.commit()

item1 = Item( user_id=1, name="Car Play, Android Auto with Bluetooth/Rear Camera Input", date=datetime.datetime.now(),  price="$55", manufacturer= "VoxEast Electronics", category=category1)

session.add(item1)
session.commit()

# items for Outdoor Electronics
category1 = Category(user_id=1, name="Outdoor Electronics")

session.add(category1)
session.commit()

item1 = Item( user_id=1, name="1000w europed electric bike from china", date=datetime.datetime.now(), description="Whosaler Adults100km range fat bicycle pedal assisted 1000w europed electric bike from china",
                     price="$500", type="electric bike", model="N/A", manufacturer= "Guangzhou Tengmei Bicycle Co. ,Ltd", category=category1)

session.add(item1)
session.commit()

item2 = Item( user_id=1, name="Pro Mini RC Drone", date=datetime.datetime.now(), description="Pro Mini RC Drone with 7km Transmission / 4K UHD Camera / 3-axis Brushless Gimbal",
                     price="$920", type="Drone", model="", manufacturer="Shenzhen Ruihan Supply Chain Co.,Ltd", category=category1)

session.add(item2)
session.commit()






print "added some items in some categories!"
