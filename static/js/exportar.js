M.AutoInit();

document.querySelector('#form_exportar').addEventListener('submit', e => {
    e.preventDefault();
    var extension = document.querySelector('#exportar').value;

    fetch('/exportar', {
        method: 'POST',
        body: new URLSearchParams('extension='+extension)
    })
        .then(response => response.text())
        .then(data => {
            document.querySelector('#content').innerHTML = data;
        })
});