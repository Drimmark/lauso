<?php
require_once(config.php);

session_start();

$controller = (isset($GET[c]) && !empty($GET[c])) ? $GET[c] . 'Controller' : 'indexController';
$action = (isset($GET[a]) && !empty($GET[a])) ? $GET[a] . 'Action' : 'indexAction';

$app = new $controller();
$app->$action();

function __autoload($class) {
    $escapedClass = str_replace(array('.', '/'), ' ', $escapedClass);

    if(file_exists('app/controller/' . $escapedClass . '.php')) {
        include_once('app/controller/' . $escapedClass . '.php');
    } else if('app/models/' . $escapedClass . '.php') {
        include_once('app/models/' . $escapedClass . '.php');
    } else if('app/views/' . $escapedClass . '.php') {
        include_once('app/views/' . $escapedClass . '.php');
    } else if('app/components/' . $escapedClass . '.php') {
        include_once('app/components/' . $escapedClass . '.php');
    }
}
