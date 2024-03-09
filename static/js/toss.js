document.addEventListener('DOMContentLoaded', () => {
    // Сетка участников
    var jsonGrid = globalAthletes = []
    var currentCategory = currentWeight = ""
    const csrfToken = document.querySelector('[name="csrfmiddlewaretoken"]')

    const messages = document.querySelector('.global__messages')
    const dateTime = new Date()

    // Query Selector
    const querySelector = (selector) => { return document.querySelector(selector) }

    // Tournament Data
    const tournamentId = querySelector('#TournamentId').value
    const tournamentStartDate = querySelector('#TournamentStartDate').value
    const tournamentEndDate = querySelector('#TournamentEndDate').value

    const tournamentStartDateFormat = new Date(tournamentStartDate);
    const tournamentEndDateFormat = new Date(tournamentEndDate);

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
                    currentCategory = category.id
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
                        
                        currentWeight = category.id

                        if (category.sorting) {
                            jsonGrid = JSON.parse(category.sorting)
                            renderContentPlaces(jsonGrid)
                        } else {
                            renderTournamentCategoriesData(globalAthletes, 'athletes')
                            renderContentPlaces(generateContentPlaces(jsonGrid, athletes_count))
                        }
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

        console.log(jsonGrid)
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

        if (data.length >= 2) {
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
                            
                            if (dateTime > tournamentStartDateFormat) {
                                div_el.style.opacity = .5
                            }

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
        } else {
            const div = document.createElement('div')
            div.classList.add('little-people')
            div.innerHTML = "Not many people in the area"
            ContentRight.appendChild(div)
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
        if (dateTime < tournamentStartDateFormat) {
            place.addEventListener('dragover', (e) => {
                e.preventDefault();
            }) 

            place.addEventListener('drop', (e) => {
                e.preventDefault();

                const eDataId = e.dataTransfer.getData('text/plain');
                const data = JSON.parse(eDataId)

                const dropped = e.target;

                if (dragged.parentNode.id == 'ContentLeftPeople') {
                    const getAthleteFromContentLeftPeopleById = document.querySelector(`#${data.elementId}`)
                    ContentLeftPeople.querySelector(`#${data.elementId}`)? ContentLeftPeople.removeChild(getAthleteFromContentLeftPeopleById) : ""

                    if (!dropped.querySelector('i')) {
                        const div_cat = document.createElement('div')
                        div_cat.classList.add('toss__content__category')

                        let oldObj = {}
                        oldObj['id'] = dropped.parentNode.id.slice(8)
                        oldObj['fio'] = dropped.innerHTML

                        FormationAthletesData(div_cat, oldObj)
                        ContentLeftPeople.appendChild(div_cat)
                    }
                } else if (dragged.parentNode.id.slice(0, 5) == 'Place') {
                    if (dropped.querySelector('i')) {
                        let dragged_place = dragged.parentNode.id.slice(6).split('-')
                        jsonGrid[dragged_place[0]][dragged_place[1]][dragged_place[2]] = {}
                    } else {
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
        } else {
            MessageRender("Срок изменения истек!", 'error')
        }
   }

    getTournamentCategoriesWeights()

    /*
        TODO: Отрисовка
    */
    DrawSorting.addEventListener('click', () => {
        if (dateTime > tournamentStartDateFormat) {
            MessageRender('Срок изменения истек!', 'error')
            return
        }
        
        if (currentCategory.length == 0) {
            MessageRender("Для продолжения выберите категорию!", 'error')
            return
        }

        if (currentWeight.length == 0) {
            MessageRender('Для продолжения выберите вес!', 'error')
            return
        }
        
        let sorted_athletes = globalAthletes.sort(() => Math.random() - 0.5)

        let data = jsonGrid
        
        if (data.length >= 2) {
            let c = 0
            for (let i = 0; i < data.length; i++) {
                for (let j = 0; j < data[i].length; j++) {
                    let obj = data[i][j]

                    for (const key in obj) {
                        if (Object.hasOwnProperty.call(obj, key)) {
                            let el = sorted_athletes[c]

                            const getAthleteFromContentLeftPeopleById = document.querySelector(`#Element-${el.id}`)
                            ContentLeftPeople.querySelector(`#Element-${el.id}`)? 
                                ContentLeftPeople.removeChild(getAthleteFromContentLeftPeopleById) : ""

                            obj[key] = el
                            c++
                        }
                    }

                }
            }
        } else {
            MessageRender('Слишком мало людей для сортировки!', 'error')
        }

        renderContentPlaces(data)
    })

    /*
        TODO: Очистка всех данных в схеме
    */
    ClearSorting.addEventListener('click', () => {
        if (dateTime > tournamentStartDateFormat) {
            MessageRender('Срок изменения истек!', 'error')
            return
        }

        if (currentCategory.length == 0) {
            MessageRender('Для продолжения выберите категорию!', 'error')
            return
        }

        if (currentWeight.length == 0) {
            MessageRender('Для продолжения выберите вес!', 'error')
            return
        }

        if (jsonGrid.length > 1) {
            if (confirm('Полностью очистить текущую схему?')) {
                jsonGrid = []

                renderTournamentCategoriesData(globalAthletes, 'athletes')

                renderContentPlaces(generateContentPlaces(jsonGrid, globalAthletes.length))
            }
        } else {
            MessageRender('Слишком мало людей!', 'error')
        }
    })

    /*
        TODO: Подтверждение и сохранение
    */
    ConfirmSorting.addEventListener('click', async () => {
        if (dateTime > tournamentStartDateFormat) {
            MessageRender('Срок изменения истек!', 'error')
            return
        }

        if (currentCategory.length == 0) {
            MessageRender('Для продолжения выберите категорию!', 'error')
            return
        }

        if (currentWeight.length == 0) {
            MessageRender('Для продолжения выберите вес!', 'error')
            return
        }

        if (jsonGrid != [] && jsonGrid.length > 1) {
            let isFieldsSaved = JsonGridCheckFull(jsonGrid)

            if (isFieldsSaved) {
                if (confirm('Вы действительно хотите сохранить изменения?')) {

                    let formData = new FormData(ContentRight)

                    formData.append('data', JSON.stringify(jsonGrid))
                    formData.append('csrfmiddlewaretoken', csrfToken.value);

                    fetch(`/api/tournaments/${tournamentId}/weight/${currentWeight}/update`, {
                        method: 'POST',
                        body: formData,
                    })
                        .then(res => res.json())
                        .then(data => {
                            MessageRender(data.message, data.status)
                        })
                        .catch(err => {
                            console.error(err)
                        })
                }
            }
        } else {
            MessageRender('Слишком мало людей!', 'error')
        }
    })

    /*
        TODO: Проверка, что сетка полностью заполнена
    */
    function JsonGridCheckFull(data) {
        let allFilled = true

        for (let i = 0; i < data.length; i++) {
            for (let j = 0; j < data[i].length; j++) { 
                for (const key in data[i][j]) {
                    if (Object.hasOwnProperty.call(data[i][j], key)) {                          
                        if (!data[i][j][key]) {
                            allFilled = false
                            break
                        }
                    }
                }
            }
        }

        return allFilled
    }


    /*
        TODO: Рендеринг сообщений
    */
   function MessageRender(message, status) {
        const div = document.createElement('div')
        div.classList.add('global__message')

        div.innerHTML = message

        switch (status) {
            case "success": 
                div.style.backgroundColor = `#10ef7f`;
                break;
            case "error":
                div.style.backgroundColor = `#ff5b5b`;
                break;
            case "warn":
                div.style.backgroundColor = `#ffd21e`;
                break;
            case "info":
                div.style.backgroundColor = `#a1a1a1`;
                break;
        }

        setTimeout(() => {
            div.style.opacity = 0

            setTimeout(() => {
                div.style.display = 'none'
            }, 300)
        }, 3000)
        
        messages.appendChild(div)
   }


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