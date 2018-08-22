// (function() {
//   'use strict';
  
angular
.module('WishList')

.component('produsList', {
    controller: ProdusListController,  
    templateUrl: 'static/app/pages/wishlist/templates/produse.html'
    })
 .component('produsView',{
    controller: ProdusViewController,
    templateUrl: 'static/app/pages/wishlist/templates/produs-view.html'
    })
  .component('produsCreate',{
    controller: ProdusCreateController,
    templateUrl: 'static/app/pages/wishlist/templates/produs-add.html',
    })
  .component('produsEdit',{
    controller: ProdusEditController,
    templateUrl: 'static/app/pages/wishlist/templates/produs-edit.html',
    })

function ProdusListController(popupService, $window, Produs) 
    {
    // GET : Take everything
    var $ctrl = this;
    $ctrl.produse = Produs.query();
  
  
    $ctrl.deleteProdus = function(produs) { // Delete a produs. Issues a DELETE to /api/produse/:id
      if (popupService.showPopup('Really delete this?')) {
        produs.$delete(function() {
          $window.location.href = ''; //redirect to home
          // $window.location.reload();  //same shit     
         });
      }
    };
  // controllerAs: 'ProdusListController'
}




function ProdusViewController($stateParams, Produs) {
  var $ctrl = this;
  $ctrl.produs = Produs.get({id:$stateParams.id}); //Get a single produs.Issues a GET to /api/produse/:id
}
// controllerAs: 'ProdusViewController'




function ProdusCreateController($state, $stateParams, Produs) {
var $ctrl = this;
$ctrl.produs = new Produs();  //create new produs instance. Properties will be set via ng-model on UI

$ctrl.addProdus = function() { //create a new produs. Issues a POST to /api/produse
  $ctrl.produs.$save(function() {
    $state.go('wishlist'); // on success go back to home i.e. produse state.
  });
};

// controllerAs: 'ProdusCreateController'
}



function ProdusEditController($state, $stateParams, Produs) {
   var $ctrl = this;

  $ctrl.updateProdus = function() { //Update the edited produs. Issues a PUT to /api/produse/:id
  $ctrl.produs.$update(function() {
  $state.go('wishlist'); // on success go back to home i.e. produse state.
  });
};

$ctrl.loadProdus = function() { //Issues a GET request to /api/produse/:id to get a produs to update
$ctrl.produs = Produs.get({id:$stateParams.id});
};

$ctrl.loadProdus(); // Load a produs which can be edited on UI
}
// controllerAs: 'ProdusEditController'





// })();