// (function() {
//   'use strict';
  
angular
.module('WishList')

.component('produsList', {
    templateUrl: 'static/app/pages/wishlist/templates/produse.html',
    controller: function($scope,popupService, $window, Produs) 
    {
    // GET : Take everything

    $scope.produse = Produs.query();
  
  
    $scope.deleteProdus = function(produs) { // Delete a produs. Issues a DELETE to /api/produse/:id
      if (popupService.showPopup('Really delete this?')) {
        produs.$delete(function() {
          $window.location.href = ''; //redirect to home
          // $window.location.reload();  //same shit     
         });
      }
    };
  // controllerAs: 'ProdusListController'
}  
})

 .component('produsView',{
    templateUrl: 'static/app/pages/wishlist/templates/produs-view.html',
    controller: function($scope,$stateParams, Produs) {
      $scope.produs = Produs.get({id:$stateParams.id}); //Get a single produs.Issues a GET to /api/produse/:id
    }
    // controllerAs: 'ProdusViewController'

  })


  .component('produsCreate',{
    templateUrl: 'static/app/pages/wishlist/templates/produs-add.html',
    controller: function($scope, $state, $stateParams, Produs) {
      $scope.produs = new Produs();  //create new produs instance. Properties will be set via ng-model on UI
      
      $scope.addProdus = function() { //create a new produs. Issues a POST to /api/produse
        $scope.produs.$save(function() {
          $state.go('wishlist'); // on success go back to home i.e. produse state.
        });
      };
      
      // controllerAs: 'ProdusCreateController'
      },
  })

  
  .component('produsEdit',{
    templateUrl: 'static/app/pages/wishlist/templates/produs-edit.html',  
    controller: function($scope, $state, $stateParams, Produs) {
   
     $scope.updateProdus = function() { //Update the edited produs. Issues a PUT to /api/produse/:id
     $scope.produs.$update(function() {
     $state.go('wishlist'); // on success go back to home i.e. produse state.
     });
   };
   
   $scope.loadProdus = function() { //Issues a GET request to /api/produse/:id to get a produs to update
   $scope.produs = Produs.get({id:$stateParams.id});
   };
   
   $scope.loadProdus(); // Load a produs which can be edited on UI
   }
   // controllerAs: 'ProdusEditController',
  })

// function ProdusListController(popupService, $window, Produs) 
//     {
//     // GET : Take everything
//     var $scope = this;
//     $scope.produse = Produs.query();
  
  
//     $scope.deleteProdus = function(produs) { // Delete a produs. Issues a DELETE to /api/produse/:id
//       if (popupService.showPopup('Really delete this?')) {
//         produs.$delete(function() {
//           $window.location.href = ''; //redirect to home
//           // $window.location.reload();  //same shit     
//          });
//       }
//     };
//   // controllerAs: 'ProdusListController'
// }




// function ProdusViewController($stateParams, Produs) {
//   var $scope = this;
//   $scope.produs = Produs.get({id:$stateParams.id}); //Get a single produs.Issues a GET to /api/produse/:id
// }
// // controllerAs: 'ProdusViewController'




// function ProdusCreateController($state, $stateParams, Produs) {
// var $scope = this;
// $scope.produs = new Produs();  //create new produs instance. Properties will be set via ng-model on UI

// $scope.addProdus = function() { //create a new produs. Issues a POST to /api/produse
//   $scope.produs.$save(function() {
//     $state.go('wishlist'); // on success go back to home i.e. produse state.
//   });
// };

// // controllerAs: 'ProdusCreateController'
// }



// function ProdusEditController($state, $stateParams, Produs) {
//    var $scope = this;

//   $scope.updateProdus = function() { //Update the edited produs. Issues a PUT to /api/produse/:id
//   $scope.produs.$update(function() {
//   $state.go('wishlist'); // on success go back to home i.e. produse state.
//   });
// };

// $scope.loadProdus = function() { //Issues a GET request to /api/produse/:id to get a produs to update
// $scope.produs = Produs.get({id:$stateParams.id});
// };

// $scope.loadProdus(); // Load a produs which can be edited on UI
// }
// // controllerAs: 'ProdusEditController'





// })();