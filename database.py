import os
from sqlalchemy import create_engine,func
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
from models import Entry, Base, Colors
from random import randint
# env variables

db_user = os.environ["MYSQL_USER"]
db_password = os.environ["MYSQL_PASSWORD"]
db_name = os.environ["MYSQL_DB"]

engine = create_engine(f'mysql+pymysql://{db_user}:{db_password}@db/{db_name}')

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

@contextmanager
def session_manager():
    session = Session()
    try:
        yield session
    except:
        session.rollback()
    finally:
        session.close()


#########################################################################################
# DATASET METHODS

def get_data(n, session):
    values = session.query(Entry).order_by(Entry.id.desc()).limit(n)
    values = [i.value for i in values]
    return values


def create_entries(n = 5):
    """
    Creates n  objects, each using Entry() model, and loads them into the 'entries' table.
     :param n: Number of entries to create
     :return: [] array of n integers
    """
    rand_list = [(randint(1,9)*1000 +randint(0,9)*100 )for i in range(n)]
    with session_manager() as s:
        s.bulk_save_objects(
            [
                Entry(value=i) for i in rand_list
            ]
        )
        s.commit()
        return get_data(n,s)


def delete_latest_entries(n = 5):
    """
    Deletes n  objects, each using Entry() model, from the 'entries' table.
     :param n: Number of entries to delete
     :return: None
    """
    with session_manager() as s:
        # Check for enough values to delete
        if (s.query(Entry.id).count() <n):
            return
        subquery = s.query(Entry.id).order_by(Entry.id.desc()).limit(n).subquery()
        s.query(Entry).filter(Entry.id.in_(subquery)).delete(synchronize_session=False)
        s.commit()


def retrieve_latest_entries(n = 5):
    """
    Retrieves n  objects, each using Entry() model, from the 'entries' table.
        :param n: Number of entries to retrieve
        :return: [] array of n integers
    """
    with session_manager() as s:
        # Check that enough values exist
        values_exist = s.query(Entry).first()
        total_rows = s.query(Entry.id).count()


        if(total_rows<=n or values_exist is None):
        # create enough entries then retrieve them
            values = create_entries(n)
            return values

        # Retrieve latest n values
        return get_data(n, s)


#########################################################################################
# COLORS METHODS


def get_color(s):
    colors =s.query(Colors).order_by(Colors.id.desc()).limit(1).one_or_none()
    colors_dict = {
        'red':colors.red,
        'green': colors.green,
        'blue': colors.blue,
        'alpha': colors.alpha
    }
    return colors_dict


def retrieve_latest_color():
    """
        Retrieves latest color object,using Colors() model, from the 'colores' table.
            :return: [] array of 4 integers representing RGBA Coloring scheme.
    """
    with session_manager() as s:
        # Check that at least one entry exists
        values_exist = s.query(Colors).first()

        if (values_exist is None):
            print("no color,creating one")
            # create color entry then retrieve it
            values = create_color_entry()
            return values

        # Retrieve latest n values
        return get_color(s)


def create_color_entry():
    """
        Creates object, using Colors() model, and loads it into the 'colores' table.
         :param n: Number of entries to create
         :return: [] array of n integers
        """
    rgb_list = [randint(0, 255)  for i in range(3)]
    alpha = randint(1,99)
    with session_manager() as s:
        s.add(Colors(
            red=rgb_list[0],
            green=rgb_list[1],
            blue=rgb_list[2],
            alpha=alpha,
        ))
        s.commit()
        return get_color(s)


def delete_latest_color_entry():
    """
    LIFO:Last In First Out
    Deletes object based on LIFO strategy from the 'colores' table.
     :return: None
    """
    with session_manager() as s:
        # Check for enough values to delete
        if (s.query(Colors.id).count() < 1):
            return

        latest_id = s.query(func.max(Colors.id)).one()
        s.query(Colors).filter(Colors.id == latest_id[0]).delete(synchronize_session=False)
        s.commit()


#########################################################################################