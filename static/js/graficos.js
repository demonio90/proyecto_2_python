M.AutoInit();

document.querySelector('#form_graficos').addEventListener('submit', e => {
    e.preventDefault();
    var grafico = document.querySelector('#graficos').value;
    var formdata = new FormData(document.querySelector('#form_graficos'));
    var columnas = formdata.getAll('columnas[]');

    fetch('/generar_grafica', {
        method: 'POST',
        body: new URLSearchParams('grafico='+grafico+'&columnas='+columnas)
    })
        .then(response => response.text())
        .then(data => {
            document.querySelector('#img').setAttribute('src', data);
        })
});