(function() {
  'use strict';

angular.module('demoApp')
       .config(function($stateProvider) {
       
        $stateProvider
       .state('session',{
        url:'/session', 
        component: 'session'
        })
        .state('wishlist',{
        url:'/wishlist', 
        templateUrl: 'static/app/pages/wishlist/wishlist.template.html'
        })
        .state('balega',{
          url:'/balega', 
          templateUrl: 'static/app/pages/balega/balega.template.html'
          })
        .state('pay',{
          url:'/pay', 
        component: 'pay'
        })
        .state('users',{
          url:'/users', 
        component: 'users'
        })

        // Wishlist
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

        // Balega
        }).state('produduse', { // state for showing all produse
          url: '/produduse',
          component: 'produdusList',
        })
        .state('viewProdudus', { //state for showing single produdus
          url: '/balega/produduse/:id/view',
          component: 'produdusView',
        })
        .state('newProdudus', { //state for adding a new produdus
          url: '/balega/produduse/new',
          component: 'produdusCreate',
        })
        .state('editProdudus', { //state for updating a produdus
          url: '/balega/produduse/:id/edit',
          component: 'produdusEdit',
        });
        

        }).run(function($state) {
        $state.go('wishlist'); //make a transition to wishlist state when app starts

    }
  );



})();