(function() {
  'use strict';

angular
  .module('session')
  .component('session', {
    templateUrl: 'static/app/pages/session/session.template.html', 
  })
  .factory('sessionTableParams',['NgTableParams','$http', function(NgTableParams,$http){
    return function(url,ngparams,resource){
      var params={
        // page:1, // show first page
        // filter: {foo:'bar'} // filter stuff
        count:  10 //count per page
      }
      angular.merge(params,ngparams);
      return new NgTableParams(params, {
        filterDelay: 0,
        getData: function(params){
          var url_params = params.url();
          var query_params = {page: url_params.page, page_size:url_params.count, ordering: params.orderBy().join(',').replace('+','')};
          angular.extend(query_params, params.filter());
          //ajax request to api
          return $http.get(url, {params:query_params}).then(function(response){
            params.total(reponse.data.count);
            if(resource)
              return response.data.results.map(function(obj){return new resource(obj);});
            else
              return response.data.results;
          });
        }
      });
    };
  }])
})();