<script lang="ts">
    import logo from '$lib/assets/logo.png' 

    let menuActive = false
</script>
 
<nav>
    <a href="/">
        <img class="logo" src="{logo}" alt="logo">
    </a>

    <button class="mob-menu" on:click={() => menuActive = !menuActive}>
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path fill="white" d="M3 6h18v2H3V6m0 5h18v2H3v-2m0 5h18v2H3v-2Z"/></svg>
    </button>

    <div class="infos {menuActive ? "menu-active" : ''}">

        <div class="row1">

            <div class="info">
                <svg width="14" height="20" viewBox="0 0 14 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M7 4.5C7.66304 4.5 8.29893 4.76339 8.76777 5.23223C9.23661 5.70107 9.5 6.33696 9.5 7C9.5 7.3283 9.43534 7.65339 9.3097 7.95671C9.18406 8.26002 8.99991 8.53562 8.76777 8.76777C8.53562 8.99991 8.26002 9.18406 7.95671 9.3097C7.65339 9.43534 7.3283 9.5 7 9.5C6.33696 9.5 5.70107 9.23661 5.23223 8.76777C4.76339 8.29893 4.5 7.66304 4.5 7C4.5 6.33696 4.76339 5.70107 5.23223 5.23223C5.70107 4.76339 6.33696 4.5 7 4.5ZM7 0C8.85652 0 10.637 0.737498 11.9497 2.05025C13.2625 3.36301 14 5.14348 14 7C14 12.25 7 20 7 20C7 20 0 12.25 0 7C0 5.14348 0.737498 3.36301 2.05025 2.05025C3.36301 0.737498 5.14348 0 7 0ZM7 2C5.67392 2 4.40215 2.52678 3.46447 3.46447C2.52678 4.40215 2 5.67392 2 7C2 8 2 10 7 16.71C12 10 12 8 12 7C12 5.67392 11.4732 4.40215 10.5355 3.46447C9.59785 2.52678 8.32608 2 7 2Z" fill="#BBBBBB"/>
                </svg>

                <h2>Lorem Ipsom dolor amet silor thi nissa</h2>
            </div>

            <div class="info">
                <svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M10 18C12.1217 18 14.1566 17.1571 15.6569 15.6569C17.1571 14.1566 18 12.1217 18 10C18 7.87827 17.1571 5.84344 15.6569 4.34315C14.1566 2.84285 12.1217 2 10 2C7.87827 2 5.84344 2.84285 4.34315 4.34315C2.84285 5.84344 2 7.87827 2 10C2 12.1217 2.84285 14.1566 4.34315 15.6569C5.84344 17.1571 7.87827 18 10 18ZM10 0C11.3132 0 12.6136 0.258658 13.8268 0.761205C15.0401 1.26375 16.1425 2.00035 17.0711 2.92893C17.9997 3.85752 18.7362 4.95991 19.2388 6.17317C19.7413 7.38642 20 8.68678 20 10C20 12.6522 18.9464 15.1957 17.0711 17.0711C15.1957 18.9464 12.6522 20 10 20C4.47 20 0 15.5 0 10C0 7.34784 1.05357 4.8043 2.92893 2.92893C4.8043 1.05357 7.34784 0 10 0ZM10.5 5V10.25L15 12.92L14.25 14.15L9 11V5H10.5Z" fill="#BBBBBB"/>
                </svg>

                <h2>Horário atendimento</h2>
            </div>

            <div class="info">
                <svg width="18" height="18" viewBox="0 0 18 18" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M17 12.5C15.8 12.5 14.5 12.3 13.4 11.9H13.1C12.8 11.9 12.6 12 12.4 12.2L10.2 14.4C7.4 12.9 5 10.6 3.6 7.8L5.8 5.6C6.1 5.3 6.2 4.9 6 4.6C5.7 3.5 5.5 2.2 5.5 1C5.5 0.5 5 0 4.5 0H1C0.5 0 0 0.5 0 1C0 10.4 7.6 18 17 18C17.5 18 18 17.5 18 17V13.5C18 13 17.5 12.5 17 12.5ZM2 2H3.5C3.6 2.9 3.8 3.8 4 4.6L2.8 5.8C2.4 4.6 2.1 3.3 2 2ZM16 16C14.7 15.9 13.4 15.6 12.2 15.2L13.4 14C14.2 14.2 15.1 14.4 16 14.4V16Z" fill="#BBBBBB"/>
                </svg>

                <h2>91111-1111</h2>
            </div>
        </div>

        <div class="row2">
            <a class="link" href="/">Home</a>

            <a class="link" href="/sobre">Quem Somos</a>

            <a class="btn-link" href="/venda">
                <div class="btn">
                    <h1>VENDA O SEU CARRO USADO</h1>
                    
                    <svg width="16" height="13" viewBox="0 0 16 13" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M10.2652 12.5V7.7H0.0344083L0 5.288H10.2652V0.5L16 6.5L10.2652 12.5Z" fill="#F29F12"/>
                    </svg>
                </div>
            </a>
        </div>
    </div>
</nav>


<style>
nav {
    display: flex;
    padding: 24px 64px;
    justify-content: space-between;
    align-items: center;

    background: radial-gradient(134.34% 134.34% at 50% 50%, #9F2424 28.13%, #270808 79%);
}

/*==========TYPOGRAPHY==========*/

h1 {
    color: #F29F12;
    font-family: Racing Sans One;
    font-size: 20px;
}
h2 {
    color: #BBB;
    font-family: Roboto Condensed;
    font-size: 18px;
}

.link {
    color: #FFF;
    font-family: Racing Sans One;
    font-size: 20px;
}
.link:hover {
    color: #F29F12;
}

/*==========CLASSES==========*/

.logo {

    width: 100%;
    min-width: 100px;
}

.btn {
    display: flex;
    padding: 16px 24px;
    align-items: center;
    gap: 8px;

    border-radius: 12px;
    background: #412222;
}
.btn:hover {
    background: #41222299;
}

.info {
    display: flex;
    align-items: center;
    gap: 8px;
}

.mob-menu {
    display: none;
}


/*==========LAYOUT==========*/

.infos {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-end;
    gap: 24px;
}

.row1,
.row2 {
    display: flex;
    align-items: center;
    gap: 32px;
}


@media screen and (max-width: 1300px) {

    .logo {
        width: 80%;
    }

    .link,
    .btn-link,
    h2,
    h1 {
        font-size: 16px;
    }

    svg {
        height: 16px;
    }
}

@media screen and (max-width: 950px) {

    .logo {
        width: 80%;
    }

    .link,
    .btn-link,
    h2,
    h1 {
        font-size: 16px;
    }

    svg {
        height: 16px;
    }

    .mob-menu {
        display: block;
        background-color: transparent;
        border: transparent;
    }
    .mob-menu svg {
        width: 100%;
        min-width: 12px;
        height: 100%;
        min-height: 12px;
    }
    .mob-menu:hover {
        cursor: pointer;
    }

    .row1 {
        flex-direction: column;
        margin-bottom: 24px;
    }

    .row2 {
        flex-direction: column;
    }

    .infos {
        text-align: center;
        position: absolute;
        display: none;
        background-color: #222;
        top: 100px;
        right: 0px;

        padding: 16px;

        transition: 0.5s ease-in;
    }
    .menu-active {
        display: block;
    }
}

</style>