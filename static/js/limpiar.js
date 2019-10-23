M.AutoInit();

document.querySelector('#form_limpiar').addEventListener('submit', e => {
    e.preventDefault();
    var columna = document.querySelector('#columnas').value;
    var limpieza = document.querySelector('#limpieza').value;

    fetch('/generar_limpieza', {
        method: 'POST',
        body: new URLSearchParams('columna='+columna+'&limpieza='+limpieza)
    })
        .then(response => response.text())
        .then(data => {
            document.querySelector('#content').innerHTML = data;
        })
});