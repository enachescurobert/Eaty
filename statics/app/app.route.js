(function() {
  'use strict';

angular.
  module('demoApp').
  config(['$locationProvider' ,'$routeProvider',
    function config($locationProvider, $routeProvider) {
      $locationProvider.hashPrefix('!');
       $routeProvider.
        when('/page1', {
        template: '<page-one></page-one>'
        }).
        when('/page2', {
          template: '<page-two></page-two>'
        }).
        when('/page3/', {
          template: '<page-three></page-three>'
        }).
        otherwise('/page1');
    }
  ]);

  function run() {
    console.log('demo app running...')
}

})();