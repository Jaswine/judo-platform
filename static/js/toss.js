document.addEventListener('DOMContentLoaded', () => {
    // Query Selector
    const querySelector = (selector) => { return document.querySelector(selector) }

    // Tournament ID
    const tournamentId = querySelector('#TournamentId').value

    // Buttons
    const HideContentCategories = querySelector('#HideContentCategories')

    // Draw Buttons
    const DrawSorting = querySelector('#DrawSorting')
    const ClearSorting = querySelector('#ClearSorting')
    const ConfirmSorting = querySelector('#ConfirmSorting')

    // Content
    const ContentLeftCategories = querySelector('#ContentLeftCategories')
    const ContentLeftWeights = querySelector('#ContentLeftWeights')
    const ContentLeftPeople = querySelector('#ContentLeftPeople')

    const ContentLeft = querySelector('#ContentLeft')
    const ContentRight = querySelector('#ContentRight')

    // Get Tournament 
    const getTournamentCategoriesWeights = async () => {
        const response = await fetch(`/api/tournament/${tournamentId}/show-all-categories-weights/`)
        const data = await response.json()

        if (data.status == 'success') {
            renderTournamentCategoriesData(data.weights, 'categories')
        } else {
            console.error(`Couldn't get tournament ${data.message}`)
        }
    }

    getTournamentCategoriesWeights()

    // Render Tournament Categories
    function renderTournamentCategoriesData(data, status='') {
        if (status == 'categories') { // TODO: Categories
            ContentLeftCategories.innerHTML = ''
        } else if (status == 'weights') { // TODO: Weights
            ContentLeftWeights.innerHTML = ''
        } else if (status == 'athletes') { // TODO: Athletes
            ContentLeftPeople.innerHTML = ''
        }

        data.forEach((category, index) => {
            console.log('category: ', category)

            const div = document.createElement('div')
            div.classList.add('toss__content__category')

            if (status == 'categories') {
                // TODO: Categories

                div.addEventListener('click', () => {
                    renderTournamentCategoriesData(category.weights, 'weights')
                })

                div.innerHTML = `
                    ${category.gender == 'Мужской' ? '<i class="fa-solid fa-mars-stroke"></i>' : '<i class="fa-solid fa-venus"></i>' }
                    <h3 class='toss__content__category__title'>${category.year}</h3>
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
                        renderTournamentCategoriesData(category.athletes, 'athletes')
                        generateContentPlaces(athletes_count)
                    })
                } else {
                    div.style.opacity = .3
                }
            } else if (status == 'athletes') {
                // TODO: Athletes

                div.innerHTML = `
                    <h3 class='toss__content__category__title'>${category.fio}</h3>
                `

                div.draggable = true

            }

            if (status == 'categories') { // TODO: Categories
                ContentLeftCategories.appendChild(div)
            } else if (status == 'weights') { // TODO: Weights
                ContentLeftWeights.appendChild(div)
            } else if (status == 'athletes') { // TODO: Athletes
                ContentLeftPeople.appendChild(div)
            }

        })

    }

    function generateContentPlaces(num) {
        ContentRight.innerHTML = ''

        for (let i=0; i < num; i++) {
            console.log('Place', i)
            const div = document.createElement('div')
            div.classList.add('toss__content__place')

            ContentRight.appendChild(div)            
        }
    }

    HideContentCategories.addEventListener('click', () => {
        console.log(ContentLeft.style.gridTemplateColumns)

        if (ContentLeft.style.gridTemplateColumns == '' 
            || ContentLeft.style.gridTemplateColumns == '30% 15% 55%' ) {
            ContentLeft.style.gridTemplateColumns = '0 0 100%'

            ContentLeftCategories.style.opacity = "0"
            ContentLeftWeights.style.opacity = "0"
        } else {
            ContentLeft.style.gridTemplateColumns = '30% 15% 55%'

            ContentLeftCategories.style.opacity = "1"
            ContentLeftWeights.style.opacity = "1"
        }

    })
})