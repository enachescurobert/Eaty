(function () {
    'use strict';
 
    angular
        .module('demoApp')
        .factory('AuthenticationService', Service);
 
    function Service($http, $window, $localStorage) {
        var service = {};

 
        service.Login = Login;
        service.Logout = Logout;
 
        return service;
 
        function Login(username, password, callback) {
            $http.post('/api-token-auth/', { username: username, password: password })
                .then(function adevarat(response) {
                    // login successful if there's a token in the response
                        // store username and token in local storage to keep user logged in between page refreshes
                        $window.localStorage.setItem('is_superuser', response.data.user.is_superuser);
                        $localStorage.currentUser = { username: username, token: response.token };

                        // add jwt token to auth header for all requests made by the $http service
                        $http.defaults.headers.common.Authorization = 'Bearer ' + response.token;
                        // execute callback with true to indicate successful login
                        callback(true);

                    
                }, function vrajeala(response){
                callback(false);
 
                })
                // .error(function(response) {
                //     callback(false);
                // })
                ;
        }
 
        function Logout() {
            // remove user from local storage and clear http auth header
            delete $localStorage.currentUser;
            window.localStorage.clear(); //try this to clear all local storage
            $http.defaults.headers.common.Authorization = '';
        }
    }
    
})();