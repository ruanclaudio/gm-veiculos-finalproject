<svelte:head>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Racing+Sans+One&display=swap');
    </style> 
</svelte:head>

<script lang="ts">
    import Nav from '$lib/components/Nav.svelte';
    import Footer from '$lib/components/Footer.svelte';
</script>


<Nav></Nav>

<slot/>

<Footer></Footer>


<style>

/*==========RESET==========*/

:global(*) {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

:global(a) {
    text-decoration: none;
}

/*==========LAYOUT==========*/

:global(html) {
    background: #5B1111;
}
</style>