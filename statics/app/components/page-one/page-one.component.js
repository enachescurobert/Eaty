(function() {
  'use strict';
  
  angular.
  module('pageOne').
  component('pageOne', {
    templateUrl: 'static/app/components/page-one/page-one.template.html',
  });
  
  function run() {
      console.log('demo app running...')
  }

})();