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
            const div = document.createElement('div')
            div.classList.add('toss__content__category')

            if (status == 'categories') {
                // TODO: Categories

                div.addEventListener('click', () => {
                    renderTournamentCategoriesData(category.weights, 'weights')
                })

                div.innerHTML = `
                    ${category.gender == 'Мужской' ? "<i class='fa-solid fa-mars-stroke'></i>" : "<i class='fa-solid fa-venus'></i>" }
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
                        renderContentPlaces(generateContentPlaces(athletes_count))
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

    /* 
        TODO: Генерация базовой сетки, 
        TODO:               куда будут вставляться пользователи
    */
    function generateContentPlaces(num) {
        ContentRight.innerHTML = ''

        let jsonGrid = []
        let baseNumber = 4
        

        if ( num > 5 && num < 8) baseNumber = 3
        else if (num > 3 && num < 6) baseNumber = 2
        else if (num > 1 && num < 4)  baseNumber = 1
        else if (num < 2)  return null


        jsonGrid = generateBaseFourArrays(jsonGrid, baseNumber)

        let rangeI = 0
        let [firstHalf, secondHalf] = splitNumber(num);
        console.log(firstHalf, secondHalf)

        for (let i=0; i<firstHalf.length; i++) {
            rangeI % baseNumber == 0 ? rangeI = 1 : rangeI++

            let newObj = {}
            firstHalf[i] ? newObj[firstHalf[i]] = "" : ""
            secondHalf[i] ? newObj[secondHalf[i]] = "" : ""
            
            console.log(`${rangeI} секция`, i)

            const gridMapping = [
                [0, 1],        // baseNumber = 2, 
                [0, 2, 1],     // baseNumber = 3, 
                [0, 2, 1, 3]   // baseNumber = 4, 
            ];

            if (baseNumber >= 2 && baseNumber <= 4 && rangeI >= 1 && rangeI <= 4) {
                const index = gridMapping[baseNumber - 2][rangeI - 1];
                if (index !== undefined) {
                    jsonGrid[index].splice(0, 0, newObj);
                }
            }
            
        }

        return jsonGrid
    }

    /* 
        TODO: Генерация 4 списков
    */
    function generateBaseFourArrays(jsonGrid, baseNumber) {
        for (let i=1; i<=baseNumber; i++) {
            let innerArray = [];
            jsonGrid.push(innerArray);
        }

        return jsonGrid
    }

    /* 
        TODO:   Деление даваемого числа на два 
        TODO:           и создание с помощью него 2 списков с числами 
    */
    function splitNumber(num) {
        let massive = []
        let del_num1 = num

        for (let i = 1; i <= num; i++) {
            massive.push(i)
        }
        
        num % 2 == 0 ? del_num1 = num / 2  : del_num1 = num / 2 + 0.5

        return [massive.slice(0, del_num1), massive.slice(del_num1, num)]; 
    }
    

    /* 
        TODO: Рендеринг сетки в виде полей 
    */
    function renderContentPlaces(data) {
        // const div = document.createElement('div')
        // div.classList.add('toss__content__place')

        // div.innerHTML += `<i>${i}.</i>`

        // ContentRight.appendChild(div)
        console.log('Базовая сетка: ', data)    
    }

    HideContentCategories.addEventListener('click', () => {
        if (ContentLeft.style.gridTemplateColumns == '' 
            || ContentLeft.style.gridTemplateColumns == '30% 15% 55%' ) {
            ContentLeft.style.gridTemplateColumns = '0 0 100%'

            ContentLeftCategories.style.opacity = '0'
            ContentLeftWeights.style.opacity = '0'
        } else {
            ContentLeft.style.gridTemplateColumns = '30% 15% 55%'

            ContentLeftCategories.style.opacity = '1'
            ContentLeftWeights.style.opacity = '1'
        }

    })
})