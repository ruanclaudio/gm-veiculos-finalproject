<script lang="ts">
    const formatter = new Intl.NumberFormat('pt-BR', {});

    export let veiculo: any

</script>

<div class="resultado">
    <img src={veiculo.imagem} alt="" srcset="">

    <div class="text">
        <div class="row1">
            <h2>{veiculo.modelo.marca} {veiculo.modelo.nome} ({veiculo.condicao.ano})</h2>

            <div class="descriptions">
                <h3>Estado: {veiculo.condicao.condicao_usado ? "Usado" : "Novo"}</h3>
                <h3>Quilometragem: {formatter.format(veiculo.condicao.quilometragem)} km</h3>
                <h3>Passou por leilão: {veiculo.condicao.leiloado ? "Sim" : "Não"}</h3>
            </div>
        </div>

        <div class="row2">
            <div class="finance">
                {#if veiculo.desconto_ativo}
                    <div class="prices">
                        <div class="off">
                            <h3 class="descount">R${formatter.format(veiculo.preco)}</h3> 
                            <h3 class="percent-off">-{veiculo.porcentagem_desconto}%</h3>
                        </div>
                        <h2>R${formatter.format(veiculo.valor_desconto)}</h2>
                    </div>

                    <h3>{veiculo.pagamento}</h3>
                {:else}
                    <h2>R${formatter.format(veiculo.preco)}</h2>

                    <h3>{veiculo.pagamento}</h3>  
                {/if}
            </div>

            <a href="/compra/{veiculo.id}" class="vendaButton">Tenho interesse <svg width="16" height="13" viewBox="0 0 16 13" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M10.2652 12.5V7.7H0.0344083L0 5.288H10.2652V0.5L16 6.5L10.2652 12.5Z" fill="#F29F12"/>
              </svg>
            </a>
        </div>
    </div>
</div>

<style>
.resultado {
    display: flex;
    padding: 24px;
    align-items: center;
    gap: 36px;
    align-self: stretch;

    background: #F29F12;
}

h2 {
    color: #000;
    font-family: Roboto;
    font-size: 24px;
}
h3 {
    color: #000;
    font-family: Roboto;
    font-size: 16px;
}

.descount {
    display: inline;
    position: relative;
    color: rgb(179, 24, 24);
    font-size: 22px;
}
.descount:before {
    position: absolute;
    content: "";
    left: 0;
    top: 50%;
    right: 0;
    border-top: 2px solid;
    border-color: inherit;
    
    -webkit-transform:rotate(-5deg);
    -moz-transform:rotate(-5deg);
    -ms-transform:rotate(-5deg);
    -o-transform:rotate(-5deg);
    transform:rotate(-5deg);
}

.percent-off {
    padding: 2px 4px;
    background-color: #000;
    border-radius: 8px;
    color: #fff;
    font-size: 12px;
}

.vendaButton {
    display: flex;
    padding: 16px 24px;
    justify-content: flex-end;
    align-items: center;
    gap: 8px;

    color: #F29F12;
    text-align: center;
    font-family: Racing Sans One;
    font-size: 20px;

    border-radius: 12px;
    background: #412222;

    cursor: pointer;
}
.vendaButton:hover {
    background: #412222d8;
}

.text {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
    gap: 32px;
    align-self: stretch;
}

.row1 {
    display: flex;
    padding: 12px 0px;
    flex-direction: column;
    align-items: flex-start;
    gap: 16px;
    align-self: stretch;
}

.row2 {
    display: flex;
    padding: 12px 0px;
    gap: 16px;  
    justify-content: space-between;
    align-items: flex-end;
    align-self: stretch;
}

.finance {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    gap: 16px;
}

.off {
    display: flex;
    gap: 8px;
    align-items: self-start;
}

.prices {
    display: grid;
    gap: 6px;
}

.descriptions {
    display: flex;
    align-items: flex-start;
    align-content: flex-start;
    gap: 12px;
    align-self: stretch;
    flex-wrap: wrap;
}

img {
    width: 450px;
    height: 260px;
}

@media screen and (max-width: 1400px) {

    .resultado {
        flex-direction: column;
    }
}

@media screen and (max-width: 650px) {
    .vendaButton {
        padding: 12px 12px;
        font-size: 16px;
        margin-top: 24px;
    }

    .row2 {
        flex-direction: column;
        align-items: flex-start;
    }

    .text {
        gap: 12px;
    }

    img {
        width: 100%;
        height: 100%;
    }
}

</style>