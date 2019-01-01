angular
.module('demoApp')
.controller('userInformations', function($scope, $localStorage){

    if ($localStorage.currentUser && $localStorage.currentUser.username == "robert") {
    // if ($localStorage.currentUser.user.is_superuser === true) {
        $scope.myVar = 'isAdmin';
        $scope.utilizator = $localStorage.currentUser.username;
    }else if ($localStorage.currentUser){
        
        $scope.myVar = 'isAuthenticated';
        $scope.utilizator = $localStorage.currentUser.username;
        
    }


})
