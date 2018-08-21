(function() {
  'use strict';

angular.module('demoApp')
       .config(function($stateProvider,$httpProvider) {
       
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
        
        .state('produse', { // state for showing all produse
          url: '/produse',
          templateUrl: 'static/app/components/product-type/templates/produse.html',
          controller: 'ProdusListController'
        })
        .state('viewProdus', { //state for showing single produs
          url: '/produse/:id/view',
          templateUrl: 'static/app/components/product-type/templates/produs-view.html',
          controller: 'ProdusViewController'
        })
        .state('newProdus', { //state for adding a new produs
          url: '/produse/new',
          templateUrl: 'static/app/components/product-type/templates/produs-add.html',
          controller: 'ProdusCreateController'
        })
        .state('editProdus', { //state for updating a produs
          url: '/produse/:id/edit',
          templateUrl: 'static/app/components/product-type/templates/produs-edit.html',
          controller: 'ProdusEditController'
        });

        }).run(function($state) {
        $state.go('produse'); //make a transition to produse state when app starts
      

        // $urlRouterProvider.otherwise('/page1');

        // state('/produs', {
        //   templateUrl: 'static/app/components/produs/templates/produs.html',
        //   controller:'ProdusCtrl'
        // }).
    }
  );



})();