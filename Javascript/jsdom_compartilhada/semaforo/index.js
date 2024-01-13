const luz = document.createElement('div')
const body = document.querySelector('.semafaro')

// Modelo 1
const verde = document.querySelector('#verde')
const amarelo = document.querySelector('#amarelo')
const vermelho = document.querySelector('#vermelho')

verde.addEventListener('click', function btn () {
    luz.classList.add('green')
    body.append(luz)
    luz.classList.remove('yellow')
    luz.classList.remove('red')
})

amarelo.addEventListener('click', function btn () {
    luz.classList.add('yellow')
    body.append(luz)
    luz.classList.remove('red')
    luz.classList.remove('green')
})

vermelho.addEventListener('click', function btn () {
    luz.classList.add('red')
    body.append(luz)
    luz.classList.remove('green')
    luz.classList.remove('yellow')
})

// Modelo 2
const btn = document.querySelector('#btn')

btn.addEventListener('click', function btn () {
        if(luz.classList == 'green'){
            luz.classList = 'yellow'
        } else if(luz.classList == 'yellow'){
            luz.classList = 'red'
        } else if(luz.classList == 'red'){
            luz.classList = 'green'
        }
})