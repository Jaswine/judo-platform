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
        const response = await fetch(`/api/tournament/${tournamentId}/show-all-categories-weights-sorting/`)
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
                div.innerHTML = `
                    <h3 class='toss__content__category__title'>${category.name}</h3>
                `

                console.log(category.sorting)
                if (category.sorting && category.sorting.length > 1) {
                    div.addEventListener('click', () => {
                        currentWeightName = category.name

                        jsonGrid = JSON.parse(category.sorting)
                        renderContentPlaces(jsonGrid)
                    })
                } else {
                    div.style.opacity = .3
                }
            }

            if (status == 'categories') { // TODO: Categories
                ContentLeftCategories.appendChild(div)
            } else if (status == 'weights') { // TODO: Weights
                ContentLeftWeights.appendChild(div)
            }
        })

    }

    /*
        TODO: Рендеринг сетки в виде полей
    */
    function renderContentPlaces(data) {
        ContentRight.innerHTML = ''

        for (let i = 0; i < data.length; i++) {
            const data_reverse = data[i]

            const pre_div = document.createElement('div')
            pre_div.classList.add('toss__content__four__place')

            console.log(i)
            switch (i) {
                case 0:
                    pre_div.innerHTML += "<h4> Pool A </h4>"
                    break
                case 1:
                    pre_div.innerHTML += "<h4> Pool B </h4>"
                    break
                case 2:
                    pre_div.innerHTML += "<h4> Pool C </h4>"
                    break
                case 3:
                    pre_div.innerHTML += "<h4> Pool D </h4>"
                    break
            }

            for (let j = 0; j < data_reverse.length; j++) {
                const div = document.createElement('div')
                div.classList.add('toss__content__two__place')
                div.id = `Place-${i}-${j}`

                let obj = data_reverse[j]

                for (const key in obj) {
                    if (Object.hasOwnProperty.call(obj, key)) {
                        const div_el = document.createElement('div')
                        div_el.classList.add('toss__content__place')

                        const id = `Place-${i}-${j}-${key}`
                        div_el.id = id

                        if (i % 2 == 0) {
                            div_el.style.backgroundColor = 'rgb(87,127,220, .2)'
                        }

                        div_el.innerHTML += `<i class="non-selectable">${key}.</i>`

                        if (obj[key] && obj[key].length != 0) {
                            if (Object.keys(obj[key]).length) {
                                const div_cat = document.createElement('div')
                                div_cat.classList.add('toss__content__category', 'protocol__content__category')

                                FormationAthletesData(div_cat, obj[key])

                                div_el.appendChild(div_cat)
                            }
                        }

                        div.appendChild(div_el)
                    }

                }

                pre_div.appendChild(div)
            }

            ContentRight.appendChild(pre_div)
        }
    }

    /*
        TODO: Формирование компонента студента
    */
    function FormationAthletesData(div, category) {
        div.id = `Element-${category.id}`
        div.innerHTML = `<h3 class='toss__content__category__title'>${category.fio}</h3>`
        return div
    }

    getTournamentCategoriesWeights()


})