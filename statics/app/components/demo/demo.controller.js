(function() {
    'use strict';

    angular
        .module('demoApp')
        .controller('DemoController', DemoController);

    DemoController.$inject = ['$scope', 'User'];

    function DemoController($scope, User) {
        //
        var vm = this;
        //
        vm.users = User.query();
        //
        console.log('demo controller running...');
        //
    }

})();