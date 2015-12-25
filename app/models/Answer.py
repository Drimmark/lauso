<?php

class Answer {
    public $id;
    public $survey;     //id of a Suervey
    public $question;   //id of a Question
    public $content;
    public $owner;      //id of a User
    public $init_date;

    public findByQuestion($idQuestion) {
        $db = new DB;
        $db->query('SELECT * FROM answers WHERE question = ?', array($idQuestion));
        $data = $db.data();
        $answers = array();

        foreach ($data as $row) {
            $answer = new Answer;
            foreach ($row as $key => $value) {
                $answer->{$key} = $value;
            }
            $answers[] = $answer;
        }

        return $answers;
    }

    public findBySurvey($idSurvey) {
        $db = new DB;
        $db->query('SELECT * FROM answers WHERE survey = ?', array($idSurvey));
        $data = $db.data();
        $answers = array();

        foreach ($data as $row) {
            $answer = new Answer;
            foreach ($row as $key => $value) {
                $answer->{$key} = $value;
            }
            $answers[] = $answer;
        }

        return $answers;
    }

    public findByOwner($idOwner) {
        $db = new DB;
        $db->query('SELECT * FROM answers WHERE owner = ?', array($idOwner));
        $data = $db.data();
        $answers = array();

        foreach ($data as $row) {
            $answer = new Answer;
            foreach ($row as $key => $value) {
                $answer->{$key} = $value;
            }
            $answers[] = $answer;
        }

        return $answers;
    }

    public findById($id) {
        $db = new DB;
        $db->query('SELECT * FROM answers WHERE id = ?', array($id));
        $data = $db.data();
        $answers = NULL;

        foreach ($data as $row) {
            $answer = new Answer;
            foreach ($row as $key => $value) {
                $answer->{$key} = $value;
            }
            $answers[] = $answer;
        }

        return $answer;
    }
}
