angular.module('demoApp')
       .factory('ProductTypeService',function($resource){
        // return $resource('/producttypes/:id', {id: '@_id'},
        //    return $resource('http://localhost:8000/Product/producttypes/:pk', {pk: '@_pk'},
        return $resource('/Product/producttypes/:pk', {pk: '@_pk'},

        {
            update:{
                method:'PUT' 
            }
        });
       }) 