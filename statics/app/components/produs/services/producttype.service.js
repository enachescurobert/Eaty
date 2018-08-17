angular.module('demoApp')
       .factory('ProductTypeService',function($resource){
           return $resource('/producttypes/:id', {id: '@_id'},
        {
            update:{
                method:'PUT' 
            }
        });
       }) 