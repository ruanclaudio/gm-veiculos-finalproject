

<main>
    <div class="form-wrapper">
        <h1>Solicitar venda de veículo</h1>

        <form action="">
            <div class="tel">
                <label for="tel">Tel: </label> <br>
                <input type="tel" name="tel" id="tel">
            </div>

            <div class="mensagem">
                <label for="">Mensagem: </label> <br>
                <textarea name="mensagem" id="mensagem"></textarea>
            </div>

            <input type="file" name="img" id="img-form">

            <input id="btn-form" type="button" value="Enviar">
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
    font-family: Roboto;
    font-size: 36px;
}

label {
    color: #000;
    text-align: center;
    font-family: Roboto;
    font-size: 24px;
}

input, textarea {
    background-color: #350a0a;
    padding: 4px;
    border-radius: 4px;
    font-size: 18px;
    color: #fff;

}

.tel {
    display: flex;
    align-items: flex-start;
    flex-direction: column;
    gap: 4px;
    width: 50%;
}

#mensagem {
    width: 75%;
    min-height: 350px;
    
    margin-top: 16px;
}

#img-form {
    width: 60%;
}

#btn-form {
    display: inline;
    padding: 24px;
    width: 40%;
    align-self: center;
    margin-top: 32px;
}

</style>