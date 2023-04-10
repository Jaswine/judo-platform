import React, {useEffect} from 'react'

const Home = () => {
  useEffect(()=>{
    const pageTitle = `${"Главная"}`
    document.title = pageTitle
  }, [])

  return (
    <div className='home-content'>
      <div className='home-info'>
        <h2>Турниры по дзюдо!</h2>
        <a className='home-info-link' href="/tournaments">Учавствовать</a>
      </div>
    </div>
  )
}

export default Home