-- SQLite
CREATE TABLE contacts(
    name text not null,
    age integer not null,
    email text not null unique
);

ALTER TABLE contacts RENAME new_contacts;