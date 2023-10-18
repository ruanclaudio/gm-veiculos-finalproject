<script lang="ts">

    import ad from "$lib/assets/ad.png"

    import Filter from "$lib/components/Filter.svelte"
    import VeiculoDisplay from "$lib/components/VeiculoDisplay.svelte"
    
    let precoSelect: any

    // let promise = async () => {

    //     fetch("")
    // } 

    // promise

    let veiculos = [
        {
            id: 1
        },
        {
            id: 2
        },
        {
            id: 3
        },
        {
            id: 4
        }
    ]
</script>

<img class="banner" src="{ad}" alt="ad">

<main>
    <div class="context">
        <h4>{veiculos.length} resultados encontrados</h4>

        <div class="sort">
            <select name="" id="" bind:this={precoSelect}>
                <option value="">Preço crescente</option>
                <option value="">option 2</option>
                <option value="">option 3</option>
                <option value="">option 4</option>
            </select>
        </div>
    </div>

    <div class="display">
        <div class="filterWrapper">
            <Filter/>
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