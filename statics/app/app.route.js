(function() {
  'use strict';

angular.module('demoApp')
       .config(function($stateProvider,$httpProvider) {
       
        $stateProvider
       .state('page1',{
        url:'/page1', 
        component: 'pageOne'
        })
        .state('wishlist',{
        url:'/wishlist', 
        templateUrl: 'static/app/components/wishlist/wishlist.template.html'
        })
        .state('page3',{
          url:'/page3', 
        component: 'pageThree'
        })
        .state('page4',{
          url:'/page4', 
        component: 'pageFour'
        })
        
        .state('produse', { // state for showing all produse
          url: '/produse',
          component: 'produsList',
        })
        .state('viewProdus', { //state for showing single produs
          url: '/wishlist/produse/:id/view',
          component: 'produsView',
        })
        .state('newProdus', { //state for adding a new produs
          url: '/wishlist/produse/new',
          component: 'produsCreate',
        })
        .state('editProdus', { //state for updating a produs
          url: '/wishlist/produse/:id/edit',
          component: 'produsEdit',
        });
        
        // .state('produse', { // state for showing all produse
        //   url: '/produse',
        //   templateUrl: 'static/app/components/product-type/templates/produse.html',
        //   controller: 'ProdusListController'
        // })
        // .state('viewProdus', { //state for showing single produs
        //   url: '/page1/produse/:id/view',
        //   templateUrl: 'static/app/components/product-type/templates/produs-view.html',
        //   controller: 'ProdusViewController'
        // })
        // .state('newProdus', { //state for adding a new produs
        //   url: '/page1/produse/new',
        //   templateUrl: 'static/app/components/product-type/templates/produs-add.html',
        //   controller: 'ProdusCreateController'
        // })
        // .state('editProdus', { //state for updating a produs
        //   url: '/page1/produse/:id/edit',
        //   templateUrl: 'static/app/components/product-type/templates/produs-edit.html',
        //   controller: 'ProdusEditController'
        // });

        }).run(function($state) {
        $state.go('page1'); //make a transition to produse state when app starts
      

        // $urlRouterProvider.otherwise('/page1');

        // state('/produs', {
        //   templateUrl: 'static/app/components/produs/templates/produs.html',
        //   controller:'ProdusCtrl'
        // }).
    }
  );



})();