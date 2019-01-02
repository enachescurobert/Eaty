angular
.module('demoApp')
.controller('userInformations', function($scope, $window, $localStorage){

    $scope.is_superuser = $window.localStorage.getItem('is_superuser');
    // if ($localStorage.currentUser && $localStorage.currentUser.username == "robert") {
    if ($localStorage.currentUser && $scope.is_superuser == "true") {
        $scope.myVar = 'isAdmin';
        $scope.username = $localStorage.currentUser.username;    
    }else if ($localStorage.currentUser){
        
        $scope.myVar = 'isAuthenticated';
        $scope.username = $localStorage.currentUser.username;
 
    }


})
