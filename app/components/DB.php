<?php

class DB {

	$user = DB_USER;	// user for the connection
	$pass = DB_PASS;	// password of the user for the connection
	$host = DB_HOST;	// hostname on which the database server resides
	$port = DB_PORT;	// port on which the database server is running.
	$dbn = DB_NAME;		// name of the database

	$dbc;				// db conection
	$dbs;				// db statement

	function __construct() {
		$dbc = new PDO('pgsql:host=' . $this->host . ':port=' . $this->port . 'dbname=' . $this->dbn,
			$this->user, $this->pass);
		$dbc->setAttribute(PDO::ATTR_ERRMODE,PDO::ERRMODE_EXCEPTION);
		$dbc->setAttribute(PDO::ATTR_CASE,PDO::CASE_LOWER);
	}

	public function run($query, $data = array()) {
		$this->dbs = $dbc->prepare($query);
		try {
			$this->dbs->execute($data);
		} catch (PDOException $e) {
			print_r($e);
			return false;
		}
	}

	public function data() {
		return $this->dbs->fetchAll();
	}
}