document.addEventListener('DOMContentLoaded', () => {
    const TournamentList = document.querySelector('#TournamentList')
    const TournamentForm = document.querySelector('#TournamentForm')

    const getTournamentList = (search='', startDate='', endDate='') => {
        fetch(`/api/tournament-list/?search=${search}&startDate=${startDate}&endDate=${endDate}`)
            .then((response) => response.json())
            .then((data) => {
                TournamentList.innerHTML = ''

                if (data.tournament_list.length > 0) {                    
                   data.tournament_list.forEach((tournament, index) => {
                        const div = document.createElement('div')
                        div.classList.add('tournament')

                        const div_header = document.createElement('div')
                        div_header.classList.add('tourname__header')
                        div_header.innerHTML = `
                            <img src="${tournament.logo}" alt="${tournament.title}">
                            <a href="/tournaments/${tournament.slug}/">${tournament.title}...</a>
                        `
                        div.appendChild(div_header)

                        const div_description = document.createElement('div')
                        div_description.classList.add('tournament__description')
                        div_description.innerHTML = `
                        <div class="tournament__description__line">
                            <h4><i class="fa-solid fa-city"></i></h4>
                            ${tournament.place}
                        </div>
                        <div class="tournament__description__line">
                            <h4>  <i class="fa-solid fa-earth-americas"></i></h4> 
                            ${ tournament.rang}
                        </div>
                        <div class="tournament__description__line">
                                <h4><i class="fa-solid fa-calendar-days"></i></h4>
                            ${tournament.startDate} - ${tournament.endDate}
                        </div>
                        <div class="tournament__description__line">
                        <h4><i class="fa-solid fa-square-pen"></i> </h4>
                        <span ${tournament.status == 'Регистрация завершенa' ? 
                                                    'style="color: #ff8181"': 
                                                    'style="color: #81a7ff;"'}
                        >${tournament.status} </span>
                    </div>
                    <div class="tournament__description__line">
                        <i class="fa-solid fa-users"></i>0
                    </div>
                        `
                    
                        div.appendChild(div_description)

                        const div_tags = document.createElement('div')
                        div_tags.classList.add('tournament__categories')

                        tournament.categories.forEach(category => {
                            const div_tag = document.createElement('div')
                            div_tag.classList.add('tournament__category')

                            if (category.gender == 'Мужской') {
                                div_tag.style.border = '2px solid #81a7ff'
                                div_tag.style.color = '#81a7ff'

                                div_tag.innerHTML = `
                                    <i class="fa-solid fa-person"></i>
                                    ${category.year}
                                `
                            } else {
                                div_tag.style.border = '2px solid #ff81a7'
                                div_tag.style.color = '#ff81a7'   

                                div_tag.innerHTML = `
                                    <i class="fa-solid fa-person-dress"></i>
                                    ${category.year}
                                `
                            }

                            div_tags.appendChild(div_tag)
                        })
                        
                        div.appendChild(div_tags)

                        if (tournament.user.username != '') {
                            const div_buttons = document.createElement('div')
                            div_buttons.classList.add('tournament__buttons')

                            if (tournament.user.type == 'Админ' || tournament.user.type == 'Секретарь' || tournament.user.status) {
                                if (tournament.status == 'Регистрация открыта') {
                                    div_buttons.innerHTML += `
                                        <a href="/tournaments/${tournament.slug}/registration-on-tournament" class="btn">Регистрация</a>
                                    `
                                }
                                div_buttons.innerHTML += `
                                    <a href="/tournaments/${tournament.slug}/panel/update-info" class="btn">Изменить</a>
                                    <a href="/tournaments/${tournament.slug}/toss" class="btn">Сортировка</a>
                                    `
                            }
                            div.appendChild(div_buttons)
                        }

                        TournamentList.appendChild(div)
                   })
                } else {
                    const notFoundElement = document.createElement('div')
                    notFoundElement.className = 'tournaments__not__found'
                    notFoundElement.innerHTML = `<h2>Турниры не найдены</h2>`

                    TournamentList.appendChild(notFoundElement)
                }
            })
    }

    getTournamentList()
        
    TournamentForm.addEventListener('submit', (e) => {
        e.preventDefault()

        getTournamentList(e.target[1].value, e.target[2].value, e.target[3].value)
    })
})