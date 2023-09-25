<svelte:head>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Racing+Sans+One&display=swap" rel="stylesheet">
</svelte:head>

<script lang="ts">
    import logo from '$lib/assets/logo.png' 
</script>
 
<nav>
    <a href="/">
        <img src="{logo}" alt="logo" srcset="">
    </a>

    <div class="info">
        <div class="row1">
            <div class="infos">
                <svg width="14" height="20" viewBox="0 0 14 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M7 4.5C7.66304 4.5 8.29893 4.76339 8.76777 5.23223C9.23661 5.70107 9.5 6.33696 9.5 7C9.5 7.3283 9.43534 7.65339 9.3097 7.95671C9.18406 8.26002 8.99991 8.53562 8.76777 8.76777C8.53562 8.99991 8.26002 9.18406 7.95671 9.3097C7.65339 9.43534 7.3283 9.5 7 9.5C6.33696 9.5 5.70107 9.23661 5.23223 8.76777C4.76339 8.29893 4.5 7.66304 4.5 7C4.5 6.33696 4.76339 5.70107 5.23223 5.23223C5.70107 4.76339 6.33696 4.5 7 4.5ZM7 0C8.85652 0 10.637 0.737498 11.9497 2.05025C13.2625 3.36301 14 5.14348 14 7C14 12.25 7 20 7 20C7 20 0 12.25 0 7C0 5.14348 0.737498 3.36301 2.05025 2.05025C3.36301 0.737498 5.14348 0 7 0ZM7 2C5.67392 2 4.40215 2.52678 3.46447 3.46447C2.52678 4.40215 2 5.67392 2 7C2 8 2 10 7 16.71C12 10 12 8 12 7C12 5.67392 11.4732 4.40215 10.5355 3.46447C9.59785 2.52678 8.32608 2 7 2Z" fill="#BBBBBB"/>
                </svg>

                <div class="txt-nav-weak">Lorem Ipsom dolor amet silor thi nissa</div>
            </div>
            <div class="infos">
                <svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M10 18C12.1217 18 14.1566 17.1571 15.6569 15.6569C17.1571 14.1566 18 12.1217 18 10C18 7.87827 17.1571 5.84344 15.6569 4.34315C14.1566 2.84285 12.1217 2 10 2C7.87827 2 5.84344 2.84285 4.34315 4.34315C2.84285 5.84344 2 7.87827 2 10C2 12.1217 2.84285 14.1566 4.34315 15.6569C5.84344 17.1571 7.87827 18 10 18ZM10 0C11.3132 0 12.6136 0.258658 13.8268 0.761205C15.0401 1.26375 16.1425 2.00035 17.0711 2.92893C17.9997 3.85752 18.7362 4.95991 19.2388 6.17317C19.7413 7.38642 20 8.68678 20 10C20 12.6522 18.9464 15.1957 17.0711 17.0711C15.1957 18.9464 12.6522 20 10 20C4.47 20 0 15.5 0 10C0 7.34784 1.05357 4.8043 2.92893 2.92893C4.8043 1.05357 7.34784 0 10 0ZM10.5 5V10.25L15 12.92L14.25 14.15L9 11V5H10.5Z" fill="#BBBBBB"/>
                </svg>

                <div class="txt-nav-weak">Horário atendimento</div>
            </div>
            <div class="infos">
                <svg width="18" height="18" viewBox="0 0 18 18" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M17 12.5C15.8 12.5 14.5 12.3 13.4 11.9H13.1C12.8 11.9 12.6 12 12.4 12.2L10.2 14.4C7.4 12.9 5 10.6 3.6 7.8L5.8 5.6C6.1 5.3 6.2 4.9 6 4.6C5.7 3.5 5.5 2.2 5.5 1C5.5 0.5 5 0 4.5 0H1C0.5 0 0 0.5 0 1C0 10.4 7.6 18 17 18C17.5 18 18 17.5 18 17V13.5C18 13 17.5 12.5 17 12.5ZM2 2H3.5C3.6 2.9 3.8 3.8 4 4.6L2.8 5.8C2.4 4.6 2.1 3.3 2 2ZM16 16C14.7 15.9 13.4 15.6 12.2 15.2L13.4 14C14.2 14.2 15.1 14.4 16 14.4V16Z" fill="#BBBBBB"/>
                </svg>

                <div class="txt-nav-weak">91111-1111</div>
            </div>
            <div class="infos">
                <svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M5.8 0H14.2C17.4 0 20 2.6 20 5.8V14.2C20 15.7383 19.3889 17.2135 18.3012 18.3012C17.2135 19.3889 15.7383 20 14.2 20H5.8C2.6 20 0 17.4 0 14.2V5.8C0 4.26174 0.61107 2.78649 1.69878 1.69878C2.78649 0.61107 4.26174 0 5.8 0ZM5.6 2C4.64522 2 3.72955 2.37928 3.05442 3.05442C2.37928 3.72955 2 4.64522 2 5.6V14.4C2 16.39 3.61 18 5.6 18H14.4C15.3548 18 16.2705 17.6207 16.9456 16.9456C17.6207 16.2705 18 15.3548 18 14.4V5.6C18 3.61 16.39 2 14.4 2H5.6ZM15.25 3.5C15.5815 3.5 15.8995 3.6317 16.1339 3.86612C16.3683 4.10054 16.5 4.41848 16.5 4.75C16.5 5.08152 16.3683 5.39946 16.1339 5.63388C15.8995 5.8683 15.5815 6 15.25 6C14.9185 6 14.6005 5.8683 14.3661 5.63388C14.1317 5.39946 14 5.08152 14 4.75C14 4.41848 14.1317 4.10054 14.3661 3.86612C14.6005 3.6317 14.9185 3.5 15.25 3.5ZM10 5C11.3261 5 12.5979 5.52678 13.5355 6.46447C14.4732 7.40215 15 8.67392 15 10C15 11.3261 14.4732 12.5979 13.5355 13.5355C12.5979 14.4732 11.3261 15 10 15C8.67392 15 7.40215 14.4732 6.46447 13.5355C5.52678 12.5979 5 11.3261 5 10C5 8.67392 5.52678 7.40215 6.46447 6.46447C7.40215 5.52678 8.67392 5 10 5ZM10 7C9.20435 7 8.44129 7.31607 7.87868 7.87868C7.31607 8.44129 7 9.20435 7 10C7 10.7956 7.31607 11.5587 7.87868 12.1213C8.44129 12.6839 9.20435 13 10 13C10.7956 13 11.5587 12.6839 12.1213 12.1213C12.6839 11.5587 13 10.7956 13 10C13 9.20435 12.6839 8.44129 12.1213 7.87868C11.5587 7.31607 10.7956 7 10 7Z" fill="white"/>
                </svg>

                <a class="txt-nav-bold" href="instagram">Nos siga</a>
            </div>
        </div>

        <div class="row2">
            <a class="txt-nav-links" href="/">Home</a>
            <a class="txt-nav-links" href="/about">Quem Somos</a>

            <a class="btn-venda-link" href="/venda">
                <div class="btn-venda">
                    
                    <div class="txt-nav-links-bold">VENDA O SEU CARRO USADO</div>
                    
                    <svg width="16" height="13" viewBox="0 0 16 13" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M10.2652 12.5V7.7H0.0344083L0 5.288H10.2652V0.5L16 6.5L10.2652 12.5Z" fill="#F29F12"/>
                    </svg>
                </div>
            </a>
        </div>
    </div>
</nav>

<style>

:global(body) {
    margin: 0;
}

nav {
    display: flex;
    padding: 24px 244px;
    justify-content: space-between;
    align-items: center;
    align-self: stretch;

    background: radial-gradient(134.34% 134.34% at 50% 50%, #9F2424 28.13%, #270808 79%);
}

.info {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-end;
    gap: 24px;
}

.row1 {
    display: flex;
    justify-content: flex-end;
    align-items: center;
    gap: 32px;
}

.row2 {
    display: flex;
    justify-content: flex-end;
    align-items: center;
    gap: 32px;
}

.infos {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 8px;
}

.txt-nav-weak {
    color: #BBB;
    leading-trim: both;
    text-edge: cap;
    font-family: Roboto Condensed;
    font-size: 18px;
    font-style: normal;
    font-weight: 400;
    line-height: normal;
}

.txt-nav-bold {
    color: #FFF;
    leading-trim: both;
    text-edge: cap;
    font-family: Roboto Condensed;
    font-size: 18px;
    font-style: normal;
    font-weight: 400;
    line-height: normal;
    text-decoration-line: underline;
} 

.txt-nav-links {
    color: #FFF;
    text-align: center;
    leading-trim: both;
    text-edge: cap;
    font-family: Racing Sans One;
    font-size: 20px;
    font-style: normal;
    font-weight: 400;
    line-height: normal;
    text-decoration-line: none;
}

.btn-venda {
    display: flex;
    padding: 16px 24px;
    justify-content: flex-end;
    align-items: center;
    gap: 8px;

    border-radius: 12px;
    background: #412222;
}

.btn-venda-link {
    text-decoration-line: none;
}

.txt-nav-links-bold {
    color: #F29F12;
    text-align: center;
    leading-trim: both;
    text-edge: cap;
    font-family: Racing Sans One;
    font-size: 20px;
    font-style: normal;
    font-weight: 400;
    line-height: normal;
    text-decoration-line: none;
}

</style>