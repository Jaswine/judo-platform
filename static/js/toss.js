document.addEventListener('DOMContentLoaded', () => {
    // Сетка участников
    var jsonGrid = globalAthletes = removedElements = []

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
                        globalAthletes = category.athletes
                        jsonGrid = []
                        
                        renderTournamentCategoriesData(globalAthletes, 'athletes')
                        renderContentPlaces(generateContentPlaces(jsonGrid, athletes_count))
                    })
                } else {
                    div.style.opacity = .3
                }
            } else if (status == 'athletes') {
                // TODO: Athletes
                
                FormationAthletesData(div, category)
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
    function generateContentPlaces(jsonGrid, num) {
        let baseNumber = 4
        
        if ( num > 5 && num < 8) baseNumber = 3
        else if (num > 2 && num < 6) baseNumber = 2
        else if (num > 1 && num < 3)  baseNumber = 1
        else if (num < 2)  return null

        jsonGrid = generateBaseFourArrays(jsonGrid, baseNumber)

        let rangeI = 0
        let [firstHalf, secondHalf] = splitNumber(num);

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
        TODO:               и создание с помощью него 2 списков с числами 
    */
    function splitNumber(num) {
        let massive = []
        let del_num1 = num

        for (let i = 1; i <= num; i++) { massive.push(i) }
        
        num % 2 == 0 ? del_num1 = num / 2  : del_num1 = num / 2 + 0.5

        return [massive.slice(0, del_num1), massive.slice(del_num1, num)]; 
    }
    

    /* 
        TODO: Рендеринг сетки в виде полей 
    */
    function renderContentPlaces(data) {
        ContentRight.innerHTML = ''

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

                            div_el.innerHTML += `<i class="non-selectable">${key}.</i>`

                            if (obj[key] && obj[key].length != 0) {
                                if (Object.keys(obj[key]).length) {
                                    const div_cat = document.createElement('div')
                                    div_cat.classList.add('toss__content__category')

                                    FormationAthletesData(div_cat, obj[key])
                                    
                                    div_el.appendChild(div_cat)
                                }
                            }

                            DropAndDragOverFormation(div_el, jsonGrid, i, j, key)

                            div.appendChild(div_el)
                        }
                    }

                    ContentRight.appendChild(div)
                }
            }
        }
    }

    /* 
        TODO: Формирование компонента студента
    */
    function FormationAthletesData(div, category) {
        div.innerHTML = `
            <h3 class='toss__content__category__title'>${category.fio}</h3>
        `

        let id = `Element-${category.id}`
        div.id = id

        let newObj = {}
        newObj['id'] = category.id
        newObj['fio'] = category.fio
        newObj['elementId'] = id

        div.style.cursor = 'grab'
        div.draggable = true

        div.addEventListener('dragstart', (e) => {
            dragged = e.target;
            e.dataTransfer.setData('text/plain', JSON.stringify(newObj)); 
        })

        return div
    }

    /*
        TODO: Добавление DragOver и Drop к чему-то
    */
   function DropAndDragOverFormation(place, jsonGrid, i, j, key) {
        place.addEventListener('dragover', (e) => {
            e.preventDefault();
        }) 

        place.addEventListener('drop', (e) => {
            e.preventDefault();

            const eDataId = e.dataTransfer.getData('text/plain');
            const data = JSON.parse(eDataId)

            const dropped = e.target;

            console.warn('dragged.parentNode: ', dragged.parentNode)
            console.log('dropped.classList: ', dropped.classList)

            if (dragged.parentNode.id == 'ContentLeftPeople') {
                const getAthleteFromContentLeftPeopleById = document.querySelector(`#${data.elementId}`)
                ContentLeftPeople.querySelector(`#${data.elementId}`)? ContentLeftPeople.removeChild(getAthleteFromContentLeftPeopleById) : ""
            } else if (dragged.parentNode.id.slice(0, 5) == 'Place') {
                // if (dropped.classList.contains('toss__content__category__title')) {
                //    
                // } else {
                //     
                // }

                if (dropped.querySelector('i')) {
                    let dragged_place = dragged.parentNode.id.slice(6).split('-')
                    jsonGrid[dragged_place[0]][dragged_place[1]][dragged_place[2]] = {}
                    // console.log(' dragged.parentNode', dragged.parentNode)
                } else {
                    console.log('Dropped Subject', dropped)
                    let oldObj = {}
                    oldObj['id'] = dropped.parentNode.id.slice(8)
                    oldObj['fio'] = dropped.innerHTML

                    let dragged_place = dragged.parentNode.id.slice(6).split('-')
                    jsonGrid[dragged_place[0]][dragged_place[1]][dragged_place[2]] = oldObj
                }
            }
            
            let newObj = {}
            newObj['id'] = data.id
            newObj['fio'] = data.fio

            jsonGrid[i][j][key] = newObj
            renderContentPlaces(jsonGrid)
        })
   }

    getTournamentCategoriesWeights()


    /*
        TODO: Очистка всех данных в схеме
    */
    ClearSorting.addEventListener('click', () => {
        if (confirm('Полностью очистить текущую схему?')) {
            jsonGrid = []

            renderTournamentCategoriesData(globalAthletes, 'athletes')

            renderContentPlaces(generateContentPlaces(jsonGrid, globalAthletes.length))
        }
    })

    /*
        TODO: Скрытие 2 списков категорий,
        TODO:                    при нажатии на кнопку c ID =
    */
    HideContentCategories.addEventListener('click', () => {
        if (ContentLeft.style.gridTemplateColumns == '' 
            || ContentLeft.style.gridTemplateColumns == '30% 15% 55%' ) {
            changeHideContentCategoriesStyles( '0 0 100%', 0, 0)
        } else {
            changeHideContentCategoriesStyles('30% 15% 55%', 1, 1)
        }
    })

    function changeHideContentCategoriesStyles(gtc, catOpac, weightOpac ) {
        ContentLeft.style.gridTemplateColumns = gtc

        ContentLeftCategories.style.opacity = catOpac
        ContentLeftWeights.style.opacity = weightOpac
    }
})