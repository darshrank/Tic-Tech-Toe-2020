import React from "react"
import {Link} from "react-router-dom"
import './Login.css'
import Logo from './images/header_logo.png'

function Login (){
  return(
    <div className="login">
      <Link to='/'>
        <img className="login__logo" src={Logo} />
      </Link>

      <div className="login__container">
        <h1>Sign-In</h1>
        <form>
          <h5>E-mail</h5>
          <input type='text' />

          <h5>Password</h5>
          <input type='password' />

          <button className="login__signInButton">Sign In</button>
        </form>
        <p>By signing in you agree to parent pay conditions of use and sale.</p>
        <button className="login__registerButton">Create Your Account</button>
      </div>
    </div>
  )
}

export default Login
