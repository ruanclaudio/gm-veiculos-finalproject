<script lang="ts">
    import empresa from "$lib/assets/local.png"
</script>

<main>
    <h1>SOBRE A EMPRESA</h1>

    <div class="row">
        <div class="text">
            <p>Há 18 anos atuando no mercado de automóveis, Mauro Moretto, proprietário da GM Veículos, mantém sua tradição de honestidade, solidez e confiança.</p>
        
            <p>Com a proposta de oferecer as melhores opções para venda, troca ou compra de veículos novos ou seminovos, A GM Veículos mantém em seu estoque veículos revisados, com garantia de procedência para proporcionar sempre tranqüilidade a você cliente.</p>
        
            <p>Nossa equipe, formada por profissionais em constante aperfeiçoamento terá o maior prazer em atendê-lo e dirimir todas as dúvidas antes de fazer um bom negócio.</p>
        
            <p>Nossas parcerias agregam e somam as qualidades da GM Veículos, as melhores Financeiras, Seguradoras e Despachantes, e claro trabalhos juntos as estes parceiros para conseguir os melhores benefícios para nossos clientes.</p>
        
            <p>A Equipe GM Veículos convida você a fazer uma visita, tomar um café e com a certeza de um excelente negócio.</p>
        </div>
        
        <img src="{empresa}" alt="empresa">
    </div>
</main>

<style>
main {
    display: flex;
    padding: 64px 64px;
    flex-direction: column;
    align-items: flex-start;
    gap: 32px;
    align-self: stretch;
}

.text {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    width: 50%;
    gap: 32px;
    flex-wrap: wrap;
}

.row {

    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 32px;
    flex-wrap: wrap;
}

h1 {
    color: #F29F12;
    text-align: center;
    font-family: Racing Sans One;
    font-size: 64px;
}

p {
    color: #FFF;
    font-family: Racing Sans One;
    font-size: 22px;
}

img {
    width: 40%;
}

@media screen and (max-width: 1300px) {
    p {
        color: #FFF;
        font-family: Racing Sans One;
        font-size: 18px;
    }
}

@media screen and (max-width: 950px) {
    .row {
        flex-direction: column;
    }

    .text {
        width: 80%;
        order: 2;
    }

    img {
        width: 80%;
    }

    main {
        align-items: center;
    }

    h1 {
        font-size: 42px;
    }
}
</style>