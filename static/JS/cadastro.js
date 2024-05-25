const tipoCadastro = document.querySelector("#tipoCadastro");
const cadastrorequisitante = document.querySelector("#cadastrorequisitante");
const cadastrooperador = document.querySelector("#cadastrooperador");

tipoCadastro.addEventListener('submit', (event) => {
    event.preventDefault();
    const selecionarTipoCadastro = document.querySelector("#selecionarTipoCadastro").value;
    if (selecionarTipoCadastro === 'requisitante') {
        cadastrorequisitante.style.display = 'block';
        cadastrooperador.style.display = 'none';
        cadastrorequisitante.scrollIntoView({behavior: 'smooth'})
    }else{
        cadastrorequisitante.style.display = 'none';
        cadastrooperador.style.display = 'block';
        cadastrooperador.scrollIntoView({behavior: 'smooth'})
    }
} )

cadastrooperador.addEventListener('submit', (event) =>{
    event.preventDefault();
    let senha = document.querySelector("#senhaoperador");
    let repetirsenha = document.querySelector("#repetirsenhaoperador");
    let msgErro = document.querySelector("#msgErrooperador");

    if (senha.value !== repetirsenha.value) {
        msgErro.style.display = 'block';
        repetirsenha.style.background = 'red';
        senha.style.background = 'red';
        return false;
    }else{
        msgErro.style.display = 'none';
        repetirsenha.style.background = 'white';
        senha.style.background = 'white';
        cadastrooperador.submit();
        return true;
    }
})

cadastrorequisitante.addEventListener('submit', (event) =>{
    event.preventDefault();
    let senha = document.querySelector("#senharequisitante");
    let repetirsenha = document.querySelector("#repetirsenharequisitante");
    let msgErro = document.querySelector("#msgErrorequisitante");

    if (senha.value !== repetirsenha.value) {
        msgErro.style.display = 'block';
        repetirsenha.style.background = 'red';
        senha.style.background = 'red';
        return false;
    }else{
        msgErro.style.display = 'none';
        repetirsenha.style.background = 'white';
        senha.style.background = 'white';
        cadastrorequisitante.submit();
        return true;
    }
})