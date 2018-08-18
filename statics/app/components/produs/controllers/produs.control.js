angular.module('demoApp')
    //    .controller('ProdusCtrl', function($scope, ProductTypeService) {
       .controller('ProdusCtrl', function($scope, $http) {

            // $scope.todoList = [{name:"Juice", done: false}];

            $http.get('/Product/producttypes').then(function(response){
                $scope.todoList = response.data;                
            });

            $scope.saveData = function() {
                var data = {name: $scope.todoInput}
                $http.put('/Product/producttypes', data)
            }

            $scope.todoAdd = function(){
                $scope.todoList.push({name: $scope.todoInput, done: false});
                $scope.todoInput = '';
            };

            $scope.remove = function() {
                var oldList = $scope.todoList;
                $scope.todoList = [];
                angular.forEach(oldList, function(x){
                    if(!x.done) $scope.todoList.push(x);
                })
            }

            // var producttype=ProductTypeService.get({pk: $scope.pk}, function(){
            //     console.log(producttype);
            // }); // get() returns a single entry

            // var producttypes=ProductTypeService.query(function(){
            //     console.log(producttypes)
            // });

            // $scope.producttype = new ProductTypeService(); //this object now has a $save() method
            // $scope.producttype.$save(function() {
            // });

            })

            

    