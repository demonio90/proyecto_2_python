M.AutoInit();

document.querySelector('#form_consultas').addEventListener('submit', e => {
    e.preventDefault();
    var formdata = new FormData(document.querySelector('#form_consultas'));
    var consultas = formdata.getAll('consultas[]');

    fetch('/generar_consultas', {
        method: 'POST',
        body: new URLSearchParams('consultas='+consultas)
    })
        .then(response => response.text())
        .then(data => {
            document.querySelector('#content').innerHTML = data;
        })
});