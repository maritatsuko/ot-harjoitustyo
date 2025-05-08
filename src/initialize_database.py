from database_connection import get_database_connection


def drop_tables(connection):
    """Drop the existing tables in the database."""

    cursor = connection.cursor()

    cursor.execute("""
        drop table if exists users;
    """)
    cursor.execute("""
        drop table if exists pieces;
    """)

    cursor.execute("""
        drop table if exists colors;
    """)

    cursor.execute("""
        drop table if exists categories;
    """)

    connection.commit()


def create_tables(connection):
    """Create the necessary tables in the database."""

    cursor = connection.cursor()

    cursor.execute("""
        create table users (
            id integer primary key autoincrement,
            username text,
            password text
        );
    """)

    cursor.execute("""
        create table colors (
            id integer primary key autoincrement,
            name text
        );
    """)

    cursor.execute("""
        insert into colors (name) values
            ('red'),
            ('blue'),
            ('green'),
            ('yellow'),
            ('brown'),
            ('black'),
            ('white'),
            ('grey'),
            ('purple'),
            ('pink'),
            ('multi');
    """)

    cursor.execute("""
        create table categories (
            id integer primary key autoincrement,
            name text
        );
    """)

    cursor.execute("""
        insert into categories (name) values
            ('top'),
            ('t-shirt'),
            ('sweater'),
            ('hoodie'),
            ('jacket'),
            ('dress'),
            ('skirt'),
            ('pants'),
            ('shorts');
    """)

    cursor.execute("""
        create table pieces (
            id integer primary key autoincrement,
            title text,
            image_path text,
            color integer,
            category integer,
            uploaded_by text,
            foreign key (color) references colors (id),
            foreign key (category) references categories (id),
            foreign key (uploaded_by) references users (username)
        );
    """)

    connection.commit()


def initialize_database():
    """Initialize the database by dropping existing tables and creating new ones."""

    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
