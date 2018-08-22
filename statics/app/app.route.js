(function() {
  'use strict';

angular.module('demoApp')
       .config(function($stateProvider,$httpProvider) {
       
        $stateProvider
       .state('session',{
        url:'/session', 
        component: 'session'
        })
        .state('wishlist',{
        url:'/wishlist', 
        templateUrl: 'static/app/pages/wishlist/wishlist.template.html'
        })
        .state('pay',{
          url:'/pay', 
        component: 'pay'
        })
        .state('users',{
          url:'/users', 
        component: 'users'
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
        $state.go('wishlist'); //make a transition to wishlist state when app starts

    }
  );



})();