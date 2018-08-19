(function() {
  'use strict';

angular.
  module('demoApp').
  config(function($stateProvider, $urlRouterProvider) {
       $stateProvider

       .state('page1',{
        url:'/page1', 
        component: 'pageOne'
        })

        .state('page2',{
        url:'/page2', 
        component: 'pageTwo'
        })

        .state('page3',{
          url:'/page3', 
        component: 'pageThree'
        })

        .state('page4',{
          url:'/page4', 
        component: 'pageFour'
        })

        .state('type',{
          url:'/type', 
        component: 'productType'
        })

        $urlRouterProvider.otherwise('/page1');

        // state('/produs', {
        //   templateUrl: 'static/app/components/produs/templates/produs.html',
        //   controller:'ProdusCtrl'
        // }).
    }
  );



})();