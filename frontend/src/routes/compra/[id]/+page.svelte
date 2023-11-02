<script lang="ts">

    import { onMount } from 'svelte';

    import VeiculoDisplayForm from "$lib/components/VeiculoDisplayForm.svelte"

    import { page } from '$app/stores';

    let formData = new FormData()

    let nomeValue: any
    let telValue: any
    let emailValue: any
    let mensagemValue: any

    async function SendHandle() {

        formData.set("nome", nomeValue.value)
        formData.set("telefone", telValue.value)
        formData.set("email", emailValue.value)
        formData.set("mensagem", mensagemValue.value)
        formData.set("veiculo", veiculoId)

        let responseInfo = await fetch("http://127.0.0.1:8000/veiculos/form-compra/", {
            method: "POST",
            body: formData,
        });
    }

    let veiculoId: any = $page.params.id
    
    let veiculos: any[] = []
    
    onMount(async () => {
        let resp = await fetch(`http://127.0.0.1:8000/veiculos/${veiculoId}`)

        veiculos = await resp.json()
    })
</script>

<main>
    <div class="form-wrapper">
        <h1>Solicitar compra de veículo</h1>

        <form action="">
            <div class="nome">
                <label for="nome">Nome: </label> <br>
                <input type="text" name="nome" id="nome" bind:this={nomeValue}>
            </div>

            <div class="tel">
                <label for="tel">Tel: </label> <br>
                <input type="tel" name="tel" id="tel" bind:this={telValue}>
            </div>

            <div class="email">
                <label for="email">Email: </label> <br>
                <input type="email" name="email" id="email" bind:this={emailValue}>
            </div>

            <div class="mensagem">
                <label for="mensagem">Mensagem: </label> <br>
                <textarea name="mensagem" id="mensagem" rows="6" bind:this={mensagemValue}></textarea>
            </div>

            {#each veiculos as veiculo (veiculo.id)}
                <VeiculoDisplayForm {veiculo}/>
            {/each}

            <button id="btn-form" type="submit" on:click={SendHandle}>Enviar</button>
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

.tel, 
.nome,
.email {
    display: flex;
    align-items: flex-start;
    flex-direction: column;
    gap: 4px;
    width: 100%;
}
#tel,
#nome,
#email {
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
    #tel,
    #nome,
    #email {
        width: 50%;
    }
}

@media screen and (max-width: 950px) {
    #tel,
    #nome,
    #email {
        width: 80%;
    }

    main {
        margin: 5% 10%;
    }
}
</style>