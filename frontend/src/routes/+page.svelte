<script lang="ts">
    import ad from "$lib/assets/ad.png"

    import Filter from "$lib/components/Filter.svelte"
</script>

<img class="banner" src="{ad}" alt="ad">

<main>
    <div class="context">
        <h4>resultados encontrados</h4>

        <div class="sort">
            <h3>Ordenar por: Maior preço</h3>

            <svg width="12" height="9" viewBox="0 0 12 9" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M1.41 0.789978L6 5.37998L10.59 0.789978L12 2.20998L6 8.20998L0 2.20998L1.41 0.789978Z" fill="white"/>
            </svg>
        </div>
    </div>

    <div class="display">
        <Filter/>

        <Filter/>
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

h3 {
    color: #FFF;
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

/*==========LAYOUT==========*/

.context {
    padding-block: 12px;

    display: flex;
    justify-content: space-between;
    align-items: center;
}

.display {
    display: flex;
    gap: 64px;
}

</style>