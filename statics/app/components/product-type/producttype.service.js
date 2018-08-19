angular.module('demoApp')
       .service('ProductTypeService', function($resource)
    {
    var restAPIUrl = "http://localhost:8000";
    return $resource(restAPIUrl + '/Product/producttypes/:id',
    { id: '@id'},
    { update: {method:'PUT'}} );
    
    });