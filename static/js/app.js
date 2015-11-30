(function(){

angular
	.module('uthhApp', [])
	.config(['$httpProvider', '$interpolateProvider', function($httpProvider, $interpolateProvider){
		$interpolateProvider.startSymbol('{[').endSymbol(']}');
    	$httpProvider.defaults.headers.post['Content-Type'] = 'application/json';
	}]);

})();
(function(){
	angular
	.module('uthhApp')
	.controller("UthhController", UthhController);

	UthhController.$inject = ['$scope', 'UthhService'];

	function UthhController($scope, uthhService){
		var vm = this;
		vm.hola = 'Hola mundo';

		uthhService.getEquipos().then(function(response){
			vm.equipos = response.data;
		});
	};
})();

(function(){
	angular
	.module('uthhApp')
	.factory("UthhService", UthhService);

	function UthhService($http){
		var URL_BASE = "https://uthh-conf-api.herokuapp.com/api/";

		var getEquipos = function(){
			return $http.get(URL_BASE + 'equipos/');
		};

		return {
			'getEquipos': getEquipos
		};
	};
})();
