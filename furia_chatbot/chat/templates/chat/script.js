const respostasFuria = [
    "Confia, pai! Mirage é nosso mapa.",
    "Clica que ele morre, irmão!",
    "Bora que hoje tem highlight no TikTok!",
    "CS é 80% cabeça, 20% mira. E eu tenho os dois.",
    "Me dropa uma AK e te dou o round, promessa.",
    "CT joga sério, TR é bagunça.",
    "Comigo não tem eco triste, tem clutch feliz!",
    "Meu coach mandou ruxar, então eu fui!",
    "Se eu errar a bala, eu erro com estilo!",
    "Smoke é arte. Flash é poesia.",
    "FURIA é mais que time, é modo de vida!",
    "Perder faz parte. Não aprender é que não dá.",
    "Toma esse spray que veio direto do bootcamp.",
    "Rush B ou nada, irmão!",
    "No meu time ninguém tiltado, só motivado.",
    "Quando a call vem do Yuurih, é pra acreditar.",
    "AWP na mão é confiança no coração!",
    "A mira pode falhar, mas o foco é 100%.",
    "5x1? Isso é só um clutch com plateia.",
    "Aqui é FURIA, não tem tempo ruim!"
];

function gerarResposta() {
    const resposta = respostasFuria[Math.floor(Math.random() * respostasFuria.length)];
    document.getElementById("resposta").innerText = resposta;
}
