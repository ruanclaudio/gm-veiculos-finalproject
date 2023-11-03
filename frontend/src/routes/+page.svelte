<script lang="ts">

    import { onMount } from 'svelte';

    import ad from "$lib/assets/ad.png"

    import Filter from "$lib/components/Filter.svelte"
    import VeiculoDisplay from "$lib/components/VeiculoDisplay.svelte"

    let sortData: any

    let veiculos: any[] = []

    let bannerImg: any

    const handleFilter = (event: any) => {
		
		veiculos = event.detail;
	};

    const handleFilterReset = (event: any) => {
		
		veiculos = event.detail;
	};

    onMount(async () => {
        let resp = await fetch("http://127.0.0.1:8000/veiculos")
        
        veiculos = await resp.json()

        let respBanner = await fetch("http://127.0.0.1:8000/personalizacao/promocoes")

        let bannerInfo = await respBanner.json()
        bannerImg = bannerInfo[0].imagem_banner
    })

</script>

<img class="banner" src={bannerImg} alt="banner promocional">

<main>
    <div class="context">
        <h4>{veiculos.length} resultados encontrados</h4>

        <div class="sort">
            <select name="sort" id="sort-select" bind:value={sortData}>
                <option value="asc">Preço crescente</option>
                <option value="des">Preço decrescente</option>
            </select>
        </div>
    </div>

    <div class="display">
        <div class="filterWrapper">
            <Filter sortData={sortData} on:getVeiculos={handleFilter} on:getVeiculosReset={handleFilterReset}/>
        </div>

        <div class="displayWrapper">
            {#each veiculos as veiculo (veiculo.id)}
                <VeiculoDisplay {veiculo}/>
            {/each}
        </div>
    </div>
</main>

<style>

main {
    padding: 12px 64px;
}

/*==========TYPOGRAPHY==========*/

h4 {
    color: #BBB;
    font-family: 'Roboto Condensed', sans-serif;
    font-size: 16px;
}

/*==========CLASSES==========*/

.banner {
    padding-block: 12px;

    width: 100%;
    max-height: 500px;
}

.sort {
    display: flex;
    justify-content: flex-end;
    align-items: center;
    gap: 4px;
}
select {
    background-color: #222;
    padding: 4px 4px;
    border: 1px solid white;
    width: 100%;
    color: #fff;
    font-family: Roboto;
    font-size: 16px; 
    cursor: pointer;
}

/*==========LAYOUT==========*/

.context {
    padding-block: 12px;

    display: flex;
    justify-content: space-between;
    align-items: center;
}

.display {
    display: flex;
    justify-content: space-between;
    gap: 32px;
}

.displayWrapper {
    display: flex;
    padding: 24px 0px;
    gap: 36px;
    flex-direction: column;
    align-items: center;
}

.filterWrapper {
    margin-top: 24px;
    height: 100%;
    display: flex;
    flex-direction: column;
    padding: 12px 24px 36px 24px;
    gap: 24px;

    background: #F29F12;
}


@media screen and (max-width: 1000px) {
    .display {
        flex-direction: column;
    }

    main {
    padding: 12px 18px;
}
}

@media screen and (max-width: 550px) {
    h4,
    select {
        font-size: 16px;
    }
}
</style>