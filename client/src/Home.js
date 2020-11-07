import React from "react"
import './Home.css'
import Banner from './images/banner.jpg'

function Home(){
  return(
    <div className="home">
      {/*fading banner*/}
      { /*issue: taking image from folder */}
      <img src={Banner}
      className="home__image"
      />

      {/*About Us*/}
      <div className="home__about">

      </div>

      {/*categories: transportation, food, stationary */}
      <div className="home__transportation">
      <img src=" " className="home__trasportImage" />
      </div>

      <div className="home__food">
        <img src=" " className="home__foodImage" />
      </div>

      <div className="home__stationary">
        <img src=" " className="home__statImage" />
      </div>
    </div>
  )
}

export default Home
