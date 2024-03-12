document.addEventListener('DOMContentLoaded', () => {
    var currentCategoryName = currentWeightName = ""

    // Query Selector
    const querySelector = (selector) => { return document.querySelector(selector) }

    const tournamentId = querySelector('#TournamentId').value

    const ContentLeftCategories = querySelector('#ContentLeftCategories')
    const ContentLeftWeights = querySelector('#ContentLeftWeights')

    const ContentLeft = querySelector('#ContentLeft')
    const ContentRight = querySelector('#ContentRight')

     /*
        TODO: Взятие категорий с апи
    */
    const getTournamentCategoriesWeights = async () => {
        const response = await fetch(`/api/tournament/${tournamentId}/show-all-categories-weights/`)
        const data = await response.json()

        if (data.status == 'success') {
            renderTournamentCategoriesData(data.weights, 'categories')
        } else {
            console.error(`Couldn't get tournament ${data.message}`)
        }
    }

     /*
        TODO: Рендеринг категорий
    */
    function renderTournamentCategoriesData(data, status='') {
        if (status == 'categories') { // TODO: Categories
            ContentLeftCategories.innerHTML = ''
        } else if (status == 'weights') { // TODO: Weights
            ContentLeftWeights.innerHTML = ''
        } else if (status == 'athletes') { // TODO: Athletes
                // <h2># ${currentCategoryName} - ${currentWeightName}</h3>

            ContentRight.innerHTML = `
                <div class="toss__content__category toss__participant__content__category toss__participant__content__category__spec ">
                    <h4>№</h4>
                    <h4>ФИО</h4>
                    <h4>Дата рождения</h4>
                </div>
            `
        }

        data.forEach((category, index) => {
            const div = document.createElement('div')
            div.classList.add('toss__content__category')

            if (status == 'categories') {
                // TODO: Categories
                div.addEventListener('click', () => {
                    renderTournamentCategoriesData(category.weights, 'weights')
                    currentCategoryName = category.year
                })

                div.innerHTML = `
                    ${category.gender == 'Мужской' ? "<i class='fa-solid fa-mars-stroke' style='color: #84BEFF'></i>" :
                                                            "<i class='fa-solid fa-venus' style='color: #FF8080'></i>" }
                    <h3 class='toss__content__category__title'>${category.year}</h3>
                    <span class="toss__content__category__span" style="background-color:${category.gender == 'Мужской' ? '#84BEFF' : '#FF8080' }" ></span>
                `
            } else if (status == 'weights') {
                // TODO: Weights
                let athletes_count = category.athletes.length
                div.innerHTML = `
                    <h3 class='toss__content__category__title'>${category.name}</h3>
                    <span>${athletes_count}</span>
                `

                if (athletes_count > 0) {
                    div.addEventListener('click', () => {
                        currentWeightName = category.name
                        renderTournamentCategoriesData(category.athletes, 'athletes')
                    })
                } else {
                    div.style.opacity = .3
                }
            } else if (status == 'athletes') {
                // TODO: Athletes
                div.classList.add('toss__participant__content__category')

                if (index % 2 != 0) {
                    div.style.backgroundColor = 'rgb(87, 127, 220, 1, .15)'
                }

                div.innerHTML = `
                    <h4>${ index + 1 }</h4>
                    <h4>${category.fio}</h4>
                    <h4>${category.year}</h4>
                `
            }

            if (status == 'categories') { // TODO: Categories
                ContentLeftCategories.appendChild(div)
            } else if (status == 'weights') { // TODO: Weights
                ContentLeftWeights.appendChild(div)
            } else if (status == 'athletes') { // TODO: Athletes
                ContentRight.appendChild(div)
            }

        })

    }

    getTournamentCategoriesWeights()


})