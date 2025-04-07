from database_connection import get_database_connection


def drop_tables(connection):

    cursor = connection.cursor()

    cursor.execute("""
        drop table if exists users;
    """)
    cursor.execute("""
        drop table if exists pieces;
    """)

    connection.commit()


def create_tables(connection):

    cursor = connection.cursor()

    cursor.execute("""
        create table users (
            id integer primary key autoincrement,
            username text,
            password text
        );
    """)
    cursor.execute("""
        create table pieces (
            id integer primary key autoincrement,
            title text,
            image_path text,
            color text,
            type text,
            user_id integer,
            foreign key (user_id) references users (id)
        );
    """)

    connection.commit()


def initialize_database():

    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
