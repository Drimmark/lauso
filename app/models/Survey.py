<?php

class Survey {
    public $id;
    public $code;
    public $name;
    public $owner;      //User object
    public $init_date;
    public $questions;  //Array of Questions objects
    public $answers;    //Array of Answer objects

}
