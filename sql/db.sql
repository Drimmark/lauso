CREATE TABLE users (
       id serial PRIMARY KEY,
       name varchar(100) NOT NULL,
       surname varchar(100) NOT NULL,
       rol integer DEFAULT 10,
       email varchar(100) UNIQUE NOT NULL,
       pass varchar(60) NOT NULL,
       nick varchar(100) UNIQUE NOT NULL
);

CREATE TABLE surveys (
       id serial PRIMARY KEY,
       code varchar(5) UNIQUE NOT NULL,
       name varchar(100) NOT NULL,
       owner integer NOT NULL REFERENCES users (id),
       init_date date NOT NULL
);

CREATE TABLE questions (
       id serial PRIMARY KEY,
       survey integer NOT NULL REFERENCES surveys (id),
       content text NOT NULL
);

CREATE TABLE answers (
       id serial PRIMARY KEY,
       question integer NOT NULL REFERENCES questions (id),
       content text NOT NULL,
       owner integer NOT NULL REFERENCES users (id),
       init_date date NOT NULL
);

CREATE TABLE groups (
       id serial PRIMARY KEY,
       name varchar(100) NOT NULL
);

CREATE TABLE groups_users (
       id_group integer NOT NULL REFERENCES groups (id),
       id_user integer NOT NULL REFERENCES users (id),
       PRIMARY KEY(id_group, id_user)
);

CREATE TABLE groups_surveys (
       id_group integer NOT NULL REFERENCES groups (id),
       id_survey integer NOT NULL REFERENCES surveys (id),
       PRIMARY KEY(id_group, id_survey)
);
