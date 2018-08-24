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
        .state('productmanagement',{
          url:'/productmanagement', 
          templateUrl: 'static/app/pages/productmanagement/productmanagement.template.html'
          })
        .state('pay',{
          url:'/pay', 
        component: 'pay'
        })
        .state('intendant',{
          url:'/intendant', 
          templateUrl: 'static/app/pages/intendant/intendant.template.html'
        })

        // Wishlist

        // .state('produse', { // state for showing all produse
        //   url: '/produse',
        //   component: 'produsList',
        // })
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
        })

        // Product Management
        
        // .state('produduse', { // state for showing all produse
        //   url: '/produduse',
        //   component: 'produdusList',
        // })
        .state('viewProdudus', { //state for showing single produdus
          url: '/productmanagement/produduse/:id/view',
          component: 'produdusView',
        })
        .state('newProdudus', { //state for adding a new produdus
          url: '/productmanagement/produduse/new',
          component: 'produdusCreate',
        })
        .state('editProdudus', { //state for updating a produdus
          url: '/productmanagement/produduse/:id/edit',
          component: 'produdusEdit',
        })

        // Intendant

        // .state('produse', { // state for showing all produse
        //   url: '/produse',
        //   component: 'produsList',
        // })
        .state('viewUser', { //state for showing single user
          url: '/intendant/users/:id/view',
          component: 'userView',
        })
        .state('newUser', { //state for adding a new user
          url: '/intendant/users/new',
          component: 'userCreate',
        })
        .state('editUser', { //state for updating a user
          url: '/intendant/users/:id/edit',
          component: 'userEdit',
        })

                // session

        // .state('produse', { // state for showing all produse
        //   url: '/produse',
        //   component: 'produsList',
        // })
        .state('viewPurchase', { //state for showing single user
          url: '/session/purchases/:id/view',
          templateUrl: 'static/app/components/purchase-row/templates/purchase-view.html',
          // component: 'purchaseView',
          controller: 'PurchaseViewController'
        })
        // .state('newPurchase', { //state for adding a new purchase
        //   url: '/session/purchases/new',
        //   component: 'purchaseCreate',
        // })
        .state('editPurchase', { //state for updating a purchase
          url: '/session/purchases/:id/edit',
          templateUrl: 'static/app/components/purchase-row/templates/purchase-edit.html',
          // component: 'purchaseEdit',
          controller: 'PurchaseEditController'
        });
        

        }).run(function($state) {
        $state.go('session'); //make a transition to session state when app starts

    }
  );



})();