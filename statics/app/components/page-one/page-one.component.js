// (function() {
//   'use strict';
  
  angular
  .module('pageOne')

  .directive('produsList', function(){
    return{
    templateUrl: 'static/app/components/product-type/templates/produse.html',
    controller: function ($scope, $state,popupService, $window, Produs) 
    {
      // GET : Take everything
      // $scope.produse = Produs.query();
      $scope.produse = Produs.query();
    
    
      $scope.deleteProdus = function(produs) { // Delete a produs. Issues a DELETE to /api/produse/:id
        if (popupService.showPopup('Really delete this?')) {
          produs.$delete(function() {
            $window.location.href = ''; //redirect to home
          });
        }
      };
    },
    controllerAs: 'ProdusListController'
  };
})

.directive('produsView', function(){
  return{
  templateUrl: 'static/app/components/product-type/templates/produs-view.html',
  controller: function($scope, $stateParams, Produs) {
  $scope.produs = Produs.get({id:$stateParams.id}); //Get a single produs.Issues a GET to /api/produse/:id
},
  controllerAs: 'ProdusViewController'
}}
)

.directive('produsCreate', function(){
  return{
  templateUrl: 'static/app/components/product-type/templates/produs-add.html',
  controller: function($scope, $state, $stateParams, Produs) {
  $scope.produs = new Produs();  //create new produs instance. Properties will be set via ng-model on UI

  $scope.addProdus = function() { //create a new produs. Issues a POST to /api/produse
    $scope.produs.$save(function() {
      $state.go('page1'); // on success go back to home i.e. produse state.
    });
  };
},
  controllerAs: 'ProdusCreateController'
}}
)

.directive('produsEdit', function(){
  return{
  templateUrl: 'static/app/components/product-type/templates/produs-edit.html',
  controller: function($scope, $state, $stateParams, Produs) {
  $scope.updateProdus = function() { //Update the edited produs. Issues a PUT to /api/produse/:id
    $scope.produs.$update(function() {
      $state.go('page1'); // on success go back to home i.e. produse state.
    });
  };

  $scope.loadProdus = function() { //Issues a GET request to /api/produse/:id to get a produs to update
    $scope.produs = Produs.get({id:$stateParams.id});
  };

  $scope.loadProdus(); // Load a produs which can be edited on UI

},
  controllerAs: 'ProdusEditController'
}}
)
  


// })();