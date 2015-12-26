CREATE TABLE users (
    user_id     serial PRIMARY KEY,
    nick        varchar(100) NOT NULL UNIQUE,
    name        varchar(100) NOT NULL,
    surname     varchar(100) NOT NULL,
    email       varchar(100) NOT NULL,
    pass        varchar(60) NOT NULL,
    rol         integer NOT NULL
);

CREATE TABLE surveys (
    survey_id   serial PRIMARY KEY,
    code        varchar(50) UNIQUE,
    name        varchar(100) NOT NULL,
    owner       integer NOT NULL REFERENCES users (user_id),
    init_date   date NOT NULL
);

CREATE TABLE questions (
    question_id     serial PRIMARY KEY,
    content         text NOT NULL,
    required        boolean DEFAULT true,
    survey          integer NOT NULL REFERENCES surveys (survey_id)
);

CREATE TABLE radio_questions (
    radio_question_id   serial PRIMARY KEY,
    content             text NOT NULL,
    question            integer NOT NULL REFERENCES question (question_id)
);

CREATE TABLE check_questions (
    check_question_id   serial PRIMARY KEY,
    content             text NOT NULL,
    question            integer NOT NULL REFERENCES question (question_id)
);

CREATE TABLE answers (
    answer_id       serial PRIMARY KEY,
    content         text NOT NULL,
    question        integer NOT NULL REFERENCES question (question_id),
    owner           integer NOT NULL REFERENCES users (user_id)
);

CREATE TABLE radio_answers (
    radio_answer_id     serial PRIMARY KEY,
    question            integer NOT NULL REFERENCES question (question_id),
    answer              integer NOT NULL REFERENCES radio_questions (radio_question_id),
    owner               integer NOT NULL REFERENCES users (user_id),
    UNIQUE(question,owner)
);

CREATE TABLE check_answers (
    check_answer_id     serial PRIMARY KEY,
    answer              integer NOT NULL REFERENCES check_questions (check_question_id),
    owner               integer NOT NULL REFERENCES users (user_id),
    UNIQUE(answer,owner)
);
