angular.module('purchaseControllers', [])
       .factory('Purchase', function($resource) {
    return $resource('/Purchase/purchases/:id/',{id:'@id'},{
        update: {method:'PUT'},
    },{

    
    stripTrailingSlashes: false
  });
})
       .service('popupService',function($window){
    this.showPopup=function(message){
        return $window.confirm(message);
    }
})

.controller('PurchaseListController', function($scope,popupService, $window, Purchase) 
{
// GET : Take everything

$scope.purchases = Purchase.query();


$scope.deletePurchase = function(purchase) { // Delete a purchase. Issues a DELETE to /api/purchases/:id
  if (popupService.showPopup('Really delete this?')) {
    purchase.$delete(function() {
      $window.location.href = ''; //redirect to home
      // $window.location.reload();  //same shit     
     });
  }
};
// controllerAs: 'PurchaseListController'
}  

)

.controller('PurchaseViewController', 
function($scope,$stateParams, Purchase) {
    $scope.purchase = Purchase.get({id:$stateParams.id}); //Get a single purchase.Issues a GET to /api/purchases/:id
  }
)

.controller('PurchaseCreateController', 
function($scope, $state, $stateParams, Purchase) {
    $scope.purchase = new Purchase();  //create new purchase instance. Properties will be set via ng-model on UI
    
    $scope.addPurchase = function() { //create a new purchase. Issues a POST to /api/purchases
      $scope.purchase.$save(function() {
        $state.go('session'); // on success go back to home i.e. purchases state.
      });
    };
    
    // controllerAs: 'PurchaseCreateController'
    }
)

.controller('PurchaseEditController', 
function($scope, $state, $stateParams, Purchase) {
   
    $scope.updatePurchase = function() { //Update the edited purchase. Issues a PUT to /api/purchases/:id
    $scope.purchase.$update(function() {
    $state.go('session'); // on success go back to home i.e. purchases state.
    });
  };
  
  $scope.loadPurchase = function() { //Issues a GET request to /api/purchases/:id to get a purchase to update
  $scope.purchase = Purchase.get({id:$stateParams.id});
  };
  
  $scope.loadPurchase(); // Load a purchase which can be edited on UI
  }

)
