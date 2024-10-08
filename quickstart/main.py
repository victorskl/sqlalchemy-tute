from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from quickstart.model import Base, User, Address

# The echo=True parameter indicates that SQL emitted by connections will be logged to standard out.
# engine = create_engine("sqlite://", echo=True)  # Use a SQLite in-memory database
engine = create_engine("sqlite:///quickstart.db", echo=True)  # Use a SQLite file-based database

# drop all existing tables
Base.metadata.drop_all(bind=engine)


def print_line(f):
    def wrapped(*args, **kwargs):
        print("-" * 64)
        return f(*args, **kwargs)

    return wrapped


@print_line
def emit_ddl():
    # Emit CREATE TABLE DDL
    Base.metadata.create_all(engine)


@print_line
def create_and_persist():
    spongebob = User(
        name="spongebob",
        fullname="Spongebob Squarepants",
        addresses=[Address(email_address="spongebob@sqlalchemy.org")],
    )
    sandy = User(
        name="sandy",
        fullname="Sandy Cheeks",
        addresses=[
            Address(email_address="sandy@sqlalchemy.org"),
            Address(email_address="sandy@squirrelpower.org"),
        ],
    )
    patrick = User(name="patrick", fullname="Patrick Star")
    session.add_all([spongebob, sandy, patrick])
    session.commit()


@print_line
def simple_select():
    stmt = select(User).where(User.name.in_(["spongebob", "sandy"]))
    for user in session.scalars(stmt):
        print(user)


@print_line
def select_with_join():
    stmt = (
        select(Address)
        .join(Address.user)
        .where(User.name == "sandy")
        .where(Address.email_address == "sandy@sqlalchemy.org")
    )
    return session.scalars(stmt).one()


@print_line
def make_changes():
    stmt = select(User).where(User.name == "patrick")
    patrick = session.scalars(stmt).one()
    patrick.addresses.append(Address(email_address="patrickstar@sqlalchemy.org"))
    sandy_address.email_address = "sandy_cheeks@sqlalchemy.org"
    session.commit()


@print_line
def some_deletes():
    sandy = session.get(User, 2)
    sandy.addresses.remove(sandy_address)

    # We can choose to emit the DELETE SQL for what’s set to be changed so far,
    # without committing the transaction, using the Session.flush() method:
    session.flush()


@print_line
def delete_object():
    # The Session.delete() method doesn’t actually perform the deletion,
    # but sets up the object to be deleted on the next flush.
    # The operation will also cascade to related objects based on the cascade options.
    patrick = session.get(User, 3)
    session.delete(patrick)
    session.commit()


if __name__ == '__main__':
    with Session(engine) as session:
        emit_ddl()
        create_and_persist()
        simple_select()
        sandy_address = select_with_join()
        print(sandy_address)
        make_changes()
        some_deletes()
        delete_object()
