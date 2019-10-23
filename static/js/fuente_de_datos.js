/*document.querySelector('#form_fuente_datos').addEventListener('submit', e => {
    e.preventDefault();

    //var archivo = document.querySelector('#archivo');
    var formData = new FormData(document.querySelector('#form_fuente_datos'));
    a = formData.get('archivo');
    console.log(a.name);

    fetch('/cargar_archivo', {
        method: 'POST',
        body: new URLSearchParams('archivo='+a.name),
        headers: {'Content-Type': 'multipart/form-data; boundary=AaB03x; charset=utf-8'}
    })
        .then(response => response.text())
        .then(data => {
            document.querySelector('#main').innerHTML = data;
        })
})*/
