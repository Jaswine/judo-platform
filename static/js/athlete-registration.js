
document.addEventListener('DOMContentLoaded', () => {
    const left_body = document.querySelector('.athlete_regisration__left__body')
    const TournamentID = document.querySelector('#TournamentID').value

    const getAthletes = () => {
        fetch(`/api/athlete-registration/${TournamentID}/`)
            .then((response) => response.json())
            .then(data => {
                console.log(data)
            })
    }

    getAthletes()
})