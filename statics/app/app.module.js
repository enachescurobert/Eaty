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
    'productmanagementControllers', //not used
    // 'productControllers', //not used  
    // 'userControllers' //not used
    'sessionControllers' //injected in Session component  
    


  ]);


})();                                                                        