(function() {
  'use strict';


angular.module('demoApp', [
    'ngRoute',
    'pageOne',
    'pageTwo',
    'pageThree',

  ]);

  function run() {
    console.log('demo app running...')
}

})();