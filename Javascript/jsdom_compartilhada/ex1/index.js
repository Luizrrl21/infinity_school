const titulo = document.querySelector('h1')
const btn = document.querySelector('#btn')
const subtitulo = document.createElement('h2')
const body = document.querySelector('body')

btn.addEventListener('click', function btn(){
    if(titulo.innerText == 'Aula'){
        titulo.innerText = 'Novo titulo'
        titulo.classList.remove('red')
        titulo.classList.add('green')
        subtitulo.innerText = 'Subtitulo'
        body.appendChild(subtitulo)
    } else {
        titulo.innerText = 'Aula'
        titulo.classList.remove('green')
        titulo.classList.add('red')
        body.removeChild(subtitulo)
    }
})
