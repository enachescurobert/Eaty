(function() {
  'use strict';

angular.module('demoApp')
       .config(function($stateProvider,$httpProvider) {
       
        $stateProvider
       .state('page1',{
        url:'/page1', 
        component: 'pageOne'
        })
        .state('page2',{
        url:'/page2', 
        component: 'pageTwo'
        })
        .state('page3',{
          url:'/page3', 
        component: 'pageThree'
        })
        .state('page4',{
          url:'/page4', 
        component: 'pageFour'
        })
        .state('type',{
          url:'/type', 
        component: 'productType'
        })
        
        .state('movies', { // state for showing all movies
          url: '/movies',
          templateUrl: 'static/app/components/product-type/templates/movies.html',
          controller: 'MovieListController'
        })
        .state('viewMovie', { //state for showing single movie
          url: '/movies/:id/view',
          templateUrl: 'static/app/components/product-type/templates/movie-view.html',
          controller: 'MovieViewController'
        })
        .state('newMovie', { //state for adding a new movie
          url: '/movies/new',
          templateUrl: 'static/app/components/product-type/templates/movie-add.html',
          controller: 'MovieCreateController'
        })
        .state('editMovie', { //state for updating a movie
          url: '/movies/:id/edit',
          templateUrl: 'static/app/components/product-type/templates/movie-edit.html',
          controller: 'MovieEditController'
        });

        }).run(function($state) {
        $state.go('movies'); //make a transition to movies state when app starts
      

        // $urlRouterProvider.otherwise('/page1');

        // state('/produs', {
        //   templateUrl: 'static/app/components/produs/templates/produs.html',
        //   controller:'ProdusCtrl'
        // }).
    }
  );



})();