'use strict';


// Declare app level module which depends on filters, and services
angular.module('myApp', [
    'ngRoute',
    'myApp.filters',
    'myApp.services',
    'myApp.directives',
    'myApp.controllers',
    'restangular'

]).
    config(['$routeProvider', 'RestangularProvider', function ($routeProvider, RestangularProvider) {
        $routeProvider
            .when('/recipes', {
                templateUrl: 'partials/recipes.html',
                controller: 'RecipeCtrl',
                title: 'Recipe List'
            })

            .when('/view2', {
                templateUrl: 'partials/partial2.html',
                controller: 'MyCtrl2',
                title: 'View 2'
            })

            .otherwise({
                redirectTo: '/view1'
            });

        RestangularProvider.setBaseUrl('http://localhost:8001');
    }]);
