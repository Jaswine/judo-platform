import React, {useState, useEffect} from 'react'
import axios from 'axios'
import { useNavigate } from 'react-router-dom'

const Signup = () => {
    const nav = useNavigate()

    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')

    const signup = async(e) =>{
        axios.post('http://module-a/api/v1/auth/signup', {
            username: username,
            password: password
        })
            .then((res)=>{
                localStorage.setItem('username', username)
                localStorage.setItem('token', res.data.token)

                nav('/')
                window.location.reload(true)
            })
            .catch((res)=>{
                alert(res.data)
            })
    }

    useEffect(()=>{
        const pageTitle = `${"Зарегистрироваться"}`
        document.title = pageTitle
    }, [])

  return (
    <div className='w-50 m-auto'>
    <h1 className="h3 mb-3 fw-normal">Регистрация</h1>

    <div className="form-floating mt-2">
      <input value={username} onChange={e=>setUsername(e.target.value)} type="login" className="form-control" id="floatingInput" placeholder="name@example.com"/>
      <label for="floatingInput">Имя пользователя</label>
    </div>
    <div className="form-floating mt-2">
      <input type="email" className="form-control" id="floatingPassword" placeholder="Password"/>
      <label for="floatingPassword">Электронная почта</label>
    </div>
    <div className="form-floating mt-2">
      <input value={password} onChange={e=>setPassword(e.target.value)} type="password" className="form-control" id="floatingPassword" placeholder="Password"/>
      <label for="floatingPassword">Пароль</label>
    </div>
    <div className="form-floating mt-2">
      <input type="password" className="form-control" id="floatingPassword" placeholder="Password"/>
      <label for="floatingPassword">Подтвердите пароль</label>
    </div>

    <button onClick={signup} className="mt-2 w-100 btn btn-lg btn-primary" type="submit">Зарегистрироваться</button>
    <p className="mt-5 mb-3 text-body-secondary">© 2017–2023</p>
    </div>
  )
}

export default Signup