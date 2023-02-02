var valor = 1;
var vents = {
    items: {
        parcela: '',
        tipo:'',
        hectareas: 0,
        descripcion:'',
        gasto: 0.00,
        fecha: '',
        products: [],
        

    },
    calculate_invoice: function () {
        var subtotal = 0.00;
        
        $.each(this.items.products, function (pos, dict) {
            // console.log(pos);
            // console.log(dict);
            dict.pos = pos;
            dict.subtotal = dict.cantidad * parseFloat(dict.precio);
            subtotal += dict.subtotal;
        });
        // console.log(subtotal);
        this.items.subtotal = subtotal;
        // this.items.iva = this.items.subtotal * iva;
        // this.items.total = this.items.subtotal + this.items.iva;

        $('input[name="gasto"]').val(this.items.subtotal.toFixed(2));
        // $('input[name="ivacalc"]').val(this.items.iva.toFixed(2));
        // $('input[name="total"]').val(this.items.total.toFixed(2));
    },
    add: function (item) {
        this.items.products.push(item);
        this.list();
    },
    list: function () {
        this.calculate_invoice();
        tblProducts = $('#tblProducts').DataTable({
            responsive: true,
            autoWidth: false,
            destroy: true,
            data: this.items.products,
            columns: [
                {"data": "id"},
                {"data": "name"},
                {"data": "categoria.nombre"},
                {"data": "ingrediente"},
                {"data": "precio"},
                {"data": "cantidad"},
                {"data": "subtotal"},
            ],
            columnDefs: [
                {
                    targets: [0],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<a rel="remove" class="btn btn-danger btn-xs btn-flat" style="color: white;"><i class="fas fa-trash-alt"></i></a>';
                    }
                },
                {
                    targets: [4],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                            return '$ ' + parseFloat(data).toLocaleString("es-AR");
        
                        }
                },
                {
                    targets: [5],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="number" name="cantidad" class="form-control form-control-sm input-sm "  value="'+row.cantidad+'">';
                    }
                },
                {
                    targets: [-1],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '$' + parseFloat(data).toFixed(2);
                    }
                },
            ],
            rowCallback(row, data) {
                console.log(row)
                // $(row).find('input[name="cantidad"]').TouchSpin({
                //     min: 1,
                //     max: 1000000000,
                //     step: 1
                // });

            },
            initComplete: function (settings, json) {

            }
        });
    },
};

$(function(){
    
    // event submit
    $('form').on('submit', function (e) {
        e.preventDefault();

        if (vents.items.products.length === 0) {
            message_error('Debe al menos tener un item en su detalle de venta');
            return false;
        }

        vents.items.date_joined = $('input[name="date_joined"]').val();
        vents.items.cli = $('select[name="cli"]').val();
        var parameters = new FormData();
        parameters.append('action', $('input[name="action"]').val());
        parameters.append('vents', JSON.stringify(vents.items));
        submit_with_ajax(window.location.pathname, 'Notificación', '¿Estas seguro de realizar la siguiente acción?', parameters, function () {
            location.href = '/erp/sale/list/';
        });
    });
    $('select[name="search"]').select2({
                // theme:"bootstrap4",
        language:"es",
        // language: 'es',
        allowClear: true,
        ajax: {
        delay: 250,
            type: 'POST',
            url: window.location.pathname,
            data: function (params) {
                var queryParameters = {
                    term: params.term,
                    action: 'search_products'
                }

                return queryParameters;
            },
            processResults: function (data) {
                return {
                    results: data
                };
            },
        },
        placeholder: 'Ingrese una descripción',
        minimumInputLength: 1,
        })
        .on('select2:select', function (e) {
            
            var data = e.params.data;
            data.cantidad = 1;
            data.subtotal = data.cantidad*data.precio;
            // console.log(data);
            vents.add(data);
            // console.log(vents.products);
            $(this).val('').trigger('change.select2');
        })
        .on('change', function () {
            vents.calculate_invoice();
        })
    $('.btnRemoveAll').on('click', function () {
        var cosa='¿Estas seguro de eliminar el producto de tu detalle?'
        if (vents.items.products.length === 0) return false;
        message_error(cosa)
    });
    $('#tblProducts tbody')
    .on('click', 'a[rel="remove"]', function () {
            var tr = tblProducts.cell($(this).closest('td, li')).index();
            
            alert_action('Notificación', '¿Estas seguro de eliminar el producto de tu detalle?', function () {
                vents.items.products.splice(tr.row, 1);
                vents.list();
            });
            
        })
    .on('change keyup', 'input[name="cantidad"]', function () {
            console.log('x');
            var cant = parseInt($(this).val());
            console.log(cant);
            var tr = tblProducts.cell($(this).closest('td, li')).index();
            vents.items.products[tr.row].cantidad = cant;
            vents.calculate_invoice();
            $('td:eq(6)', tblProducts.row(tr.row).node()).html('$' + vents.items.products[tr.row].subtotal.toFixed(2));
        });
        
});