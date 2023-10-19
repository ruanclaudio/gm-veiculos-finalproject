<script lang="ts">
    import VeiculoDisplay from "$lib/components/VeiculoDisplay.svelte"

    interface Veiculo {
        id: number
    }

    import { page } from '$app/stores';
    console.log($page.params.id)
    
    let veiculo: Veiculo
    // fetch veiculo
</script>

<main>
    <div class="form-wrapper">
        <h1>Solicitar compra de veículo</h1>

        <form action="">
            <div class="tel">
                <label for="tel">Tel: </label> <br>
                <input type="tel" name="tel" id="tel">
            </div>

            <div class="mensagem">
                <label for="mensagem">Mensagem: </label> <br>
                <textarea name="mensagem" id="mensagem" rows="6" ></textarea>
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