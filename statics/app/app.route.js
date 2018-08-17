(function() {
  'use strict';

angular.
  module('demoApp').
  config(['$locationProvider' ,'$routeProvider',
    function config($locationProvider, $routeProvider) {
      $locationProvider.hashPrefix('');
       $routeProvider.
        when('/page1', {
        template: '<page-one></page-one>'
        }).
        when('/page2', {
          template: '<page-two></page-two>'
        }).
        when('/page3', {
          template: '<page-three></page-three>'
        }).
        when('/page4', {
          template: '<page-four></page-four>'
        }).
        when('/type', {
          template: '<product-type></product-type>'
        }).
        when('/produs', {
          templateUrl: 'static/app/components/produs/templates/produs.html',
          controller:'ProdusCtrl'
        }).
        otherwise('/page1');
    }
  ]);



})();