(function() {
    'use strict';

    angular
        .module('demoApp', [
            'ngRoute',
            'ngResource'
        ])
        .config(config)
        .run(run);


    config.$inject = ['$locationProvider', '$routeProvider'];

    function config($locationProvider, $routeProvider) {
        // $locationProvider.html5Mode(false);
        $routeProvider.when("/demo", {
                templateUrl: "static/app/demo/demo.template.html",
                controller: "DemoController",
                controllerAs: "vm"
            })
            .otherwise({
                redirectTo: '/demo'
            });

    }


    run.$inject = [];

    function run() {
        console.log('demo app running...')
    }

})();