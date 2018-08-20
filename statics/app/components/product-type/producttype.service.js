// angular.module('demoApp.services',[])
//        .factory('Movie', function($resource)
//     {
//     var restAPIUrl = "http://localhost:8000";
//     return $resource(restAPIUrl + '/Product/producttypes/:id',
//     { id: '@_id'},
//     { update: {method:'PUT'}} );
    
//     });

angular.module('demoApp.services', []).factory('Movie', function($resource) {
    return $resource('http://localhost:8000/Product/producttypes/:id', { id: '@_id' }, {
        update: {
        method: 'PUT'
        }
    });
});