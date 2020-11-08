import React from "react"
import { Link } from "react-router-dom"
import './Header.css'
import Logo from './images/header_logo.png'

function Header(){
  return(
    <nav className="header">
      {/*header logo*/}
      <Link to="/">
        <img className="header__logo" src={Logo} alt="header-logo " />
      </Link>


      {/*login link in header*/}
      <div className="header__nav">
        <Link to="/login" className="header__link">
          <div className="header__option">
            <span className="header__optionLineOne">Hello,</span>
            <span className="header__optionLineTwo">Sign In</span>
          </div>
        </Link>
      </div>

    </nav>
  )
}

export default Header
