(function() {
  'use strict';


angular.module('demoApp', [
    'ui.router',
    'ngResource',
    'session',
    'pay',
    'WishList',
    'wishList.services',
    'ProductManagement',
    'ProductManagement.services',
    'InTendant',
    'inTendant.services',
    'productmanagementControllers' //not used
    // 'productControllers', //not used here 
    // 'userControllers' //not used here //injected in InTendant module

  ]);


})();                                                                        