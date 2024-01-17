document.addEventListener('DOMContentLoaded', () => {
    const left_body = document.querySelector('.athlete_regisration__left__body')
    const TournamentID = document.querySelector('#TournamentID').value

    const getAthletes = () => {
        fetch(`/api/list-of-registered-on-tournament/${TournamentID}/`)
            .then((response) => response.json())
            .then(data => {
                console.log(data)
                left_body.innerHTML = ''

                if (data.athletes.length > 0) {
                    data.athletes.forEach((athlete, index) =>{
                        const athlete_form = document.createElement('form')
                        athlete_form.classList.add('athlete_regisration__left__person')

                        athlete_form.innerHTML += `
                            <span>${ index+1}.</span>
                            <input type="hidden" name="athlete" value="${athlete.id}" />
                            <b>${athlete.fio}</b>
                            <span>${athlete.year}</span>
                            <span>${athlete.discharge}</span>
                            <input type="hidden" name="weight" value="${athlete.weights[0].id}" />
                            <span>${athlete.weights[0].name}</span>
                            <button type="button" class='btn'>-</button>
                        `
                        
                        left_body.appendChild(athlete_form)
                    })

                    const add_more = document.createElement('div')
                    add_more.innerHTML = `<a href="{% url 'base:add_new_athlete' %}" class="btn btn--primary">Добавить нового спортсмена</a>`
                    left_body.appendChild(add_more)
                }
            })
    }

    left_body.addEventListener('click', (e) => {
        if (e.target.classList.contains('btn')) {
            const athlete  = e.target.parentNode
            let formData = new FormData(athlete);

            fetch(`/api/list-of-registered-on-tournament/${TournamentID}/`, {
                method: 'POST',
                body: formData,
            })
                .then(response => response.json())
                .then(data => {
                    console.log(data);
                    getAthletes()
                })
        }
    })

    getAthletes()

})