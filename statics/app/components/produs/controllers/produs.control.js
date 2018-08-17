angular.module('demoApp')
       .controller('ProdusCtrl', function($scope, ProductTypeService) {
            
            var producttype=ProductTypeService.get({id: $scope.id}, function(){
                console.log(producttype);
            }); // get() returns a single entry

            var producttypes=ProductTypeService.query(function(){
                console.log(producttypes)
            });

            $scope.producttype = new ProductTypeService(); //this object now has a $save() method
            $scope.producttype.$save(function() {
            });

           

            });

            

    