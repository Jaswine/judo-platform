import React, {useState, useEffect} from 'react'

const DeleteAccount = () => {
    const [username, setUsername] = useState(localStorage.getItem('username'))

    useEffect(()=>{
        const pageTitle = `${"Delete account"}`
        document.title = pageTitle
    }, [])

    const Logout = () => {
        localStorage.clear()

        window.location.reload(true)
    }

  return (
    <div className='d-flex'>
        <nav id="sidebarMenu" className="col-md-3 col-lg-2 d-md-block bg-body-tertiary sidebar collapse">
      <div className="position-sticky pt-3 sidebar-sticky">
        <ul className="nav flex-column">
          <li className="nav-item">
            <a className="nav-link active" aria-current="page" href="#">
              <h4>{username}</h4>
            </a>
          </li>
          <li className="nav-item">
            <a className="nav-link" href="/cabinet">
              <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" className="feather feather-file align-text-bottom" aria-hidden="true"><path d="M13 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9z"></path><polyline points="13 2 13 9 20 9"></polyline></svg>
              Info
            </a>
          </li>
          <li className="nav-item">
            <a className="nav-link" href="/edituser">
              <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" className="feather feather-shopping-cart align-text-bottom" aria-hidden="true"><circle cx="9" cy="21" r="1"></circle><circle cx="20" cy="21" r="1"></circle><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"></path></svg>
              Edit
            </a>
          </li>
          <li className="nav-item">
            <a className="nav-link" href="/" onClick={Logout}>
              <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" className="feather feather-users align-text-bottom" aria-hidden="true"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>
              Logout
            </a>
          </li>
        </ul>
      </div>
    </nav>
    <main className="col-md-9 ms-sm-auto col-lg-10 px-md-4">
      <div className="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pt-3 pb-2 mb-3 border-bottom">
        <h1 className="h2">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" className="feather feather-users align-text-bottom" aria-hidden="true"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>
            Delete account
        </h1>
      </div>
      <button className='btn btn-primary btn-lg px-4 gap-3 mt-3'>Delete account</button>
    </main>
    </div>
  )
}

export default DeleteAccount