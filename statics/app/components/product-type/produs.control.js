angular.module('demoApp')
       .controller('ProductTypeCtrl', function ($scope, ProductTypeService) 
{
  // GET : Récupère tous les Posts
  $scope.posts = ProductTypeService.query();
 
  // GET : Récupère le Post #3
  $scope.postToEdit = ProductTypeService.get({id:3});
 
  // DELETE : Supprime le Post #3
  ProductTypeService.delete({id:3});
 
  //UPDATE
  var post = ProductTypeService.get({id:2}, function() 
    {
  post.archived = true;
  post.$update();
    });

  // SAVE : Crée un nouveau Post
  var myPostObj = {name: 'Twix2'};
  ProductTypeService.save(myPostObj);
 
  // SAVE : Crée un nouveau Post, version #2
  var aPost = new ProductTypeService(myPostObj);
  aPost.$save();
 
});