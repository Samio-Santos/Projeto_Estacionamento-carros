function mudaFoto(foto) {
    var icon = document.getElementById("parking") = foto;
}

function Confirm_mensagem() {
        window.confirm('Tem certeza que deseja enviar o formulario?')
}

// function isValid_cpf() {
//     var cpf = document.getElementById('cpf')
//     if (cpf.value.length > 11 || cpf.value.length < 11) {
//         alert('CPF inválido! O CPF possui 11 digitos.')
//         cpf.value = ''
//     }
//     cpf.focus()
// }

// // Função que bloqueia teclas especificas no campo "INPUT"
// document.getElementById('cpf').addEventListener('keypress', function(event) {
//     if (event.key == '.' || event.key == '-') {
//         event.preventDefault()
//     }
    
// });

// // Função que permiti que o usuario digite SOMENTE números no campo "input"
// function filtroTeclas(event) {
//     return ((event.charCode >= 48 && event.charCode <= 57) || (event.keyCode == 45 || event.charCode == 46))
//   }

