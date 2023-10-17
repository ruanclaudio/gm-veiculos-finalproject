<div class="top">
    <div class="main-filter">
        <button class="tipoButton">Carros</button>
        <button class="tipoButton">Motos</button>
    </div>

    <h4>Limpar filtros</h4>
</div>

<hr>
<div class="options">
    <div class="preco-select">
        <label for="preco-select"><h3>Faixa de preço</h3></label>
    
        <select name="preco-select" id="preco-select">
            <option value="Option 1">Option 1</option>
            <option value="Option 2">Option 2</option>
            <option value="Option 3">Option 3</option>
            <option value="Option 4">Option 4</option>
            <option value="Option 5">Option 5</option>
        </select>
    </div>

    <div class="marca-select">
        <label for="marca-select"><h3>Marca</h3></label>

        <select name="marca-select" id="marca-select">
            <option value="Option 1">Option 1</option>
            <option value="Option 2">Option 2</option>
            <option value="Option 3">Option 3</option>
            <option value="Option 4">Option 4</option>
            <option value="Option 5">Option 5</option>
        </select>
    </div>

    <div class="modelo-select">
        <label for="modelo-select"><h3>Modelo</h3></label>

        <select name="modelo-select" id="modelo-select">
            <option value="Option 1">Option 1</option>
            <option value="Option 2">Option 2</option>
            <option value="Option 3">Option 3</option>
            <option value="Option 4">Option 4</option>
            <option value="Option 5">Option 5</option>
        </select>
    </div>

    <div class="checkbox">
        <input type="checkbox" name="usado" id="usado-checkbox">
        <label for="usado-checkbox"><h3>Usado</h3></label>
    </div>

    <div class="checkbox">
        <input type="checkbox" name="leilao" id="leilao-checkbox">
        <label for="leilao-checkbox"><h3>Leilão</h3></label>
    </div>
</div>

<button class="tipoButton">Buscar</button>

<style>

h4 {
    color: #000;
    font-family: Roboto;
    font-size: 16px;
    text-decoration-line: underline;
}
h3 {
    color: #000;
    font-family: Roboto;
    font-size: 24px; 
}

hr {
    border: 1px solid black;
    border-radius: 24px;
}

.options {
    display: flex;
    flex-direction: column;
    gap: 24px;
}

.top {
    display: flex;
    padding-top: 24px;
    justify-content: space-between;
    align-items: baseline;
    align-self: stretch;
    gap: 42px;
}

.main-filter {
    display: flex;
    gap: 16px;
}

.tipoButton {
    border: none;
    display: flex;
    padding: 12px 24px;
    justify-content: center;
    align-items: center;
    gap: 8px;
    cursor: pointer;

    border-radius: 12px;
    background: #5B1111;

    color: #FFF;
    text-align: center;
    font-family: Racing Sans One;
    font-size: 20px;
}
.tipoButton:hover {
    background: #412222d8;
}

select {
    display: flex;
    align-items: center;
    border: none;
    width: 100%;
    color: #000;
    font-family: Roboto;
    font-size: 16px; 
    cursor: inherit;
    min-width: 12ch;
    max-width: 24ch;
    border-radius: 0.25em;
    padding: 0.25em 0.5em;
    font-size: 1.25rem;
    margin-top: 8px;
}

.checkbox {
    display: flex;
    gap: 8px;
}

input[type="checkbox"] {
    width: 18px;
}

@media screen and (max-width: 1000px) {
    .options {
        flex-direction: row;
        flex-wrap: wrap;
        align-items: end;
    }
}

@media screen and (max-width: 550px) {
    .main-filter {
        flex-wrap: wrap;
        justify-content: center;
    }

    .top {
        flex-wrap: wrap;
        justify-content: center;
    }

    .tipoButton {
        padding: 12px 16px;
        font-size: 16px;
    }
}

</style>