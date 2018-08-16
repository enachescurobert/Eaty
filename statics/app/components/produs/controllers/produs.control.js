produs
    .controller('ProdusController', function($scope, Product, ProductType) {
        ProductType.query().$promise.then(function(data) {
            $scope.products = data;
        });
        Product.query().$promise.then(function(data) {
            $scope.producttypes = data;
        });
});