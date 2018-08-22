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
        

        }).run(function($state) {
        $state.go('page1'); //make a transition to page1 state when app starts

    }
  );



})();