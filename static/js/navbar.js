document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.tooltipped');
    var instances = M.Tooltip.init(elems, 'html');
});

var botones = document.querySelectorAll('.tooltipped');

botones.forEach(boton => {
    boton.addEventListener('click', e => {
        switch(e.currentTarget.id) {
            case 'btn_datos':
                //peticion('/fuente_datos');
                fetch('/fuente_datos')
                    .then(res => res.text())
                    .then(data => {
                        document.querySelector('#main').innerHTML = data;
                        var script = document.createElement('script');
                        script.setAttribute('src', '../static/js/fuente_de_datos.js');

                        document.querySelector('#script').appendChild(script);                       
                    })
            break;
            case 'btn_graficos':
                fetch('/graficos')
                    .then(res => res.text())
                    .then(data => {
                        document.querySelector('#main').innerHTML = data;
                        var script = document.createElement('script');
                        script.setAttribute('src', '../static/js/graficos.js');

                        document.querySelector('#script').appendChild(script);
                    })
            break;
            case 'btn_limpieza':
                fetch('/limpiar')
                    .then(res => res.text())
                    .then(data => {
                        document.querySelector('#main').innerHTML = data;
                        var script = document.createElement('script');
                        script.setAttribute('src', '../static/js/limpiar.js');

                        document.querySelector('#script').appendChild(script);
                    })
            break;
            case 'btn_consulta_info':
                fetch('/consulta_info')
                    .then(res => res.text())
                    .then(data => {
                        document.querySelector('#main').innerHTML = data;
                        var script = document.createElement('script');
                        script.setAttribute('src', '../static/js/consulta-info.js');

                        document.querySelector('#script').appendChild(script);
                    })
            break;
            case 'btn_exportar':
                fetch('/generar_exportacion')
                    .then(res => res.text())
                    .then(data => {
                        document.querySelector('#main').innerHTML = data;
                        var script = document.createElement('script');
                        script.setAttribute('src', '../static/js/exportar.js');

                        document.querySelector('#script').appendChild(script);
                    })
            break;
            case 'btn_consultas_propias':
                
            break;
        }
    });
});

function peticion(ruta) {
    fetch(ruta)
        .then(res => res.text())
        .then(data => {
            document.querySelector('#main').innerHTML = data;
        })
}