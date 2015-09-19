<?php

class DB {

    private $host = DB_HOST;
    private $port = DB_PORT;
    private $name = DB_NAME;
    private $user = DB_USER;
    private $password = DB_PASSWORD;
    private $connection;
    private $stmt;

    function __construct() {
        $dsn = 'pgsql:host=' . $this->host . ';port=' . $this->port . ';dbname=' . $this->name;
        $this->connection = new PDO($dsn, $this->user, $this->password);
        $this->connection->setAttribute(PDO::ATTR_CASE, PDO::CASE_LOWER);
        $this->connection->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    }

    public function query($query, $data = array()) {
        $this->stmt = $this->connection->prepare($query);

        try {
            return $this->stmt->execute($data);
        } catch(PDOException $e) {
            print_r($e);
            return false;
        }
    }

    public function data() {
        try {
            return $this->stmt->fetchAll();
        } catch(PDOException $e) {
            print_r($e);
            return false;
        }
    }
}
