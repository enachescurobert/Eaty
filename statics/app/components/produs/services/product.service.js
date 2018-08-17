// produs
//     .factory('Product', function($resource) {
//         return $resource(
//             'http://localhost:8000/productdetails/:id/',
//             {},
//             {
//                 'query': {
//                     method: 'GET',
//                     isArray: true,
//                     headers: {
//                         'Content-Type':'application/json'
//                     }
//                 }
//             },
//             {
//                 stripTrailingSlashes: false
//             }
//         );
//     });