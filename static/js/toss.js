document.addEventListener('DOMContentLoaded', () => {
    // Сетка участников
    var jsonGrid = []

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

                jsonGrid = []
                let athletes_count = category.athletes.length
                div.innerHTML = `
                    <h3 class='toss __content__category__title'>${category.name}</h3>
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
                let id = `Element-${category.id}-${category.fio}`

                div.id = id
                div.style.cursor = 'grab'
                div.draggable = true

                div.addEventListener('dragstart', (e) => {
                    e.dataTransfer.setData('text/plain', id); 
                })

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
        let baseNumber = 4
        
        if ( num > 5 && num < 8) baseNumber = 3
        else if (num > 2 && num < 6) baseNumber = 2
        else if (num > 1 && num < 3)  baseNumber = 1
        else if (num < 2)  return null


        jsonGrid = generateBaseFourArrays(jsonGrid, baseNumber)

        let rangeI = 0
        let [firstHalf, secondHalf] = splitNumber(num);
        // console.log(firstHalf, secondHalf)

        for (let i=0; i<firstHalf.length; i++) {
            rangeI % baseNumber == 0 ? rangeI = 1 : rangeI++

            let newObj = {}
            firstHalf[i] ? newObj[firstHalf[i]] = "" : ""
            secondHalf[i] ? newObj[secondHalf[i]] = "" : ""            

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
        ContentRight.innerHTML = ''

        // console.log('Базовая сетка: ', data)

        if (data.length == 4) {
            for (let i = 0; i < data.length; i++) {
                const data_reverse = data[i]

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

                            div_el.innerHTML += `<i>${key}.</i>`

                            if (obj[key].length != 0) {
                                const div_cat = document.createElement('div')
                                div_cat.classList.add('toss__content__category')

                                div_cat.innerHTML = `<h3 class='toss__content__category__title'>${obj[key]}</h3>`

                                let div_cat_id = `Element-${obj[key]}`

                                div_cat.id = div_cat_id
                                div_cat.style.cursor = 'grab'
                                div_cat.draggable = true

                                div_cat.addEventListener('dragstart', (e) => {
                                    e.dataTransfer.setData('text/plain', id); 
                                })

                                div_el.appendChild(div_cat)
                            }

                            div_el.addEventListener('dragover', (e) => {
                                e.preventDefault();
                            }) 
                            
                            div_el.addEventListener('drop', (e) => {
                                e.preventDefault();
                                const eData = e.dataTransfer.getData('text/plain');
                                const eDataList = eData.split('-')
                                console.log('Order:', id, 'Item: ', eData)
                                
                                // jsonGrid[i].splice(j, 0, newObj);
                                // console.log(jsonGrid[i][j][key])
                                jsonGrid[i][j][key] = eDataList[2]
                                renderContentPlaces(jsonGrid)

                                // const draggedItem = document.getElementById(data);
                                // e.target.appendChild(draggedItem);
                            })

                            div.appendChild(div_el)
                        }
                    }

                    ContentRight.appendChild(div)
                }
            }
        }

    }

    /*
        TODO: Скрытие 2 списков категорий
    */
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