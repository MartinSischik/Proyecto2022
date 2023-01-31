// var vents = {
//     items: {
//         parcela: '',
//         tipo:'',
//         hectareas: 0,
//         descripcion:'',
//         gasto: 0.00,
//         fecha: '',
//         products: []

//     }, 
        

// };


// $(function(){
// $('select[name="search"]').select2({
//     // theme: "bootstrap4",
//     language: 'es',
//     allowClear: true,
//     ajax: {
//         delay: 250,
//         type: 'POST',
//         url: window.location.pathname,
//         data: function () {
//             var x = document.getElementById("buscar").value;
//             var queryParameters = {
                
//                 term: x,
//                 action: 'search_products'
//             }
//             return queryParameters;
//         },
//         processResults: function (data) {
//             return {
//                 results: data
//             };
//         },
//     },
//     placeholder: 'Ingrese una descripción',
//     // minimumInputLength: 1,
    
// })
// .on('select2:select', function (e) {
//     var data = e.params.data;
//     data.cant = 1;
//     data.subtotal = 0.00;
//     vents.add(data);
//     $(this).val('').trigger('change.select2');
// });

// vents.list();
// Esto se puso aqui para que funcione bien el editar y calcule bien los valores del iva. // sino tomaría el valor del iva de la base debe
// coger el que pusimos al inicializarlo. 
// });
