import React, {useState} from 'react'

const Header = () => {
    const [username, setUsername] = useState(localStorage.getItem('username'))
    const [token, setToken] = useState(localStorage.getItem('token'))

    const Logout = () => {
        localStorage.clear()

        window.location.reload(true)
    }

  return (
    <div>
        <div className="container">
    <header className="header d-flex flex-wrap justify-content-center py-3">
      <a href="/" className="d-flex align-items-center mb-3 mb-md-0 me-md-auto link-body-emphasis text-decoration-none">
        <span className="fs-4">JUDO</span>
      </a>

      <ul className="nav nav-pills">
        <li className="nav-item"><a href="/" className="nav-link">Главная</a></li>
        <li className="nav-item"><a href="/tournaments" className="nav-link">Турниры</a></li>
        {!token?(
            <>
                <li className="nav-item"><a href="/signin" className="nav-link">Авторизация</a></li>
                <li className="nav-item"><a href="/signup" className="nav-link">Регистрация</a></li>
            </>
        ):
            <>
                <li className="nav-item"><a href="/cabinet" className="nav-link">{username}</a></li>
                <li className="nav-item"><a href="#" onClick={Logout} className="nav-link">Выйти</a></li>
            </>
        }
      </ul>
    </header>
  </div>
    </div>
  )
}

export default Header