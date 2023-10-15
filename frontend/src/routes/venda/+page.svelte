
<main>
    <div class="form-wrapper">
        <h1>Solicitar venda de veículo</h1>

        <form action="">
            <div class="tel">
                <label for="tel">Tel: </label> <br>
                <input type="tel" name="tel" id="tel">
            </div>

            <div class="mensagem">
                <label for="mensagem">Mensagem: </label> <br>
                <textarea name="mensagem" id="mensagem" rows="6" ></textarea>
            </div>

            <div class="file">
                <label for="file">Selecionar foto do veículo <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24"><path fill="currentColor" d="M2 12h2v5h16v-5h2v5c0 1.11-.89 2-2 2H4a2 2 0 0 1-2-2v-5M12 2L6.46 7.46l1.42 1.42L11 5.75V15h2V5.75l3.13 3.13l1.42-1.43L12 2Z"/></svg></label> <br><br>
                <input type="file" name="file" id="file">
            </div>

            <button id="btn-form" type="submit">Enviar</button>
        </form>
    </div>
</main>


<style>

main {
    margin: 5% 20%;
}

.form-wrapper {
    display: flex;
    padding: 24px;
    flex-direction: column;
    align-items: flex-start;
    gap: 36px;
    align-self: stretch;

    background: #F29F12;
}

form {
    display: flex;
    flex-direction: column;
    gap: 42px;
    width: 100%;
}

h1 {
    text-align: center;
    font-family: Roboto condensed;
    font-size: 36px;
}

label {
    color: #000;
    text-align: center;
    font-family: Roboto condensed;
    font-size: 24px;
}

input, textarea {
    background-color: #350a0a;
    padding: 4px;
    border-radius: 4px;
    font-size: 18px;
    color: #fff;
    resize: none;
}

.tel {
    display: flex;
    align-items: flex-start;
    flex-direction: column;
    gap: 4px;
    width: 100%;
}
#tel {
    width: 30%;
}

#mensagem {
    width: 80%;
    margin-top: 16px;
}

input[type="file"] {
    display: none;
}

.file label {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    color: #FFF;
    font-size: 16px;
    background-color: #350a0a;
    padding: 12px;
    border-radius: 4px;
}

#btn-form {
    display: inline;
    padding: 16px 32px;
    align-self: center;
    margin-top: 32px;
    background-color: #350a0a;
    color: #F29F12;
    font-family: Racing Sans One; 
    font-size: 18px;
    border-radius: 4px;
}


@media screen and (max-width: 1300px) {
    #tel {
        width: 50%;
    }
}

@media screen and (max-width: 950px) {
    #tel {
        width: 80%;
    }
}
</style>