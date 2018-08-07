(function() {
    'use strict';
    angular
        .module('demoApp')
        .factory('User', User);

    User.$inject = ['$resource'];

    function User($resource) {

        var resourceUrl = 'https://jsonplaceholder.typicode.com/users';

        return $resource(resourceUrl, {}, {
            'query': { method: 'GET', isArray: true },
            'get': { method: 'GET' },
            'update': { method: 'PUT' }
        });
    }
})();